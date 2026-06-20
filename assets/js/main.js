document.addEventListener('DOMContentLoaded', () => {
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
    }, 3000);
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
    let soldStartX = 0;
    let soldStartY = 0;
    let soldHasSwiped = false;

    soldTrack.addEventListener('touchstart', (e) => {
      soldStartX = e.touches[0].clientX;
      soldStartY = e.touches[0].clientY;
      soldHasSwiped = false;
    }, { passive: true });

    soldTrack.addEventListener('touchmove', (e) => {
      if (soldHasSwiped || !soldStartX) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = soldStartX - currentX;
      const diffY = soldStartY - currentY;

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (e.cancelable) e.preventDefault();
        const swipeThreshold = 50;
        if (Math.abs(diffX) > swipeThreshold) {
          soldHasSwiped = true;
          if (diffX > 0) {
            soldCurrentSlide = (soldCurrentSlide + 1) % soldTotalSlides;
          } else {
            soldCurrentSlide = (soldCurrentSlide - 1 + soldTotalSlides) % soldTotalSlides;
          }
          updateSoldSlider();
          resetSoldAutoSlide();
          soldStartX = 0;
          soldStartY = 0;
        }
      }
    }, { passive: false });

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
    }, 3000);
  }

  function resetFeatAutoSlide() {
    clearInterval(featInterval);
    startFeatAutoSlide();
  }

  if (featTrack) {
    // Touch Swipe Support
    let featStartX = 0;
    let featStartY = 0;
    let featHasSwiped = false;

    featTrack.addEventListener('touchstart', (e) => {
      featStartX = e.touches[0].clientX;
      featStartY = e.touches[0].clientY;
      featHasSwiped = false;
    }, { passive: true });

    featTrack.addEventListener('touchmove', (e) => {
      if (featHasSwiped || !featStartX) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = featStartX - currentX;
      const diffY = featStartY - currentY;

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (e.cancelable) e.preventDefault();
        const swipeThreshold = 50;
        if (Math.abs(diffX) > swipeThreshold) {
          featHasSwiped = true;
          const maxSlide = getFeatMaxSlide();
          if (diffX > 0) {
            featCurrentSlide = (featCurrentSlide + 1) > maxSlide ? 0 : featCurrentSlide + 1;
          } else {
            featCurrentSlide = (featCurrentSlide - 1) < 0 ? maxSlide : featCurrentSlide - 1;
          }
          updateFeatSlider();
          resetFeatAutoSlide();
          featStartX = 0;
          featStartY = 0;
        }
      }
    }, { passive: false });

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
    }, 3050);
  }

  function resetTestimonialAutoSlide() {
    clearInterval(testimonialInterval);
    startTestimonialAutoSlide();
  }

  if (testimonialTrack) {
    // Touch Swipe Support
    let testimonialStartX = 0;
    let testimonialStartY = 0;
    let testimonialHasSwiped = false;

    testimonialTrack.addEventListener('touchstart', (e) => {
      testimonialStartX = e.touches[0].clientX;
      testimonialStartY = e.touches[0].clientY;
      testimonialHasSwiped = false;
    }, { passive: true });

    testimonialTrack.addEventListener('touchmove', (e) => {
      if (!isMobile()) return;
      if (testimonialHasSwiped || !testimonialStartX) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = testimonialStartX - currentX;
      const diffY = testimonialStartY - currentY;

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (e.cancelable) e.preventDefault();
        const swipeThreshold = 50;
        if (Math.abs(diffX) > swipeThreshold) {
          testimonialHasSwiped = true;
          const maxSlide = getTestimonialMaxSlide();
          if (diffX > 0) {
            testimonialCurrentSlide = (testimonialCurrentSlide + 1) > maxSlide ? 0 : testimonialCurrentSlide + 1;
          } else {
            testimonialCurrentSlide = (testimonialCurrentSlide - 1) < 0 ? maxSlide : testimonialCurrentSlide - 1;
          }
          updateTestimonialSlider();
          resetTestimonialAutoSlide();
          testimonialStartX = 0;
          testimonialStartY = 0;
        }
      }
    }, { passive: false });

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

  // --- Auth Tabs Toggle Logic ---
  const authLoginTab = document.getElementById('auth-login-tab');
  const authSignupTab = document.getElementById('auth-signup-tab');
  const authLoginForm = document.getElementById('auth-login-form');
  const authSignupForm = document.getElementById('auth-signup-form');

  if (authLoginTab && authSignupTab && authLoginForm && authSignupForm) {
    authLoginTab.addEventListener('click', () => {
      // Toggle tabs styling
      authLoginTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      
      authSignupTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      
      // Toggle form visibility
      authLoginForm.classList.remove('hidden');
      authSignupForm.classList.add('hidden');
    });

    authSignupTab.addEventListener('click', () => {
      // Toggle tabs styling
      authSignupTab.classList.add('text-brand', 'border-b-2', 'border-brand');
      authSignupTab.classList.remove('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      
      authLoginTab.classList.remove('text-brand', 'border-b-2', 'border-brand');
      authLoginTab.classList.add('text-zinc-400', 'dark:text-zinc-500', 'hover:text-zinc-900', 'dark:hover:text-white');
      
      // Toggle form visibility
      authSignupForm.classList.remove('hidden');
      authLoginForm.classList.add('hidden');
    });
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
    let newsStartX = 0;
    let newsStartY = 0;
    let newsHasSwiped = false;

    newsTrack.addEventListener('touchstart', (e) => {
      newsStartX = e.touches[0].clientX;
      newsStartY = e.touches[0].clientY;
      newsHasSwiped = false;
    }, { passive: true });

    newsTrack.addEventListener('touchmove', (e) => {
      if (newsHasSwiped || !newsStartX) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = newsStartX - currentX;
      const diffY = newsStartY - currentY;

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (e.cancelable) e.preventDefault();
        const swipeThreshold = 50;
        if (Math.abs(diffX) > swipeThreshold) {
          newsHasSwiped = true;
          if (diffX > 0) {
            newsCurrentSlide = newsCurrentSlide + 1;
          } else {
            newsCurrentSlide = newsCurrentSlide - 1;
          }
          updateNewsSlider();
        }
      }
    }, { passive: false });

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
    let reviewsStartX = 0;
    let reviewsStartY = 0;
    let reviewsHasSwiped = false;

    reviewsTrack.addEventListener('touchstart', (e) => {
      reviewsStartX = e.touches[0].clientX;
      reviewsStartY = e.touches[0].clientY;
      reviewsHasSwiped = false;
    }, { passive: true });

    reviewsTrack.addEventListener('touchmove', (e) => {
      if (reviewsHasSwiped || !reviewsStartX) return;
      const currentX = e.touches[0].clientX;
      const currentY = e.touches[0].clientY;
      const diffX = reviewsStartX - currentX;
      const diffY = reviewsStartY - currentY;

      if (Math.abs(diffX) > Math.abs(diffY)) {
        if (e.cancelable) e.preventDefault();
        const swipeThreshold = 50;
        if (Math.abs(diffX) > swipeThreshold) {
          reviewsHasSwiped = true;
          if (diffX > 0) {
            reviewsCurrentSlide = reviewsCurrentSlide + 1;
          } else {
            reviewsCurrentSlide = reviewsCurrentSlide - 1;
          }
          updateReviewsSlider();
        }
      }
    }, { passive: false });

    window.addEventListener('resize', updateReviewsSlider);
  }
});
