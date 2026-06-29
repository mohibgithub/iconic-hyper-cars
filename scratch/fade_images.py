import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Update main car image class in Listings page to include transition-all and duration-200 ---
# Old:
# class="main-car-img w-full h-full object-contain pointer-events-none transition-transform duration-500 group-hover:scale-[1.03]"
html = html.replace(
    'class="main-car-img w-full h-full object-contain pointer-events-none transition-transform duration-500 group-hover:scale-[1.03]"',
    'class="main-car-img w-full h-full object-contain pointer-events-none transition-all duration-200 group-hover:scale-[1.03]"'
)

# --- 2. Update the JavaScript Thumbnail Click Handler to implement the fade transition ---
old_js_swap = """      // 1. Thumbnail Click Handler - Swap Main Car Image
      const listingCards = document.querySelectorAll('.listing-card');
      
      listingCards.forEach(card => {
        const mainImg = card.querySelector('.main-car-img');
        const thumbnails = card.querySelectorAll('.thumb-wrapper');
        
        thumbnails.forEach(thumb => {
          thumb.addEventListener('click', () => {
            const thumbImg = thumb.querySelector('.thumb-img');
            if (mainImg && thumbImg) {
              // Swap the image sources
              const oldMainSrc = mainImg.src;
              mainImg.src = thumbImg.src;
              
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
      });"""

new_js_swap = """      // 1. Thumbnail Click Handler - Swap Main Car Image (with Smooth Fade Transition)
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
      });"""

html = html.replace(old_js_swap, new_js_swap)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Fade transitions for image swap implemented successfully!")
