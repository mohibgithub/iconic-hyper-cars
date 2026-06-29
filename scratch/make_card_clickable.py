import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Replace the Card 1 Section with clickable overlay and removed expanded gallery ---
old_card_code = """          <!-- CARD 1: BUGATTI CHIRON -->
          <div class="listing-card bg-white dark:bg-zinc-900/40 border border-black/15 dark:border-white/10 rounded-[12px] overflow-hidden shadow-card hover:shadow-card-hover transition-all duration-300 flex flex-col md:flex-row p-3 md:p-4 gap-4">
            
            <!-- Left Side: Image Gallery -->
            <div class="w-full md:w-[42%] shrink-0">
              <!-- Main Image Display -->
              <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">
                <img src="assets/images/product-list/bugatti/2200xxs.webp" alt="Bugatti Chiron"
                  class="main-car-img w-full h-full object-contain pointer-events-none transition-all duration-200 group-hover:scale-[1.03]" />
                
                <!-- Overlay Badges -->
                <span class="absolute top-2.5 left-2.5 bg-brand text-white text-[9px] font-bold uppercase px-2.5 py-1 rounded-[6px] shadow-md tracking-wider">CAR OF THE WEEK</span>
              </div>

              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron profile" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron rear three quarters" />
                </div>
                <div id="trigger-more-gallery" class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                  <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron rear straight" />
                  <div id="more-overlay" class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
                </div>
              </div>

              <!-- Expanded Gallery Grid (Collapsible Portal) -->
              <div id="expanded-gallery" class="grid grid-cols-4 gap-2 max-h-0 overflow-hidden transition-all duration-500 ease-in-out select-none">
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (2).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 4" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (3).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 5" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (4).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 6" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (5).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 7" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (6).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 8" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (7).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 9" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (8).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 10" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (9).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 11" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (10).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 12" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (11).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 13" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (12).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 14" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (2).webp" class="thumb-img w-full h-full object-contain bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron interior" />
                </div>
              </div>
            </div>"""

new_card_code = """          <!-- CARD 1: BUGATTI CHIRON -->
          <div class="listing-card relative cursor-pointer bg-white dark:bg-zinc-900/40 border border-black/15 dark:border-white/10 rounded-[12px] overflow-hidden shadow-card hover:shadow-card-hover transition-all duration-300 flex flex-col md:flex-row p-3 md:p-4 gap-4">
            <!-- Absolute overlay link to details page -->
            <a href="details.html" class="absolute inset-0 z-10" aria-label="View Bugatti Chiron Details"></a>

            <!-- Left Side: Image Gallery -->
            <div class="w-full md:w-[42%] shrink-0">
              <!-- Main Image Display -->
              <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">
                <img src="assets/images/product-list/bugatti/2200xxs.webp" alt="Bugatti Chiron"
                  class="main-car-img w-full h-full object-contain pointer-events-none transition-all duration-200 group-hover:scale-[1.03]" />
                
                <!-- Overlay Badges -->
                <span class="absolute top-2.5 left-2.5 bg-brand text-white text-[9px] font-bold uppercase px-2.5 py-1 rounded-[6px] shadow-md tracking-wider">CAR OF THE WEEK</span>
              </div>

              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron profile" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron rear three quarters" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                  <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron rear straight" />
                  <div class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
                </div>
              </div>
            </div>"""

html = html.replace(old_card_code, new_card_code)

# --- 2. Make Call and WhatsApp buttons container relative z-20 to capture clicks ---
old_buttons = """                <!-- Call / WhatsApp Buttons -->
                <div class="flex items-center gap-2 w-full sm:w-auto shrink-0 select-none">"""

new_buttons = """                <!-- Call / WhatsApp Buttons -->
                <div class="flex items-center gap-2 w-full sm:w-auto shrink-0 select-none relative z-20">"""

html = html.replace(old_buttons, new_buttons)

# --- 3. Clean up listings page Javascript logic (remove thumbnail swapper & expanded gallery scripts) ---
old_js_swap_expanded = """      // 1. Thumbnail Click Handler - Swap Main Car Image (with Smooth Fade Transition)
      const listingCards = document.querySelectorAll('.listing-card');
      
      listingCards.forEach(card => {
        const mainImg = card.querySelector('.main-car-img');
        const thumbnails = card.querySelectorAll('.thumb-wrapper');
        
        thumbnails.forEach(thumb => {
          thumb.addEventListener('click', () => {
            const thumbImg = thumb.querySelector('.thumb-img');
            if (mainImg && thumbImg && mainImg.src !== thumbImg.src) {
              // Trigger fade-out
              mainImg.classList.add('opacity-0');
              
              setTimeout(() => {
                // Swap source after fade-out
                mainImg.src = thumbImg.src;
                // Trigger fade-in
                mainImg.classList.remove('opacity-0');
              }, 180); // matches transition-duration slightly under 200ms
              
              // Reset border styles on thumbnails
              thumbnails.forEach(t => {
                t.classList.remove('border-brand', 'dark:border-brand');
                t.classList.add('border-black/10', 'dark:border-white/10');
              });
              
              // Set active border on clicked thumbnail
              thumb.classList.remove('border-black/10', 'dark:border-white/10');
              thumb.classList.add('border-brand', 'dark:border-brand');
            }
          });
        });
      });

      // 2. Favorite button toggle interaction
      const favButtons = document.querySelectorAll('.fav-btn');
      favButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const heartIcon = btn.querySelector('.fav-heart');
          if (heartIcon) {
            if (heartIcon.getAttribute('fill') === 'currentColor') {
              // Toggle off
              heartIcon.setAttribute('fill', 'none');
              heartIcon.classList.remove('text-brand');
              heartIcon.classList.add('text-white');
            } else {
              // Toggle on
              heartIcon.setAttribute('fill', 'currentColor');
              heartIcon.classList.remove('text-white');
              heartIcon.classList.add('text-brand');
              
              // Quick scale bounce animation
              btn.classList.add('scale-125');
              setTimeout(() => {
                btn.classList.remove('scale-125');
              }, 200);
            }
          }
        });
      });

      // 2.5. Expanded Gallery Toggle Logic
      const triggerBtn = document.getElementById('trigger-more-gallery');
      const expandedGallery = document.getElementById('expanded-gallery');
      const moreOverlay = document.getElementById('more-overlay');
      
      if (triggerBtn && expandedGallery) {
        triggerBtn.addEventListener('click', () => {
          const isClosed = expandedGallery.classList.contains('max-h-0');
          if (isClosed) {
            expandedGallery.classList.remove('max-h-0');
            expandedGallery.classList.add('max-h-[800px]', 'mt-3');
            if (moreOverlay) moreOverlay.textContent = "LESS";
          } else {
            expandedGallery.classList.remove('max-h-[800px]', 'mt-3');
            expandedGallery.classList.add('max-h-0');
            if (moreOverlay) moreOverlay.textContent = "+12";
          }
        });
      }"""

new_js_swap_expanded = """      // 2. Favorite button toggle interaction (Legacy)
      const favButtons = document.querySelectorAll('.fav-btn');
      favButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
        });
      });"""

html = html.replace(old_js_swap_expanded, new_js_swap_expanded)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Listings card click navigation and thumbnail styling successfully applied!")
