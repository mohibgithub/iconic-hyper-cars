document.addEventListener('DOMContentLoaded', () => {
  // Global auth state tracker
  window.isAuthenticated = false;

  // Check if token is in URL (e.g., after OAuth redirect)
  const urlParams = new URLSearchParams(window.location.search);
  const urlToken = urlParams.get('token');
  if (urlToken) {
    localStorage.setItem('iconic_auth_token', urlToken);
    // Clean up URL
    urlParams.delete('token');
    const newSearch = urlParams.toString();
    const newUrl = window.location.pathname + (newSearch ? '?' + newSearch : '') + window.location.hash;
    window.history.replaceState({}, document.title, newUrl);
  }

  // --- Reusable API URL Helper for multi-port testing ---
  function getApiUrl(path) {
    const isLocalhost = window.location.hostname === 'localhost' || 
                        window.location.hostname === '127.0.0.1' || 
                        window.location.hostname.startsWith('192.168.') ||
                        window.location.hostname === '';
    const isFileProtocol = window.location.protocol === 'file:';

    // If it's a live production site (not local), use relative path directly
    if (!isLocalhost && !isFileProtocol) {
      return path;
    }

    // If we're already on the server port 3000, use relative path directly
    if (window.location.port === '3000') {
      return path;
    }

    // For local development on other ports (e.g. 5500) or file:/// protocol, redirect to local port 3000
    const protocol = isFileProtocol ? 'http:' : window.location.protocol;
    const hostname = window.location.hostname === '' ? 'localhost' : window.location.hostname;
    return `${protocol}//${hostname}:3000${path}`;
  }

  // --- Reusable Authenticated Fetch Wrapper ---
  async function authenticatedFetch(path, options = {}) {
    const url = getApiUrl(path);
    const token = localStorage.getItem('iconic_auth_token');
    if (!options.headers) {
      options.headers = {};
    }
    if (token) {
      options.headers['Authorization'] = `Bearer ${token}`;
    }
    options.credentials = 'include';
    return fetch(url, options);
  }

  // --- Reusable Swipe Gesture Helper ---
  function enableTouchSwipe(trackElement, onSwipeLeft, onSwipeRight) {
    if (!trackElement) return;
    let startX = 0;
    let startY = 0;
    let endX = 0;
    let endY = 0;

    trackElement.addEventListener('touchstart', (e) => {
      startX = e.touches[0].screenX;
      startY = e.touches[0].screenY;
      endX = startX;
      endY = startY;
    }, { passive: true });

    trackElement.addEventListener('touchmove', (e) => {
      endX = e.touches[0].screenX;
      endY = e.touches[0].screenY;
    }, { passive: true });

    trackElement.addEventListener('touchend', () => {
      const diffX = startX - endX;
      const diffY = startY - endY;

      // Swipe threshold of 50px, and horizontal angle check
      if (Math.abs(diffX) > 50 && Math.abs(diffX) > Math.abs(diffY)) {
        if (diffX > 0) {
          onSwipeLeft(); // Swiped left (show next)
        } else {
          onSwipeRight(); // Swiped right (show prev)
        }
      }
      startX = 0;
      startY = 0;
      endX = 0;
      endY = 0;
    });
  }

  // --- Theme Toggle Logic ---
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const sunIcon = document.getElementById('sun-icon');
  const moonIcon = document.getElementById('moon-icon');

  // Set initial theme based on localStorage or user preferences
  if (
    localStorage.getItem('color-theme') === 'dark' ||
    (!('color-theme' in localStorage) &&
      window.matchMedia('(prefers-color-scheme: dark)').matches)
  ) {
    document.documentElement.classList.add('dark');
    sunIcon.classList.remove('hidden');
    moonIcon.classList.add('hidden');
  } else {
    document.documentElement.classList.remove('dark');
    sunIcon.classList.add('hidden');
    moonIcon.classList.remove('hidden');
  }

  // Toggle theme function
  themeToggleBtn.addEventListener('click', () => {
    if (document.documentElement.classList.contains('dark')) {
      document.documentElement.classList.remove('dark');
      localStorage.setItem('color-theme', 'light');
      sunIcon.classList.add('hidden');
      moonIcon.classList.remove('hidden');
    } else {
      document.documentElement.classList.add('dark');
      localStorage.setItem('color-theme', 'dark');
      sunIcon.classList.remove('hidden');
      moonIcon.classList.add('hidden');
    }
  });

  // --- Search Bar Focus Handler ---
  const searchPopover = document.getElementById('search-popover');
  const searchInput = document.getElementById('search-input');

  if (searchPopover && searchInput) {
    searchPopover.addEventListener('toggle', (event) => {
      if (event.newState === 'open') {
        // Focus the search input with a slight delay to allow the entry animation to finish
        setTimeout(() => {
          searchInput.focus();
        }, 150);
      } else {
        searchInput.value = '';
      }
    });
  }

  // --- First Slider (Sold Cars) Logic ---
  const soldTrack = document.getElementById('slider-track');
  const soldPrevBtn = document.getElementById('slider-prev-btn');
  const soldNextBtn = document.getElementById('slider-next-btn');
  const soldSlides = document.querySelectorAll('.slider-slide');
  const soldTotalSlides = soldSlides.length;
  let soldCurrentSlide = 0;
  let soldInterval;

  function updateSoldSlider() {
    if (!soldTrack) return;
    soldTrack.style.transform = `translateX(-${soldCurrentSlide * 100}%)`;
  }

  function startSoldAutoSlide() {
    soldInterval = setInterval(() => {
      soldCurrentSlide = (soldCurrentSlide + 1) % soldTotalSlides;
      updateSoldSlider();
    }, 5000);
  }

  function resetSoldAutoSlide() {
    clearInterval(soldInterval);
    startSoldAutoSlide();
  }

  if (soldTrack) {
    if (soldPrevBtn && soldNextBtn) {
      soldPrevBtn.addEventListener('click', () => {
        soldCurrentSlide = (soldCurrentSlide - 1 + soldTotalSlides) % soldTotalSlides;
        updateSoldSlider();
        resetSoldAutoSlide();
      });

      soldNextBtn.addEventListener('click', () => {
        soldCurrentSlide = (soldCurrentSlide + 1) % soldTotalSlides;
        updateSoldSlider();
        resetSoldAutoSlide();
      });
    }

    // Touch Swipe Support
    enableTouchSwipe(
      soldTrack,
      () => {
        soldCurrentSlide = (soldCurrentSlide + 1) % soldTotalSlides;
        updateSoldSlider();
        resetSoldAutoSlide();
      },
      () => {
        soldCurrentSlide = (soldCurrentSlide - 1 + soldTotalSlides) % soldTotalSlides;
        updateSoldSlider();
        resetSoldAutoSlide();
      }
    );

    startSoldAutoSlide();
  }

  // --- Second Slider (Iconic Feature) Logic ---
  const featTrack = document.getElementById('featured-slider-track');
  const featSlides = document.querySelectorAll('.featured-slider-slide');
  const featTotalSlides = featSlides.length;
  let featCurrentSlide = 0;
  let featInterval;

  function getFeatMaxSlide() {
    return featTotalSlides - 2; // Always 4 because we show 2 slides on all viewports (mobile & desktop)
  }

  function updateFeatSlider() {
    if (!featTrack) return;
    const stepSize = 50; // Always 50% width since we show 2 slides on all viewports
    
    // Boundary check
    const maxSlide = getFeatMaxSlide();
    if (featCurrentSlide > maxSlide) {
      featCurrentSlide = 0;
    } else if (featCurrentSlide < 0) {
      featCurrentSlide = maxSlide;
    }
    
    featTrack.style.transform = `translateX(-${featCurrentSlide * stepSize}%)`;
  }

  function startFeatAutoSlide() {
    featInterval = setInterval(() => {
      const maxSlide = getFeatMaxSlide();
      featCurrentSlide = (featCurrentSlide + 1) > maxSlide ? 0 : featCurrentSlide + 1;
      updateFeatSlider();
    }, 5000);
  }

  function resetFeatAutoSlide() {
    clearInterval(featInterval);
    startFeatAutoSlide();
  }

  if (featTrack) {
    // Touch Swipe Support
    enableTouchSwipe(
      featTrack,
      () => {
        const maxSlide = getFeatMaxSlide();
        featCurrentSlide = (featCurrentSlide + 1) > maxSlide ? 0 : featCurrentSlide + 1;
        updateFeatSlider();
        resetFeatAutoSlide();
      },
      () => {
        const maxSlide = getFeatMaxSlide();
        featCurrentSlide = (featCurrentSlide - 1) < 0 ? maxSlide : featCurrentSlide - 1;
        updateFeatSlider();
        resetFeatAutoSlide();
      }
    );

    // Handle screen resize
    window.addEventListener('resize', () => {
      updateFeatSlider();
    });

    startFeatAutoSlide();
  }

  // --- Third Slider (Testimonials) Logic ---
  const testimonialTrack = document.getElementById('testimonials-slider-track');
  const testimonialSlides = document.querySelectorAll('.testimonials-slide');
  const testimonialTotalSlides = testimonialSlides.length;
  let testimonialCurrentSlide = 0;
  let testimonialInterval;

  function isMobile() {
    return window.innerWidth < 768;
  }

  function getTestimonialMaxSlide() {
    return testimonialTotalSlides - 1; // 1 slide at a time, max index is 2 (3 slides total)
  }

  function updateTestimonialSlider() {
    if (!testimonialTrack) return;
    if (isMobile()) {
      const stepSize = 100; // Each slide is 100% width
      const maxSlide = getTestimonialMaxSlide();
      
      // Boundary check
      if (testimonialCurrentSlide > maxSlide) {
        testimonialCurrentSlide = 0;
      } else if (testimonialCurrentSlide < 0) {
        testimonialCurrentSlide = maxSlide;
      }
      
      testimonialTrack.style.transform = `translateX(-${testimonialCurrentSlide * stepSize}%)`;
    } else {
      testimonialTrack.style.transform = '';
    }
  }

  function startTestimonialAutoSlide() {
    if (!isMobile()) return;
    testimonialInterval = setInterval(() => {
      const maxSlide = getTestimonialMaxSlide();
      testimonialCurrentSlide = (testimonialCurrentSlide + 1) > maxSlide ? 0 : testimonialCurrentSlide + 1;
      updateTestimonialSlider();
    }, 5000);
  }

  function resetTestimonialAutoSlide() {
    clearInterval(testimonialInterval);
    startTestimonialAutoSlide();
  }

  if (testimonialTrack) {
    // Touch Swipe Support
    enableTouchSwipe(
      testimonialTrack,
      () => {
        if (!isMobile()) return;
        const maxSlide = getTestimonialMaxSlide();
        testimonialCurrentSlide = (testimonialCurrentSlide + 1) > maxSlide ? 0 : testimonialCurrentSlide + 1;
        updateTestimonialSlider();
        resetTestimonialAutoSlide();
      },
      () => {
        if (!isMobile()) return;
        const maxSlide = getTestimonialMaxSlide();
        testimonialCurrentSlide = (testimonialCurrentSlide - 1) < 0 ? maxSlide : testimonialCurrentSlide - 1;
        updateTestimonialSlider();
        resetTestimonialAutoSlide();
      }
    );

    // Handle screen resize
    window.addEventListener('resize', () => {
      if (!isMobile()) {
        clearInterval(testimonialInterval);
        testimonialInterval = null;
        testimonialCurrentSlide = 0;
        testimonialTrack.style.transform = '';
      } else {
        if (!testimonialInterval) {
          startTestimonialAutoSlide();
        }
        updateTestimonialSlider();
      }
    });

    // Initial load check
    if (isMobile()) {
      startTestimonialAutoSlide();
    }
  }

  // --- Auth Tabs Toggle Logic & Authentication ---
  const authLoginTab = document.getElementById('auth-login-tab');
  const authSignupTab = document.getElementById('auth-signup-tab');
  const authLoginForm = document.getElementById('auth-login-form');
  const authSignupForm = document.getElementById('auth-signup-form');
  const profilePopover = document.getElementById('profile-popover');

  if (authLoginTab && authSignupTab && authLoginForm && authSignupForm && profilePopover) {
    // 1. Setup DOM structure for logged in / logged out states
    const loggedOutContainer = document.createElement('div');
    loggedOutContainer.id = 'auth-logged-out-view';
    loggedOutContainer.className = 'flex flex-col w-full';
    
    // Move existing popover content into loggedOutContainer
    while (profilePopover.firstChild) {
      loggedOutContainer.appendChild(profilePopover.firstChild);
    }
    profilePopover.appendChild(loggedOutContainer);

    const loggedInContainer = document.createElement('div');
    loggedInContainer.id = 'auth-logged-in-view';
    loggedInContainer.className = 'flex flex-col gap-4 hidden';
    profilePopover.appendChild(loggedInContainer);

    // 2. Tab Navigation logic (toggled via loggedOutContainer)
    const tabsHeader = authLoginTab.parentElement;

    // Create and inject Forgot Password form
    const forgotForm = document.createElement('form');
    forgotForm.id = 'auth-forgot-form';
    forgotForm.className = 'flex flex-col gap-3.5 hidden text-left';
    forgotForm.innerHTML = `
      <p class="text-[11px] text-zinc-500 dark:text-zinc-400 mb-2 leading-relaxed font-semibold">
        Enter your email address and we will send you a secure link to reset your password.
      </p>
      <div class="flex flex-col gap-1">
        <label for="forgot-email" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Email Address</label>
        <input type="email" id="forgot-email" required placeholder="name@example.com"
          class="w-full text-xs px-3 py-2 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 focus:outline-none focus:border-brand transition-colors duration-200 text-zinc-900 dark:text-white placeholder-zinc-400" />
      </div>
      <button type="submit" class="w-full bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-2.5 rounded-lg active:scale-[0.98] transition-all duration-200 shadow-md">
        Send Reset Link
      </button>
      <button type="button" id="forgot-back-to-login" class="text-center text-[10px] text-zinc-400 dark:text-zinc-500 hover:text-brand font-bold transition-colors mt-1.5">
        Back to Login
      </button>
    `;
    loggedOutContainer.insertBefore(forgotForm, authSignupForm.nextSibling);

    // Create and inject Reset Password form
    const resetForm = document.createElement('form');
    resetForm.id = 'auth-reset-form';
    resetForm.className = 'flex flex-col gap-3.5 hidden text-left';
    resetForm.innerHTML = `
      <p class="text-[11px] text-zinc-500 dark:text-zinc-400 mb-2 leading-relaxed font-semibold">
        Create a new password for your account (minimum 6 characters).
      </p>
      <div class="flex flex-col gap-1">
        <label for="reset-password" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">New Password</label>
        <input type="password" id="reset-password" required placeholder="••••••••"
          class="w-full text-xs px-3 py-2 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 focus:outline-none focus:border-brand transition-colors duration-200 text-zinc-900 dark:text-white placeholder-zinc-400" />
      </div>
      <button type="submit" class="w-full bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-2.5 rounded-lg active:scale-[0.98] transition-all duration-200 shadow-md">
        Save New Password
      </button>
    `;
    loggedOutContainer.insertBefore(resetForm, forgotForm.nextSibling);

    // Hook up Forgot Password click triggers
    const forgotTriggers = authLoginForm.querySelectorAll('a');
    let forgotTriggerBtn = null;
    forgotTriggers.forEach(link => {
      if (link.textContent.trim() === 'Forgot?') {
        forgotTriggerBtn = link;
      }
    });

    if (forgotTriggerBtn) {
      forgotTriggerBtn.addEventListener('click', (e) => {
        e.preventDefault();
        clearFormMessages(authLoginForm);
        clearFormMessages(forgotForm);
        tabsHeader.classList.add('hidden');
        authLoginForm.classList.add('hidden');
        authSignupForm.classList.add('hidden');
        forgotForm.classList.remove('hidden');
      });
    }

    const backToLoginBtn = forgotForm.querySelector('#forgot-back-to-login');
    if (backToLoginBtn) {
      backToLoginBtn.addEventListener('click', () => {
        clearFormMessages(forgotForm);
        clearFormMessages(authLoginForm);
        tabsHeader.classList.remove('hidden');
        authLoginForm.classList.remove('hidden');
        authSignupForm.classList.add('hidden');
        forgotForm.classList.add('hidden');
      });
    }

    authLoginTab.addEventListener('click', () => {
      authLoginTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authSignupTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authLoginForm.classList.remove('hidden');
      authSignupForm.classList.add('hidden');
      forgotForm.classList.add('hidden');
      resetForm.classList.add('hidden');
    });

    authSignupTab.addEventListener('click', () => {
      authSignupTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authLoginTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authSignupForm.classList.remove('hidden');
      authLoginForm.classList.add('hidden');
      forgotForm.classList.add('hidden');
      resetForm.classList.add('hidden');
    });

    // Helper functions to show success/error feedback inside forms
    function showFormMessage(form, type, message) {
      let msgContainer = form.querySelector('.auth-msg-container');
      if (!msgContainer) {
        msgContainer = document.createElement('div');
        form.insertBefore(msgContainer, form.firstChild);
      }
      msgContainer.textContent = message;
      msgContainer.classList.remove('hidden');
      
      if (type === 'error') {
        msgContainer.className = 'auth-msg-container text-xs font-semibold p-2.5 rounded-lg text-center mb-2.5 bg-brand/10 border border-brand/20 text-brand';
      } else {
        msgContainer.className = 'auth-msg-container text-xs font-semibold p-2.5 rounded-lg text-center mb-2.5 bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/30 text-emerald-600 dark:text-emerald-400';
      }
    }

    function clearFormMessages(form) {
      const msgContainer = form.querySelector('.auth-msg-container');
      if (msgContainer) {
        msgContainer.classList.add('hidden');
        msgContainer.textContent = '';
      }
    }

    // Dynamic UI states rendering
    function renderLoggedInView(user) {
      window.isAuthenticated = true;
      const initials = user.name
        ? user.name.split(' ').map(n => n[0]).join('').toUpperCase().substring(0, 2)
        : 'U';

      const isAdmin = user.role === 'admin';

      loggedInContainer.innerHTML = `
        <div class="flex items-center gap-3.5 pb-4 border-b border-zinc-100 dark:border-zinc-800">
          <div class="h-11 w-11 rounded-full bg-brand/10 border border-brand/20 flex items-center justify-center text-brand font-bold text-sm tracking-wider shrink-0">
            ${initials}
          </div>
          <div class="flex flex-col min-w-0">
            <div class="flex items-center gap-1.5">
              <h3 class="font-bold text-sm text-zinc-900 dark:text-white truncate leading-tight">${user.name}</h3>
              ${isAdmin ? `<span class="text-[8px] font-extrabold tracking-wider bg-brand text-white px-1.5 py-0.5 rounded-[4px] uppercase shrink-0">ADMIN</span>` : ''}
            </div>
            <p class="text-[10px] text-zinc-400 dark:text-zinc-500 truncate mt-0.5">${user.email}</p>
          </div>
        </div>
        
        <div class="flex flex-col gap-1 py-1">
          ${isAdmin ? `
            <!-- Admin Panel Options -->
            <a href="#" class="flex items-center justify-between text-xs font-bold py-2.5 px-3 rounded-lg bg-red-50/50 dark:bg-brand/10 border border-brand/20 text-brand transition-colors">
              <span>Admin Dashboard</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 stroke-current" fill="none" viewBox="0 0 24 24" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </a>
            <a href="#" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
              <span>Manage Hypercars</span>
              <span class="text-[9px] font-bold text-zinc-400 dark:text-zinc-500">Edit Inventory</span>
            </a>
            <a href="#" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
              <span>Sourcing Enquiries</span>
              <span class="text-[9px] font-bold text-zinc-400 dark:text-zinc-500">View Requests</span>
            </a>
          ` : `
            <!-- Standard User Options -->
            <a href="#" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
              <span>VIP Dashboard</span>
              <span class="text-[9px] font-bold tracking-widest text-brand uppercase bg-brand/10 px-2 py-0.5 rounded-full">ACTIVE</span>
            </a>
            <a href="listings.html" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
              <span>My Enquiries & Sourcing</span>
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 stroke-current opacity-60" fill="none" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </a>
            <a href="#" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
              <span>Saved Hypercars</span>
              <span class="text-[9px] font-bold text-zinc-400 dark:text-zinc-500">0 Cars</span>
            </a>
          `}
          <a href="#" class="flex items-center justify-between text-xs font-semibold py-2.5 px-3 rounded-lg hover:bg-zinc-50 dark:hover:bg-zinc-900/50 text-zinc-700 dark:text-zinc-300 transition-colors">
            <span>Account Settings</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 stroke-current opacity-60" fill="none" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
            </svg>
          </a>
        </div>

        <div class="border-t border-zinc-100 dark:border-zinc-800 pt-3">
          <button id="auth-logout-btn" class="w-full flex items-center justify-center gap-2 bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-2.5 rounded-lg active:scale-[0.98] transition-all duration-200 shadow-md">
            <span>Log Out</span>
          </button>
        </div>
      `;

      loggedOutContainer.classList.add('hidden');
      loggedInContainer.classList.remove('hidden');

      // Update trigger buttons on the page to indicate authenticated state
      const profileButtons = document.querySelectorAll('[popovertarget="profile-popover"]');
      profileButtons.forEach(btn => {
        btn.classList.add('text-brand');
        btn.classList.remove('text-white', 'text-zinc-900');
        if (!btn.querySelector('.active-dot')) {
          const dot = document.createElement('span');
          dot.className = 'active-dot absolute top-0 md:top-0.5 right-0 md:right-0.5 h-2 w-2 rounded-full bg-emerald-500 border border-white dark:border-zinc-950';
          btn.classList.add('relative');
          btn.appendChild(dot);
        }
      });

      // Attach logout event
      const logoutBtn = document.getElementById('auth-logout-btn');
      if (logoutBtn) {
        logoutBtn.addEventListener('click', handleLogout);
      }
    }

    function renderLoggedOutView() {
      window.isAuthenticated = false;
      loggedInContainer.innerHTML = '';
      loggedOutContainer.classList.remove('hidden');
      loggedInContainer.classList.add('hidden');

      // Restore profile trigger buttons styling
      const profileButtons = document.querySelectorAll('[popovertarget="profile-popover"]');
      profileButtons.forEach(btn => {
        btn.classList.remove('text-brand');
        // Restore standard styling (header is transparent with white text, menu is dark)
        const isHeaderButton = btn.closest('.main-header') !== null;
        if (isHeaderButton) {
          btn.classList.add('text-white');
        } else {
          btn.classList.add('text-zinc-900');
        }
        
        const dot = btn.querySelector('.active-dot');
        if (dot) dot.remove();
      });
    }

    // Submit Logins
    authLoginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFormMessages(authLoginForm);

      const emailInput = document.getElementById('login-email');
      const passwordInput = document.getElementById('login-password');
      const submitBtn = authLoginForm.querySelector('button[type="submit"]');

      if (!emailInput || !passwordInput || !submitBtn) return;

      const email = emailInput.value;
      const password = passwordInput.value;

      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = 'SIGNING IN...';

      try {
        const response = await authenticatedFetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok && data.success) {
          if (data.token) {
            localStorage.setItem('iconic_auth_token', data.token);
          }
          showFormMessage(authLoginForm, 'success', 'Login successful! Welcome back.');
          renderLoggedInView(data.user);
          window.dispatchEvent(new Event('auth-login-success'));

          emailInput.value = '';
          passwordInput.value = '';

          setTimeout(() => {
            if (typeof profilePopover.hidePopover === 'function') {
              profilePopover.hidePopover();
            }
            clearFormMessages(authLoginForm);
          }, 1200);
        } else {
          showFormMessage(authLoginForm, 'error', data.error || 'Invalid credentials.');
        }
      } catch (err) {
        showFormMessage(authLoginForm, 'error', 'Network error. Please try again.');
        console.error('Login error:', err);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });

    // Submit Signup
    authSignupForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFormMessages(authSignupForm);

      const nameInput = document.getElementById('signup-name');
      const emailInput = document.getElementById('signup-email');
      const passwordInput = document.getElementById('signup-password');
      const submitBtn = authSignupForm.querySelector('button[type="submit"]');

      if (!nameInput || !emailInput || !passwordInput || !submitBtn) return;

      const name = nameInput.value;
      const email = emailInput.value;
      const password = passwordInput.value;

      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = 'CREATING ACCOUNT...';

      try {
        const response = await authenticatedFetch('/api/auth/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, password })
        });

        const data = await response.json();

        if (response.ok && data.success) {
          if (data.token) {
            localStorage.setItem('iconic_auth_token', data.token);
          }
          showFormMessage(authSignupForm, 'success', 'Account created! Welcome to Iconic.');
          renderLoggedInView(data.user);
          window.dispatchEvent(new Event('auth-login-success'));

          nameInput.value = '';
          emailInput.value = '';
          passwordInput.value = '';

          setTimeout(() => {
            if (typeof profilePopover.hidePopover === 'function') {
              profilePopover.hidePopover();
            }
            clearFormMessages(authSignupForm);
          }, 1200);
        } else {
          showFormMessage(authSignupForm, 'error', data.error || 'Failed to create account.');
        }
      } catch (err) {
        showFormMessage(authSignupForm, 'error', 'Network error. Please try again.');
        console.error('Signup error:', err);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });

    // Handle logout
    async function handleLogout() {
      const logoutBtn = document.getElementById('auth-logout-btn');
      if (logoutBtn) {
        logoutBtn.disabled = true;
        logoutBtn.innerHTML = '<span>Logging out...</span>';
      }

      try {
        const response = await authenticatedFetch('/api/auth/logout', { 
          method: 'POST'
        });
        localStorage.removeItem('iconic_auth_token');
        if (response.ok) {
          renderLoggedOutView();
          window.dispatchEvent(new Event('auth-logout-success'));
          setTimeout(() => {
            if (typeof profilePopover.hidePopover === 'function') {
              profilePopover.hidePopover();
            }
          }, 500);
        }
      } catch (err) {
        console.error('Logout error:', err);
      }
    }

    // Handle Google Sign Up / Login Click
    const googleAuthBtn = loggedOutContainer.querySelector('button[type="button"]');
    if (googleAuthBtn) {
      googleAuthBtn.addEventListener('click', () => {
        window.location.href = getApiUrl('/api/auth/google');
      });
    }

    // Initial auth status check
    async function checkAuthStatus() {
      try {
        const response = await authenticatedFetch('/api/auth/me');
        const data = await response.json();
        if (response.ok && data.success) {
          if (data.token) {
            localStorage.setItem('iconic_auth_token', data.token);
          }
          renderLoggedInView(data.user);
        } else {
          renderLoggedOutView();
        }
      } catch (err) {
        renderLoggedOutView();
      }
    }

    // Check status immediately
    checkAuthStatus();

    // Intercept Place an Ad button clicks
    const placeAdButtons = document.querySelectorAll('[aria-label="Place an ad"]');
    placeAdButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        const hasLocalToken = !!localStorage.getItem('iconic_auth_token');
        if (!window.isAuthenticated && !hasLocalToken) {
          e.preventDefault();
          // Open profile popover
          const profilePopover = document.getElementById('profile-popover');
          if (profilePopover && typeof profilePopover.showPopover === 'function') {
            profilePopover.showPopover();
            // Show custom alert inside popover
            const loginForm = document.getElementById('auth-login-form');
            if (loginForm) {
              showFormMessage(loginForm, 'error', 'Please sign in to place an ad.');
            }
          }
        }
      });
    });

    // 4. Submit Forgot Password Form
    forgotForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFormMessages(forgotForm);

      const emailInput = forgotForm.querySelector('#forgot-email');
      const submitBtn = forgotForm.querySelector('button[type="submit"]');
      if (!emailInput || !submitBtn) return;

      const email = emailInput.value;
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = 'SENDING LINK...';

      try {
        const response = await authenticatedFetch('/api/auth/forgot-password', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email })
        });
        const data = await response.json();

        if (response.ok && data.success) {
          showFormMessage(forgotForm, 'success', 'Password reset link sent! Check your email inbox.');
          emailInput.value = '';
        } else {
          showFormMessage(forgotForm, 'error', data.error || 'Failed to send reset link.');
        }
      } catch (err) {
        showFormMessage(forgotForm, 'error', 'Network error. Please try again.');
        console.error('Forgot password error:', err);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });

    // 5. Submit Reset Password Form
    resetForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearFormMessages(resetForm);

      const passwordInput = resetForm.querySelector('#reset-password');
      const submitBtn = resetForm.querySelector('button[type="submit"]');
      if (!passwordInput || !submitBtn) return;

      const password = passwordInput.value;
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = 'SAVING PASSWORD...';

      // Parse token from URL hash (sent on recovery redirect from Supabase)
      const hashParams = new URLSearchParams(window.location.hash.substring(1));
      let accessToken = hashParams.get('access_token');

      if (!accessToken) {
        accessToken = localStorage.getItem('iconic_auth_token') || urlParams.get('token');
      }

      if (!accessToken) {
        showFormMessage(resetForm, 'error', 'Invalid or expired session. Please request a new link.');
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
        return;
      }

      try {
        const response = await fetch(getApiUrl('/api/auth/update-password'), {
          method: 'POST',
          headers: { 
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
          },
          body: JSON.stringify({ password })
        });
        const data = await response.json();

        if (response.ok && data.success) {
          showFormMessage(resetForm, 'success', 'Password updated! Please login with your new password.');
          passwordInput.value = '';

          // Clear Hash parameters securely
          window.history.replaceState({}, document.title, window.location.pathname);

          setTimeout(() => {
            clearFormMessages(resetForm);
            tabsHeader.classList.remove('hidden');
            authLoginForm.classList.remove('hidden');
            resetForm.classList.add('hidden');
          }, 2500);
        } else {
          showFormMessage(resetForm, 'error', data.error || 'Failed to update password.');
        }
      } catch (err) {
        showFormMessage(resetForm, 'error', 'Network error. Please try again.');
        console.error('Reset password error:', err);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });

    // 6. Check URL parameters for Reset Password redirection
    const hashParams = new URLSearchParams(window.location.hash.substring(1));
    const isResetAction = urlParams.get('action') === 'reset-password' || hashParams.get('type') === 'recovery';

    if (isResetAction) {
      setTimeout(() => {
        if (profilePopover) {
          if (typeof profilePopover.showPopover === 'function') {
            profilePopover.showPopover();
          } else {
            profilePopover.style.display = 'block';
          }
          tabsHeader.classList.add('hidden');
          authLoginForm.classList.add('hidden');
          authSignupForm.classList.add('hidden');
          forgotForm.classList.add('hidden');
          resetForm.classList.remove('hidden');
        }
      }, 500); // Small timeout to ensure popover transitions correctly after render
    }
  }

  // --- Global Slider Helper ---
  function getVisibleSlides() {
    if (window.innerWidth < 768) {
      return 1;
    } else if (window.innerWidth < 1024) {
      return 2;
    } else {
      return 3;
    }
  }

  // --- News Slider Logic ---
  const newsTrack = document.getElementById('news-slider-track');
  const newsPrevBtn = document.getElementById('news-prev-btn');
  const newsNextBtn = document.getElementById('news-next-btn');
  const newsSlides = document.querySelectorAll('.news-slider-slide');
  const newsTotalSlides = newsSlides.length;
  let newsCurrentSlide = 0;

  function getNewsMaxSlide() {
    return newsTotalSlides - getVisibleSlides();
  }

  function updateNewsSlider() {
    if (!newsTrack) return;
    const visible = getVisibleSlides();
    const stepSize = 100 / visible;
    const maxSlide = getNewsMaxSlide();
    
    if (newsCurrentSlide > maxSlide) {
      newsCurrentSlide = 0;
    } else if (newsCurrentSlide < 0) {
      newsCurrentSlide = maxSlide;
    }
    
    newsTrack.style.transform = `translateX(-${newsCurrentSlide * stepSize}%)`;
  }

  if (newsTrack) {
    if (newsPrevBtn && newsNextBtn) {
      newsPrevBtn.addEventListener('click', () => {
        newsCurrentSlide = newsCurrentSlide - 1;
        updateNewsSlider();
      });

      newsNextBtn.addEventListener('click', () => {
        newsCurrentSlide = newsCurrentSlide + 1;
        updateNewsSlider();
      });
    }

    // Touch Swipe Support
    enableTouchSwipe(
      newsTrack,
      () => {
        newsCurrentSlide = newsCurrentSlide + 1;
        updateNewsSlider();
      },
      () => {
        newsCurrentSlide = newsCurrentSlide - 1;
        updateNewsSlider();
      }
    );

    window.addEventListener('resize', updateNewsSlider);
  }

  // --- Reviews Slider Logic ---
  const reviewsTrack = document.getElementById('reviews-slider-track');
  const reviewsPrevBtn = document.getElementById('reviews-prev-btn');
  const reviewsNextBtn = document.getElementById('reviews-next-btn');
  const reviewsSlides = document.querySelectorAll('.reviews-slider-slide');
  const reviewsTotalSlides = reviewsSlides.length;
  let reviewsCurrentSlide = 0;

  function getReviewsMaxSlide() {
    return reviewsTotalSlides - getVisibleSlides();
  }

  function updateReviewsSlider() {
    if (!reviewsTrack) return;
    const visible = getVisibleSlides();
    const stepSize = 100 / visible;
    const maxSlide = getReviewsMaxSlide();
    
    if (reviewsCurrentSlide > maxSlide) {
      reviewsCurrentSlide = 0;
    } else if (reviewsCurrentSlide < 0) {
      reviewsCurrentSlide = maxSlide;
    }
    
    reviewsTrack.style.transform = `translateX(-${reviewsCurrentSlide * stepSize}%)`;
  }

  if (reviewsTrack) {
    if (reviewsPrevBtn && reviewsNextBtn) {
      reviewsPrevBtn.addEventListener('click', () => {
        reviewsCurrentSlide = reviewsCurrentSlide - 1;
        updateReviewsSlider();
      });

      reviewsNextBtn.addEventListener('click', () => {
        reviewsCurrentSlide = reviewsCurrentSlide + 1;
        updateReviewsSlider();
      });
    }

    // Touch Swipe Support
    enableTouchSwipe(
      reviewsTrack,
      () => {
        reviewsCurrentSlide = reviewsCurrentSlide + 1;
        updateReviewsSlider();
      },
      () => {
        reviewsCurrentSlide = reviewsCurrentSlide - 1;
        updateReviewsSlider();
      }
    );

    window.addEventListener('resize', updateReviewsSlider);
  }

  // --- Video Autoplay Fallback for Mobile (iOS Safari / Android Chrome) ---
  const videos = document.querySelectorAll('video');
  videos.forEach(video => {
    const playPromise = video.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        const playOnInteraction = () => {
          video.play();
          document.removeEventListener('touchstart', playOnInteraction);
          document.removeEventListener('click', playOnInteraction);
        };
        document.addEventListener('touchstart', playOnInteraction, { passive: true });
        document.addEventListener('click', playOnInteraction, { passive: true });
      });
    }
  });

});
