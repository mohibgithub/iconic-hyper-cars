const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(express.json());
app.use(cookieParser());

// Serve static frontend files from root directory
app.use(express.static(path.join(__dirname)));

// Supabase Client Setup
const supabaseUrl = process.env.SUPABASE_URL;
const supabaseAnonKey = process.env.SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey || supabaseUrl.includes('your-project') || supabaseAnonKey.includes('your-supabase-anon')) {
  console.warn('========================================================================');
  console.warn('⚠️  WARNING: Supabase URL or Anon Key is missing or using placeholders in .env!');
  console.warn(' Please update your .env file with actual credentials to use authentication.');
  console.warn('========================================================================');
}

const supabase = createClient(supabaseUrl || 'https://placeholder.supabase.co', supabaseAnonKey || 'placeholder');

// --- AUTHENTICATION API ROUTES ---

// 1. Signup Route
app.post('/api/auth/signup', async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // Basic Validations
    if (!name || !email || !password) {
      return res.status(400).json({ error: 'All fields (name, email, password) are required.' });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: 'Password must be at least 6 characters long.' });
    }

    // Call Supabase Signup
    const { data, error } = await supabase.auth.signUp({
      email: email.toLowerCase(),
      password: password,
      options: {
        data: {
          name: name
        }
      }
    });

    if (error) {
      return res.status(400).json({ error: error.message });
    }

    if (!data.user) {
      return res.status(400).json({ error: 'Registration failed.' });
    }

    // Set cookie if a session is immediately created
    if (data.session) {
      res.cookie('token', data.session.access_token, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
      });
    }

    // Fetch user's role from the public.profiles table (created automatically by trigger)
    let role = 'user';
    const { data: profile, error: profileErr } = await supabase
      .from('profiles')
      .select('role')
      .eq('id', data.user.id)
      .single();

    if (profile) {
      role = profile.role;
    }

    res.status(201).json({
      success: true,
      user: {
        id: data.user.id,
        name: data.user.user_metadata?.name || name,
        email: data.user.email,
        role: role
      }
    });
  } catch (error) {
    console.error('Signup error:', error);
    res.status(500).json({ error: 'Internal server error during registration.' });
  }
});

// 2. Login Route
app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password are required.' });
    }

    // Call Supabase sign in
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.toLowerCase(),
      password: password
    });

    if (error) {
      return res.status(401).json({ error: error.message });
    }

    if (!data.user || !data.session) {
      return res.status(400).json({ error: 'Authentication failed.' });
    }

    // Set cookie with token
    res.cookie('token', data.session.access_token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
    });

    // Fetch user's role from profiles table
    let role = 'user';
    const { data: profile } = await supabase
      .from('profiles')
      .select('role')
      .eq('id', data.user.id)
      .single();

    if (profile) {
      role = profile.role;
    }

    res.status(200).json({
      success: true,
      user: {
        id: data.user.id,
        name: data.user.user_metadata?.name || 'User',
        email: data.user.email,
        role: role
      }
    });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ error: 'Internal server error during authentication.' });
  }
});

// 3. Get Authenticated User Details (Check Session)
app.get('/api/auth/me', async (req, res) => {
  try {
    const token = req.cookies.token;
    if (!token) {
      return res.status(401).json({ error: 'Not authenticated.' });
    }

    // Verify token with Supabase Auth
    const { data: { user }, error } = await supabase.auth.getUser(token);

    if (error || !user) {
      return res.status(401).json({ error: 'Invalid session or token.' });
    }

    // Fetch role from profiles table
    let role = 'user';
    const { data: profile } = await supabase
      .from('profiles')
      .select('role')
      .eq('id', user.id)
      .single();

    if (profile) {
      role = profile.role;
    }

    res.status(200).json({
      success: true,
      user: {
        id: user.id,
        name: user.user_metadata?.name || 'User',
        email: user.email,
        role: role
      }
    });
  } catch (error) {
    console.error('Get session error:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// 4. Logout Route
app.post('/api/auth/logout', async (req, res) => {
  try {
    const token = req.cookies.token;
    if (token) {
      // Sign out from Supabase auth
      const tempClient = createClient(supabaseUrl || 'https://placeholder.supabase.co', supabaseAnonKey || 'placeholder', {
        auth: {
          persistSession: false
        }
      });
      await tempClient.auth.signOut(token);
    }
  } catch (err) {
    // Ignore Supabase sign out error on logout
  }

  res.clearCookie('token');
  res.status(200).json({ success: true, message: 'Logged out successfully.' });
});

// 5. Google OAuth Login Route
app.get('/api/auth/google', async (req, res) => {
  try {
    const redirectUrl = `${req.protocol}://${req.get('host')}/api/auth/callback`;
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: {
        redirectTo: redirectUrl
      }
    });

    if (error) {
      return res.status(400).send(`Google Login failed: ${error.message}`);
    }

    res.redirect(data.url);
  } catch (error) {
    console.error('Google OAuth redirect error:', error);
    res.status(500).send('Internal server error.');
  }
});

// 6. OAuth Callback Route
app.get('/api/auth/callback', async (req, res) => {
  try {
    const code = req.query.code;
    
    if (!code) {
      return res.redirect('/?error=No authentication code found');
    }

    // Exchange the code for a session
    const { data, error } = await supabase.auth.exchangeCodeForSession(code);

    if (error || !data.session) {
      console.error('Code exchange error:', error);
      return res.redirect(`/?error=${encodeURIComponent(error?.message || 'Authentication failed')}`);
    }

    // Set cookie with token
    res.cookie('token', data.session.access_token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'strict',
      maxAge: 7 * 24 * 60 * 60 * 1000, // 7 days
    });

    res.redirect('/');
  } catch (error) {
    console.error('Callback error:', error);
    res.redirect('/?error=internal_server_error');
  }
});

// Start the Server
app.listen(PORT, () => {
  console.log(`===================================================`);
  console.log(` Iconic Hypercars server running on port ${PORT} `);
  console.log(` URL: http://localhost:${PORT}                       `);
  console.log(`===================================================`);
});
