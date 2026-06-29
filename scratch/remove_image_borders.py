import os

listings_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"
details_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/details.html"

# --- 1. Modify listings.html main display border-radius and remove borders ---
with open(listings_path, "r", encoding="utf-8") as f:
    listings_html = f.read()

# Replace main display div
old_listings_main = '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/10 dark:border-white/10">'
new_listings_main = '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[12px] overflow-hidden group select-none">'
listings_html = listings_html.replace(old_listings_main, new_listings_main)

# Replace thumbnails row
old_listings_thumbs = """              <!-- 3 Smaller Thumbnails underneath -->
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
              </div>"""

new_listings_thumbs = """              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron profile" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200">
                  <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron rear three quarters" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 relative">
                  <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron rear straight" />
                  <div class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
                </div>
              </div>"""

listings_html = listings_html.replace(old_listings_thumbs, new_listings_thumbs)

with open(listings_path, "w", encoding="utf-8") as f:
    f.write(listings_html)


# --- 2. Modify details.html main display border-radius, remove borders and apply opacity states ---
with open(details_path, "r", encoding="utf-8") as f:
    details_html = f.read()

# Replace main display
old_details_main = '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-900 rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 select-none shadow-sm">'
new_details_main = '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-900 rounded-[12px] overflow-hidden select-none shadow-sm">'
details_html = details_html.replace(old_details_main, new_details_main)

# Replace thumbnails row (remove borders, add opacity classes)
old_details_thumbs = """            <!-- Thumbnail row -->
            <div class="flex gap-2.5 select-none">
              <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron profile" />
              </div>
              <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron rear three quarters" />
              </div>
              <div id="trigger-more-gallery" class="thumb-wrapper flex-1 aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron rear view" />
                <div id="more-overlay" class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
              </div>
            </div>"""

new_details_thumbs = """            <!-- Thumbnail row -->
            <div class="flex gap-2.5 select-none">
              <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-100">
                <img src="assets/images/product-list/bugatti/2200xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron profile" />
              </div>
              <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs.webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron rear three quarters" />
              </div>
              <div id="trigger-more-gallery" class="thumb-wrapper flex-1 aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 relative opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (1).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron rear view" />
                <div id="more-overlay" class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+12</div>
              </div>
            </div>"""

details_html = details_html.replace(old_details_thumbs, new_details_thumbs)

# Replace expanded gallery grid item classes
old_expanded_thumbs = """            <!-- Collapsible Gallery (Portal of remaining 12 images) -->
            <div id="expanded-gallery" class="grid grid-cols-4 gap-2.5 max-h-0 overflow-hidden transition-all duration-500 ease-in-out select-none">
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (2).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 4" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (3).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 5" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (4).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 6" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (5).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 7" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (6).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 8" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (7).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 9" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (8).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 10" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (9).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 11" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (10).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 12" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (11).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 13" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/1900xxs (12).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron angle 14" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                <img src="assets/images/product-list/bugatti/2200xxs (2).webp" class="thumb-img w-full h-full object-cover rounded-[6px]" alt="Bugatti Chiron interior" />
              </div>
            </div>"""

new_expanded_thumbs = """            <!-- Collapsible Gallery (Portal of remaining 12 images) -->
            <div id="expanded-gallery" class="grid grid-cols-4 gap-2.5 max-h-0 overflow-hidden transition-all duration-500 ease-in-out select-none">
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (2).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 4" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (3).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 5" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (4).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 6" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (5).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 7" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (6).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 8" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (7).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 9" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (8).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 10" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (9).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 11" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (10).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 12" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (11).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 13" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/1900xxs (12).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron angle 14" />
              </div>
              <div class="thumb-wrapper aspect-[3/2] rounded-[12px] overflow-hidden cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100">
                <img src="assets/images/product-list/bugatti/2200xxs (2).webp" class="thumb-img w-full h-full object-cover rounded-[12px]" alt="Bugatti Chiron interior" />
              </div>
            </div>"""

details_html = details_html.replace(old_expanded_thumbs, new_expanded_thumbs)

# Replace Javascript logic in details.html (switch active border styling to active opacity styling)
old_details_js = """            thumbnails.forEach(t => {
              t.classList.remove('border-brand', 'dark:border-brand');
              t.classList.add('border-black/10', 'dark:border-white/10');
            });
            thumb.classList.remove('border-black/10', 'dark:border-white/10');
            thumb.classList.add('border-brand', 'dark:border-brand');"""

new_details_js = """            thumbnails.forEach(t => {
              t.classList.remove('opacity-100');
              t.classList.add('opacity-60');
            });
            thumb.classList.remove('opacity-60');
            thumb.classList.add('opacity-100');"""

details_html = details_html.replace(old_details_js, new_details_js)

# Second JS block in toggle expanded gallery
old_details_js2 = """                  // Reset active borders across ALL thumbnails
                  thumbnails.forEach(t => {
                    t.classList.remove('border-brand', 'dark:border-brand');
                    t.classList.add('border-black/10', 'dark:border-white/10');
                  });
                  extraThumbs.forEach(t => {
                    t.classList.remove('border-brand', 'dark:border-brand');
                    t.classList.add('border-black/10', 'dark:border-white/10');
                  });
                  thumb.classList.remove('border-black/10', 'dark:border-white/10');
                  thumb.classList.add('border-brand', 'dark:border-brand');"""

new_details_js2 = """                  // Reset active opacity across ALL thumbnails
                  thumbnails.forEach(t => {
                    t.classList.remove('opacity-100');
                    t.classList.add('opacity-60');
                  });
                  extraThumbs.forEach(t => {
                    t.classList.remove('opacity-100');
                    t.classList.add('opacity-60');
                  });
                  thumb.classList.remove('opacity-60');
                  thumb.classList.add('opacity-100');"""

details_html = details_html.replace(old_details_js2, new_details_js2)

with open(details_path, "w", encoding="utf-8") as f:
    f.write(details_html)

print("Border radius rounded-[12px] applied and red active borders replaced with opacity swaps successfully!")
