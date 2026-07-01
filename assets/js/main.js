document.addEventListener('DOMContentLoaded', () => {
  // --- Reusable Swipe Gesture Helper ---
  function enableTouchSwipe(trackElement, onSwipeLeft, onSwipeRight) {
    if (!trackElement) return;
    let startX = 0, startY = 0, diffX = 0, diffY = 0, isHorizontalSwipe = false;

    trackElement.addEventListener('touchstart', (e) => {
      startX = e.touches[0].clientX;
      startY = e.touches[0].clientY;
      diffX = 0;
      diffY = 0;
      isHorizontalSwipe = false;
    }, { passive: true });

    trackElement.addEventListener('touchmove', (e) => {
      if (!startX || !startY) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      diffX = startX - currentX;
      diffY = startY - currentY;

      if (!isHorizontalSwipe && Math.abs(diffX) > 5 && Math.abs(diffX) > Math.abs(diffY)) {
        isHorizontalSwipe = true;
      }

      if (isHorizontalSwipe) {
        if (e.cancelable) e.preventDefault();
      }
    }, { passive: false });

    trackElement.addEventListener('touchend', () => {
      if (isHorizontalSwipe && Math.abs(diffX) > 50) {
        if (diffX > 0) {
          onSwipeLeft();
        } else {
          onSwipeRight();
        }
      }
      startX = 0;
      startY = 0;
      diffX = 0;
      diffY = 0;
      isHorizontalSwipe = false;
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
    authLoginTab.addEventListener('click', () => {
      authLoginTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authSignupTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authLoginForm.classList.remove('hidden');
      authSignupForm.classList.add('hidden');
    });

    authSignupTab.addEventListener('click', () => {
      authSignupTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authLoginTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      authSignupForm.classList.remove('hidden');
      authLoginForm.classList.add('hidden');
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
        const response = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok && data.success) {
          showFormMessage(authLoginForm, 'success', 'Login successful! Welcome back.');
          renderLoggedInView(data.user);

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
        const response = await fetch('/api/auth/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, password }),
        });

        const data = await response.json();

        if (response.ok && data.success) {
          showFormMessage(authSignupForm, 'success', 'Account created! Welcome to Iconic.');
          renderLoggedInView(data.user);

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
        const response = await fetch('/api/auth/logout', { method: 'POST' });
        if (response.ok) {
          renderLoggedOutView();
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
        window.location.href = '/api/auth/google';
      });
    }

    // Initial auth status check
    async function checkAuthStatus() {
      try {
        const response = await fetch('/api/auth/me');
        const data = await response.json();
        if (response.ok && data.success) {
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

  // --- Place an Ad bottom drawer and auto-save ---
  function initializePlaceAdDrawer() {
    const placeAdButtons = document.querySelectorAll('[aria-label="Place an ad"]');
    if (placeAdButtons.length === 0) return;

    const profilePopover = document.getElementById('profile-popover');

    // 1. Inject Drawer & Backdrop if not already present
    if (!document.getElementById('ad-drawer')) {
      const backdrop = document.createElement('div');
      backdrop.id = 'ad-drawer-backdrop';
      document.body.appendChild(backdrop);

      const drawer = document.createElement('div');
      drawer.id = 'ad-drawer';
      drawer.innerHTML = `
        <div class="flex items-center justify-between border-b border-black/[0.08] dark:border-white/[0.08] px-6 py-4 shrink-0">
          <h3 class="text-sm font-logo font-extrabold uppercase tracking-widest text-zinc-900 dark:text-white">Place Your Listing</h3>
          <button id="ad-drawer-close-btn" class="text-zinc-400 hover:text-zinc-900 dark:hover:text-white transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <form id="ad-drawer-form" class="flex-1 overflow-y-auto p-6 flex flex-col gap-4 text-left">
          <div id="ad-form-message" class="hidden text-xs font-semibold p-2.5 rounded-lg text-center"></div>

          <div class="grid grid-cols-2 gap-3.5">
            <div class="flex flex-col gap-1">
              <label for="ad-brand" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Brand</label>
              <select id="ad-brand" required class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white focus:outline-none focus:border-brand">
                <option value="" disabled selected>Select Brand</option>
                <option value="Bugatti">Bugatti</option>
                <option value="Koenigsegg">Koenigsegg</option>
                <option value="Pagani">Pagani</option>
                <option value="Ferrari">Ferrari</option>
                <option value="Lamborghini">Lamborghini</option>
                <option value="Mercedes-Benz">Mercedes-Benz</option>
                <option value="McLaren">McLaren</option>
                <option value="Porsche">Porsche</option>
                <option value="Aston Martin">Aston Martin</option>
              </select>
            </div>
            <div class="flex flex-col gap-1">
              <label for="ad-model" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Model</label>
              <input type="text" id="ad-model" required placeholder="e.g. Chiron Super Sport" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3.5">
            <div class="flex flex-col gap-1">
              <label for="ad-year" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Year</label>
              <input type="number" id="ad-year" required min="1900" max="2027" placeholder="e.g. 2024" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="ad-price" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Price (e.g. AED 38,500,000)</label>
              <input type="text" id="ad-price" required placeholder="e.g. AED 38,500,000" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3.5">
            <div class="flex flex-col gap-1">
              <label for="ad-mileage" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Mileage (e.g. 1,200 km)</label>
              <input type="text" id="ad-mileage" required placeholder="e.g. 1,200 km" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="ad-specs" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Regional Specs</label>
              <select id="ad-specs" required class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white focus:outline-none focus:border-brand">
                <option value="" disabled selected>Select Specs</option>
                <option value="GCC Specs">GCC Specs</option>
                <option value="European Specs">European Specs</option>
                <option value="USA Specs">USA Specs</option>
                <option value="Other">Other Specs</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3.5">
            <div class="flex flex-col gap-1">
              <label for="ad-exterior-color" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Exterior Color</label>
              <input type="text" id="ad-exterior-color" required placeholder="e.g. Atlantic Blue" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="ad-interior-color" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Interior Color</label>
              <input type="text" id="ad-interior-color" required placeholder="e.g. Black Alcantara" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
          </div>

          <div class="grid grid-cols-2 gap-3.5">
            <div class="flex flex-col gap-1">
              <label for="ad-engine" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Engine Specs</label>
              <input type="text" id="ad-engine" placeholder="e.g. 8.0L W16 Quad-Turbo" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
            <div class="flex flex-col gap-1">
              <label for="ad-transmission" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Transmission</label>
              <input type="text" id="ad-transmission" placeholder="e.g. 7-Speed DSG" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
            </div>
          </div>

          <div class="flex flex-col gap-1">
            <label for="ad-location" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Location (City, Country)</label>
            <input type="text" id="ad-location" required placeholder="e.g. Sheikh Zayed Road, Dubai" class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand" />
          </div>

          <div class="flex flex-col gap-1">
            <label for="ad-description" class="text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500">Vehicle Description</label>
            <textarea id="ad-description" rows="3" placeholder="Pristine condition, single owner, full manufacturer warranty..." class="w-full text-xs px-3 py-2.5 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 text-zinc-900 dark:text-white placeholder-zinc-400 focus:outline-none focus:border-brand resize-none"></textarea>
          </div>

          <div class="pt-3 mt-2 shrink-0 border-t border-black/[0.05] dark:border-white/[0.05]">
            <button type="submit" class="w-full bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-3 rounded-lg active:scale-[0.98] transition-all duration-200 shadow-md">
              Submit Listing for Verification
            </button>
          </div>
        </form>
      `;
      document.body.appendChild(drawer);
    }

    const drawer = document.getElementById('ad-drawer');
    const backdrop = document.getElementById('ad-drawer-backdrop');
    const closeBtn = document.getElementById('ad-drawer-close-btn');
    const form = document.getElementById('ad-drawer-form');
    const formMsg = document.getElementById('ad-form-message');

    if (!drawer || !backdrop || !closeBtn || !form || !formMsg) return;

    // Helper: Close Drawer
    function closeDrawer() {
      drawer.classList.remove('active');
      backdrop.classList.remove('active');
      document.body.style.overflow = '';
    }

    // Helper: Open Drawer
    function openDrawer() {
      drawer.classList.add('active');
      backdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
      loadDraft();
    }

    // Click Handlers to Close
    closeBtn.addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', closeDrawer);

    // Attach click event to all "Place an ad" buttons
    placeAdButtons.forEach(btn => {
      btn.addEventListener('click', async (e) => {
        e.preventDefault();
        
        // Enforce user authentication
        try {
          const res = await fetch('/api/auth/me');
          const data = await res.json();
          
          if (res.ok && data.success) {
            openDrawer();
          } else {
            promptLogin();
          }
        } catch (err) {
          promptLogin();
        }
      });
    });

    function promptLogin() {
      if (profilePopover) {
        if (typeof profilePopover.showPopover === 'function') {
          profilePopover.showPopover();
        }
        
        // Show login warning
        const loginForm = document.getElementById('auth-login-form');
        if (loginForm) {
          let msgContainer = loginForm.querySelector('.auth-msg-container');
          if (!msgContainer) {
            msgContainer = document.createElement('div');
            loginForm.insertBefore(msgContainer, loginForm.firstChild);
          }
          msgContainer.textContent = 'Please sign in to place an ad.';
          msgContainer.classList.remove('hidden');
          msgContainer.className = 'auth-msg-container text-xs font-semibold p-2.5 rounded-lg text-center mb-2.5 bg-brand/10 border border-brand/20 text-brand';
        }
      }
    }

    // LocalStorage Draft Auto-Save
    const fields = [
      'ad-brand', 'ad-model', 'ad-year', 'ad-price', 'ad-mileage', 'ad-specs',
      'ad-exterior-color', 'ad-interior-color', 'ad-engine', 'ad-transmission',
      'ad-location', 'ad-description'
    ];

    function saveDraft() {
      const draft = {};
      fields.forEach(id => {
        const input = document.getElementById(id);
        if (input) {
          draft[id] = input.value;
        }
      });
      localStorage.setItem('iconic_ad_draft', JSON.stringify(draft));
    }

    function loadDraft() {
      try {
        const saved = localStorage.getItem('iconic_ad_draft');
        if (!saved) return;
        const draft = JSON.parse(saved);
        fields.forEach(id => {
          const input = document.getElementById(id);
          if (input && draft[id] !== undefined) {
            input.value = draft[id];
          }
        });
      } catch (err) {
        console.error('Error loading draft:', err);
      }
    }

    function clearDraft() {
      localStorage.removeItem('iconic_ad_draft');
      form.reset();
    }

    // Auto-save on any input events
    form.addEventListener('input', saveDraft);
    form.addEventListener('change', saveDraft);

    // Form Submit Handler
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      formMsg.classList.add('hidden');
      formMsg.textContent = '';

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.disabled = true;
      submitBtn.textContent = 'SUBMITTING LISTING...';

      const payload = {
        brand: document.getElementById('ad-brand').value,
        model: document.getElementById('ad-model').value,
        year: document.getElementById('ad-year').value,
        price: document.getElementById('ad-price').value,
        mileage: document.getElementById('ad-mileage').value,
        specs: document.getElementById('ad-specs').value,
        exterior_color: document.getElementById('ad-exterior-color').value,
        interior_color: document.getElementById('ad-interior-color').value,
        engine: document.getElementById('ad-engine').value,
        transmission: document.getElementById('ad-transmission').value,
        location: document.getElementById('ad-location').value,
        description: document.getElementById('ad-description').value
      };

      try {
        const response = await fetch('/api/listings', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok && data.success) {
          formMsg.textContent = 'Listing submitted successfully! Admin will verify it shortly.';
          formMsg.className = 'text-xs font-semibold p-2.5 rounded-lg text-center mb-4 bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/30 text-emerald-600 dark:text-emerald-400';
          formMsg.classList.remove('hidden');

          clearDraft();

          setTimeout(() => {
            closeDrawer();
            formMsg.classList.add('hidden');
          }, 2500);
        } else {
          formMsg.textContent = data.error || 'Failed to submit listing.';
          formMsg.className = 'text-xs font-semibold p-2.5 rounded-lg text-center mb-4 bg-brand/10 border border-brand/20 text-brand';
          formMsg.classList.remove('hidden');
        }
      } catch (err) {
        formMsg.textContent = 'Network error. Please try again.';
        formMsg.className = 'text-xs font-semibold p-2.5 rounded-lg text-center mb-4 bg-brand/10 border border-brand/20 text-brand';
        formMsg.classList.remove('hidden');
        console.error('Listings post error:', err);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
      }
    });
  }

  // Initialize
  initializePlaceAdDrawer();
});
