document.addEventListener('DOMContentLoaded', () => {
  const wizardContainer = document.getElementById('sell-wizard-container');
  const lockOverlay = document.getElementById('auth-lock-overlay');
  const lockLoginBtn = document.getElementById('lock-login-btn');
  const form = document.getElementById('sell-car-form');
  const formMsg = document.getElementById('sell-form-msg');
  const btnNext = document.getElementById('btn-next-step');
  const btnBack = document.getElementById('btn-back-step');
  const step1View = document.getElementById('wizard-step-1');
  const step2View = document.getElementById('wizard-step-2');
  
  // Step indicator elements
  const stepIndicator1 = document.getElementById('step-indicator-1');
  const stepIndicator2 = document.getElementById('step-indicator-2');

  let currentStep = 1;
  const fields = [
    'sell-location', 'sell-brand', 'sell-model', 'sell-trim', 'sell-specs',
    'sell-year', 'sell-mileage', 'sell-body-type', 'sell-price', 'sell-phone',
    'sell-exterior-color', 'sell-interior-color', 'sell-engine', 'sell-transmission',
    'sell-steering', 'sell-horsepower', 'sell-top-speed', 'sell-torque',
    'sell-description', 'sell-photos'
  ];

  // --- Auth Check on Load ---
  async function checkPageAuth() {
    try {
      const res = await fetch('/api/auth/me');
      const data = await res.json();
      
      if (res.ok && data.success) {
        // Unlock Form
        lockOverlay.classList.add('hidden');
        lockOverlay.style.opacity = '0';
        lockOverlay.style.pointerEvents = 'none';
        
        wizardContainer.classList.remove('opacity-30', 'pointer-events-none');
        
        // Load Draft and restore correct step
        loadDraft();
      } else {
        // Keep Locked
        lockOverlay.classList.remove('hidden');
        lockOverlay.style.opacity = '1';
        lockOverlay.style.pointerEvents = 'auto';
        
        wizardContainer.classList.add('opacity-30', 'pointer-events-none');
      }
    } catch (err) {
      // Offline / Server error lock fallback
      lockOverlay.classList.remove('hidden');
      lockOverlay.style.opacity = '1';
      lockOverlay.style.pointerEvents = 'auto';
      wizardContainer.classList.add('opacity-30', 'pointer-events-none');
    }
  }

  if (lockLoginBtn) {
    lockLoginBtn.addEventListener('click', () => {
      const profilePopover = document.getElementById('profile-popover');
      if (profilePopover && typeof profilePopover.showPopover === 'function') {
        profilePopover.showPopover();
      }
    });
  }

  // --- Step Navigation & Validation ---
  function updateStepUI() {
    if (currentStep === 1) {
      step1View.classList.remove('hidden');
      step2View.classList.add('hidden');
      
      // Update indicators
      stepIndicator2.querySelector('.step-num').className = 'step-num w-7 h-7 bg-zinc-100 dark:bg-zinc-900 text-zinc-400 dark:text-zinc-500 border-2 border-zinc-200 dark:border-zinc-800 font-bold text-xs rounded-full flex items-center justify-center transition-all duration-200';
      stepIndicator2.querySelector('.step-title').className = 'step-title text-[9px] font-bold uppercase tracking-wider text-zinc-400 dark:text-zinc-500';
    } else {
      step1View.classList.add('hidden');
      step2View.classList.remove('hidden');
      
      // Update indicators
      stepIndicator2.querySelector('.step-num').className = 'step-num w-7 h-7 bg-brand text-white border-2 border-brand font-bold text-xs rounded-full flex items-center justify-center transition-all duration-200';
      stepIndicator2.querySelector('.step-title').className = 'step-title text-[9px] font-bold uppercase tracking-wider text-zinc-800 dark:text-zinc-200';
    }
  }

  function validateStep1() {
    // Validate required fields of step 1
    const step1Inputs = step1View.querySelectorAll('[required]');
    let allValid = true;
    
    step1Inputs.forEach(input => {
      if (!input.value || input.value.trim() === '') {
        input.classList.add('border-brand');
        allValid = false;
      } else {
        input.classList.remove('border-brand');
      }
    });
    
    return allValid;
  }

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      formMsg.classList.add('hidden');
      if (validateStep1()) {
        currentStep = 2;
        updateStepUI();
        saveDraft(); // Save step progress
      } else {
        formMsg.textContent = 'Please fill out all required basic information fields.';
        formMsg.className = 'text-xs font-semibold p-2.5 rounded-lg text-center mb-4 bg-brand/10 border border-brand/20 text-brand';
        formMsg.classList.remove('hidden');
      }
    });
  }

  if (btnBack) {
    btnBack.addEventListener('click', () => {
      formMsg.classList.add('hidden');
      currentStep = 1;
      updateStepUI();
      saveDraft(); // Save step progress
    });
  }

  // --- Draft Auto-Save Logic ---
  function saveDraft() {
    const draft = {
      step: currentStep,
      values: {}
    };
    
    fields.forEach(id => {
      const input = document.getElementById(id);
      if (input) {
        draft.values[id] = input.value;
      }
    });
    
    localStorage.setItem('iconic_sell_draft', JSON.stringify(draft));
  }

  function loadDraft() {
    try {
      const saved = localStorage.getItem('iconic_sell_draft');
      if (!saved) return;
      const draft = JSON.parse(saved);
      
      // Load field values
      if (draft.values) {
        fields.forEach(id => {
          const input = document.getElementById(id);
          if (input && draft.values[id] !== undefined) {
            input.value = draft.values[id];
          }
        });
      }
      
      // Load current step
      if (draft.step === 2 && validateStep1()) {
        currentStep = 2;
        updateStepUI();
      }
    } catch (err) {
      console.error('Failed to load draft:', err);
    }
  }

  function clearDraft() {
    localStorage.removeItem('iconic_sell_draft');
    form.reset();
    currentStep = 1;
    updateStepUI();
  }

  // Hook input events on all fields for real-time draft saving
  form.addEventListener('input', saveDraft);
  form.addEventListener('change', saveDraft);

  // --- Form Submission ---
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    formMsg.classList.add('hidden');
    formMsg.textContent = '';

    const submitBtn = document.getElementById('btn-submit-listing');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = 'SUBMITTING LISTING...';

    // Parse photos input
    const photosRaw = document.getElementById('sell-photos').value;
    const photosArray = photosRaw 
      ? photosRaw.split(',').map(url => url.trim()).filter(url => url !== '') 
      : [];

    const payload = {
      location: document.getElementById('sell-location').value,
      brand: document.getElementById('sell-brand').value,
      model: document.getElementById('sell-model').value,
      trim: document.getElementById('sell-trim').value,
      specs: document.getElementById('sell-specs').value,
      year: parseInt(document.getElementById('sell-year').value),
      mileage: document.getElementById('sell-mileage').value,
      body_type: document.getElementById('sell-body-type').value,
      price: document.getElementById('sell-price').value,
      phone_number: document.getElementById('sell-phone').value,
      exterior_color: document.getElementById('sell-exterior-color').value,
      interior_color: document.getElementById('sell-interior-color').value,
      engine: document.getElementById('sell-engine').value,
      transmission: document.getElementById('sell-transmission').value,
      steering: document.getElementById('sell-steering').value,
      horsepower: document.getElementById('sell-horsepower').value,
      top_speed: document.getElementById('sell-top-speed').value,
      torque: document.getElementById('sell-torque').value,
      description: document.getElementById('sell-description').value,
      photos: photosArray
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

        // Clear local draft data
        clearDraft();

        // Redirect after a short delay
        setTimeout(() => {
          window.location.href = 'listings.html';
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
      console.error('Submit listing error:', err);
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    }
  });

  // Check auth and unlock page
  checkPageAuth();
  
  // Also check auth periodically or listen to messages to unlock page immediately on login
  window.addEventListener('focus', checkPageAuth);
});
