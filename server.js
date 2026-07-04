const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const multer = require('multer');
const { createClient } = require('@supabase/supabase-js');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(express.json());
app.use(cookieParser());

// Enable CORS for cross-origin local testing (like VS Code Live Server & LAN Mobile devices)
app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (origin && (origin.includes('localhost') || origin.includes('127.0.0.1') || origin.includes('192.168.'))) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});

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
      token: data.session ? data.session.access_token : null,
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
      token: data.session.access_token,
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
    const token = req.cookies.token || (req.headers.authorization && req.headers.authorization.split(' ')[1]);
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
      token, // Return token back to client so they can save it in localStorage
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
    const referer = req.headers.referer;
    if (referer) {
      res.cookie('oauth_redirect_origin', referer, {
        httpOnly: true,
        maxAge: 10 * 60 * 1000, // 10 minutes
      });
    }

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

    // Get origin to redirect back to
    const redirectOrigin = req.cookies.oauth_redirect_origin || `${req.protocol}://${req.get('host')}/`;
    res.clearCookie('oauth_redirect_origin');

    // Parse URL and append token parameter safely
    const targetUrl = new URL(redirectOrigin);
    targetUrl.searchParams.set('token', data.session.access_token);

    res.redirect(targetUrl.toString());
  } catch (error) {
    console.error('Callback error:', error);
    res.redirect('/?error=internal_server_error');
  }
});

// Configure Multer for Memory Storage
const upload = multer({
  storage: multer.memoryStorage(),
  limits: {
    fileSize: 10 * 1024 * 1024 // Limit to 10MB per file
  }
});

// 6b. Image Upload Endpoint
app.post('/api/upload', upload.array('photos', 20), async (req, res) => {
  try {
    const token = req.cookies.token || (req.headers.authorization && req.headers.authorization.split(' ')[1]);
    if (!token) {
      return res.status(401).json({ error: 'Please sign in to upload images.' });
    }

    const { data: { user }, error: authError } = await supabase.auth.getUser(token);
    if (authError || !user) {
      return res.status(401).json({ error: 'Please sign in to upload images.' });
    }

    if (!req.files || req.files.length === 0) {
      return res.status(400).json({ error: 'No files uploaded.' });
    }

    const uploadPromises = req.files.map(async (file) => {
      const fileExt = file.originalname.split('.').pop();
      const fileName = `${user.id}/${Date.now()}-${Math.floor(Math.random() * 1000000)}.${fileExt}`;
      const filePath = fileName;

      // Upload file to Supabase Storage bucket 'car-images'
      const { data, error } = await supabase.storage
        .from('car-images')
        .upload(filePath, file.buffer, {
          contentType: file.mimetype,
          upsert: true
        });

      if (error) {
        if (error.message && error.message.includes('Bucket not found')) {
          throw new Error("Supabase Storage bucket 'car-images' not found. Please create the bucket named 'car-images' (and make it Public) in your Supabase dashboard.");
        }
        throw error;
      }

      // Get public URL
      const { data: { publicUrl } } = supabase.storage
        .from('car-images')
        .getPublicUrl(filePath);

      return publicUrl;
    });

    const urls = await Promise.all(uploadPromises);
    res.status(200).json({ success: true, urls });
  } catch (error) {
    console.error('File upload error:', error);
    res.status(500).json({ error: error.message || 'Failed to upload images.' });
  }
});

// 7. Place an Ad / Create Listing Endpoint
app.post('/api/listings', async (req, res) => {
  try {
    const token = req.cookies.token || (req.headers.authorization && req.headers.authorization.split(' ')[1]);
    if (!token) {
      return res.status(401).json({ error: 'Please sign in to submit a listing.' });
    }

    // Verify token with Supabase Auth
    const { data: { user }, error } = await supabase.auth.getUser(token);
    if (error || !user) {
      return res.status(401).json({ error: 'Please sign in to submit a listing.' });
    }

    const {
      brand, model, trim, year, price, mileage, specs, body_type,
      exterior_color, interior_color, horsepower, engine, transmission,
      steering, top_speed, torque, location, description, phone_number, photos
    } = req.body;

    // Basic Validations for Required Step 1 Fields
    if (!brand || !model || !trim || !year || !price || !mileage || !specs || !body_type || !location || !phone_number) {
      return res.status(400).json({ error: 'Missing required vehicle information.' });
    }

    // Insert into Supabase listings table
    const { data: listing, error: insertError } = await supabase
      .from('listings')
      .insert([{
        brand,
        model,
        trim,
        year: parseInt(year),
        price,
        mileage,
        specs,
        body_type,
        exterior_color: exterior_color || 'N/A',
        interior_color: interior_color || 'N/A',
        horsepower: horsepower || 'N/A',
        engine: engine || 'N/A',
        transmission: transmission || 'N/A',
        steering: steering || 'N/A',
        top_speed: top_speed || 'N/A',
        torque: torque || 'N/A',
        location,
        description: description || '',
        phone_number,
        photos: Array.isArray(photos) ? photos : [],
        user_id: user.id,
        status: 'pending' // default pending state
      }])
      .select()
      .single();

    if (insertError) {
      console.error('Database insert error:', insertError);
      return res.status(400).json({ error: insertError.message });
    }

    res.status(201).json({
      success: true,
      message: 'Listing submitted for verification successfully!',
      listing
    });
  } catch (error) {
    console.error('Listings post error:', error);
    res.status(500).json({ error: 'Internal server error.' });
// 8. Get Approved Listings Endpoint
app.get('/api/listings', async (req, res) => {
  try {
    const { data: listings, error } = await supabase
      .from('listings')
      .select('*')
      .eq('status', 'approved')
      .order('created_at', { ascending: false });

    if (error) {
      console.error('Fetch listings database error:', error);
      return res.status(400).json({ error: error.message });
    }

    res.status(200).json({ success: true, listings });
  } catch (error) {
    console.error('Fetch listings endpoint error:', error);
    res.status(500).json({ error: 'Internal server error.' });
  }
});

// Start the Server
app.listen(PORT, () => {
  console.log(`===================================================`);
  console.log(` Iconic Hypercars server running on port ${PORT} `);
  console.log(` URL: http://localhost:${PORT}                       `);
  console.log(`===================================================`);
});
