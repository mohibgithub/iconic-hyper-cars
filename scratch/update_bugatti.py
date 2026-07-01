import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Replace Listing Card 1 (Bugatti Chiron) with updated images & content ---
old_card_area = """          <!-- CARD 1: BUGATTI CHIRON -->
          <div class="listing-card bg-white dark:bg-zinc-900/40 border border-black/15 dark:border-white/10 rounded-[12px] overflow-hidden shadow-card hover:shadow-card-hover transition-all duration-300 flex flex-col md:flex-row p-3 md:p-4 gap-4">
            
            <!-- Left Side: Image Gallery -->
            <div class="w-full md:w-[42%] shrink-0">
              <!-- Main Image Display -->
              <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">
                <img src="assets/images/chiron.png" alt="Bugatti Chiron Super Sport"
                  class="main-car-img w-full h-full object-cover pointer-events-none transition-transform duration-500 group-hover:scale-[1.03]" />
                
                <!-- Overlay Badges -->
                <span class="absolute top-2.5 left-2.5 bg-brand text-white text-[9px] font-bold uppercase px-2.5 py-1 rounded-[6px] shadow-md tracking-wider">CAR OF THE WEEK</span>
              </div>

              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                  <img src="assets/images/chiron.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 1" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/mercedes_one.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 2" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                  <img src="assets/images/ferrari_enzo.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 3" />
                  <div class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+20</div>
                </div>
              </div>
            </div>

            <!-- Right Side: Details and Actions -->
            <div class="flex-1 flex flex-col justify-between pt-1">
              
              <!-- Upper Info Block -->
              <div>
                <!-- Price & Date Row -->
                <div class="flex items-baseline justify-between mb-1.5">
                  <span class="text-xl md:text-2xl font-extrabold text-zinc-950 dark:text-white uppercase tracking-tight">EUR 9,999,999</span>
                  <span class="text-[11px] text-zinc-500 dark:text-zinc-400 font-semibold">1 hour ago</span>
                </div>

                <!-- Title Header -->
                <h3 class="text-base md:text-lg font-bold text-zinc-900 dark:text-white uppercase tracking-wide font-logo mb-1 leading-snug">
                  Bugatti <span class="text-zinc-300 dark:text-zinc-700 mx-1">•</span> Chiron <span class="text-zinc-300 dark:text-zinc-700 mx-1">•</span> Super Sport
                </h3>

                <!-- First Line Description -->
                <p class="text-xs md:text-[13px] text-zinc-500 dark:text-zinc-400 mb-4 leading-relaxed line-clamp-1 font-medium">
                  Brand new condition (first line of description)
                </p>

                <!-- Spec Grid Pills -->
                <div class="grid grid-cols-2 gap-2 mb-4 max-w-sm">
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Year</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">2024</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Mileage</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">0 Km</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Drive</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">Left hand</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Specs</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">GCC Specs</span>
                  </div>
                </div>
              </div>"""

new_card_area = """          <!-- CARD 1: BUGATTI CHIRON -->
          <div class="listing-card bg-white dark:bg-zinc-900/40 border border-black/15 dark:border-white/10 rounded-[12px] overflow-hidden shadow-card hover:shadow-card-hover transition-all duration-300 flex flex-col md:flex-row p-3 md:p-4 gap-4">
            
            <!-- Left Side: Image Gallery -->
            <div class="w-full md:w-[42%] shrink-0">
              <!-- Main Image Display -->
              <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">
                <img src="assets/images/product-list/bugatti/2200xxs.webp" alt="Bugatti Chiron"
                  class="main-car-img w-full h-full object-cover pointer-events-none transition-transform duration-500 group-hover:scale-[1.03]" />
                
                <!-- Overlay Badges -->
                <span class="absolute top-2.5 left-2.5 bg-brand text-white text-[9px] font-bold uppercase px-2.5 py-1 rounded-[6px] shadow-md tracking-wider">CAR OF THE WEEK</span>
              </div>

              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron profile" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron rear three quarters" />
                </div>
                <div id="trigger-more-gallery" class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                  <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron rear straight" />
                  <div id="more-overlay" class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
                </div>
              </div>

              <!-- Expanded Gallery Grid (Collapsible Portal) -->
              <div id="expanded-gallery" class="grid grid-cols-4 gap-2 max-h-0 overflow-hidden transition-all duration-500 ease-in-out select-none">
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (2).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 4" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (3).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 5" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (4).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 6" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (5).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 7" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (6).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 8" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (7).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 9" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (8).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 10" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (9).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 11" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (10).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 12" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (11).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 13" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs (12).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 14" />
                </div>
                <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (2).webp" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron interior" />
                </div>
              </div>
            </div>

            <!-- Right Side: Details and Actions -->
            <div class="flex-1 flex flex-col justify-between pt-1">
              
              <!-- Upper Info Block -->
              <div>
                <!-- Price & Date Row -->
                <div class="flex items-baseline justify-between mb-1.5">
                  <span class="text-xl md:text-2xl font-extrabold text-zinc-950 dark:text-white uppercase tracking-tight">EUR 3,600,000</span>
                  <span class="text-[11px] text-zinc-500 dark:text-zinc-400 font-semibold">1 hour ago</span>
                </div>

                <!-- Title Header -->
                <h3 class="text-base md:text-lg font-bold text-zinc-900 dark:text-white uppercase tracking-wide font-logo mb-1 leading-snug">
                  Bugatti <span class="text-zinc-300 dark:text-zinc-700 mx-1">•</span> Chiron <span class="text-zinc-300 dark:text-zinc-700 mx-1">•</span> Luxury Coupe
                </h3>

                <!-- First Line Description -->
                <p class="text-xs md:text-[13px] text-zinc-500 dark:text-zinc-400 mb-4 leading-relaxed line-clamp-1 font-medium">
                  Pristine dark blue Bugatti Chiron in showroom condition. Low mileage, fully serviced.
                </p>

                <!-- Spec Grid Pills -->
                <div class="grid grid-cols-2 gap-2 mb-4 max-w-sm">
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Year</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">2021</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Mileage</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">2,200 Km</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Drive</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">Left hand</span>
                  </div>
                  <div class="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-zinc-100/70 dark:bg-zinc-900 border border-black/[0.04] dark:border-white/[0.04]">
                    <span class="text-[10px] font-bold text-zinc-400 uppercase shrink-0">Specs</span>
                    <span class="text-[11px] font-bold text-zinc-800 dark:text-zinc-200">GCC Specs</span>
                  </div>
                </div>
              </div>"""

html = html.replace(old_card_area, new_card_area)

# --- 2. Add JavaScript gallery toggle logic ---
old_js_block = """      // 3. Filter Dropdown Toggle & Selection Logic (Fixed Position Portal)"""

new_js_block = """      // 2.5. Expanded Gallery Toggle Logic
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
      }

      // 3. Filter Dropdown Toggle & Selection Logic (Fixed Position Portal)"""

html = html.replace(old_js_block, new_js_block)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Bugatti Chiron images and gallery toggle scripts integrated successfully!")
