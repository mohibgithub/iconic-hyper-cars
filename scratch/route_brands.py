import os

index_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/index.html"
listings_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"
details_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/details.html"

# --- 1. Update index.html to route listings links to brands.html ---
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# Replace links in index.html
index_html = index_html.replace('href="listings.html"', 'href="brands.html"')
# Double-check specific instances of listings.html
index_html = index_html.replace('listings.html', 'brands.html')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)


# --- 2. Update details.html to route listings links to brands.html ---
with open(details_path, "r", encoding="utf-8") as f:
    details_html = f.read()

# Replace links in details.html
details_html = details_html.replace('href="listings.html"', 'href="brands.html"')
# Double-check specific instances of listings.html
details_html = details_html.replace('listings.html', 'brands.html')

with open(details_path, "w", encoding="utf-8") as f:
    f.write(details_html)


# --- 3. Update listings.html to route menu/sticky links to brands.html and add empty state JS ---
with open(listings_path, "r", encoding="utf-8") as f:
    listings_html = f.read()

# Replace sticky bottom / header links in listings.html
listings_html = listings_html.replace('href="listings.html"', 'href="brands.html"')
# But wait! We do NOT want to change the file references in script comments or search links if they are internal,
# but replacing the HTML anchors is what we want. Let's do a targeted replace for listings.html links.
# Let's replace the mobile menu and bottom nav anchors specifically.
listings_html = listings_html.replace('href="listings.html"', 'href="brands.html"')

# Add dynamic brand URL checker to show empty state when brand !== bugatti
old_js_block = """    // --- Listing Card Custom Page Logic ---
    document.addEventListener('DOMContentLoaded', () => {"""

new_js_block = """    // --- Listing Card Custom Page Logic ---
    document.addEventListener('DOMContentLoaded', () => {
      
      // 0. Brand Selection Query Checker
      const urlParams = new URLSearchParams(window.location.search);
      const brandParam = urlParams.get('brand');
      const chironCard = document.querySelector('.listing-card');
      
      if (brandParam && brandParam !== 'bugatti') {
        if (chironCard) {
          chironCard.style.display = 'none';
          
          // Render a clean luxury empty state container
          const emptyState = document.createElement('div');
          emptyState.className = 'w-full py-20 text-center flex flex-col items-center justify-center bg-white dark:bg-zinc-900/20 border border-black/10 dark:border-white/10 rounded-[12px] p-8 shadow-sm';
          emptyState.innerHTML = `
            <h3 class="text-base font-bold uppercase tracking-widest text-zinc-900 dark:text-white font-logo mb-2">No Listings Found</h3>
            <p class="text-xs text-zinc-500 dark:text-zinc-400 font-medium mb-6">There are currently no active listings for this manufacturer.</p>
            <a href="brands.html" class="bg-brand text-white font-bold text-[11px] uppercase tracking-wider px-5 py-2.5 rounded-[6px] hover:bg-brand/80 transition-all active:scale-95 shadow-md">Choose Another Brand</a>
          `;
          chironCard.parentNode.appendChild(emptyState);
        }
      }"""

listings_html = listings_html.replace(old_js_block, new_js_block)

with open(listings_path, "w", encoding="utf-8") as f:
    f.write(listings_html)

print("Brands page routing and listings empty-state javascript successfully integrated!")
