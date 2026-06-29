import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Fix Double vertical Divider after Filters ---
# Replace <span class="h-5 w-px bg-zinc-300 dark:bg-zinc-850 mx-3 shrink-0">|</span>
# with a single clean vertical border line (no inner pipe text)
html = html.replace(
    '<span class="h-5 w-px bg-zinc-300 dark:bg-zinc-850 mx-3 shrink-0">|</span>',
    '<span class="h-5 w-px bg-zinc-300 dark:bg-zinc-800 mx-3 shrink-0"></span>'
)

# --- 2. Replace the Filters Scrolling area with new layout (Portal-ready buttons) ---
old_scrolling_filters = """          <!-- Scrolling Filter Pills Container -->
          <div class="flex gap-2.5 overflow-x-auto scrollbar-none pb-2 flex-grow select-none">
            
            <!-- Country Dropdown -->
            <div class="relative filter-dropdown-container">
              <button class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8">
                <span class="filter-label">Country</span>
                <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
              </button>
              <div class="filter-dropdown-menu hidden absolute top-full left-0 mt-1.5 z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Global">Global</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="UAE">United Arab Emirates</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Germany">Germany</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Monaco">Monaco</button>
              </div>
            </div>

            <!-- Price Dropdown -->
            <div class="relative filter-dropdown-container">
              <button class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8">
                <span class="filter-label">Price</span>
                <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
              </button>
              <div class="filter-dropdown-menu hidden absolute top-full left-0 mt-1.5 z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Any Price">Any Price</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Under €2M">Under €2,000,000</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="€2M - €5M">€2,000,000 - €5,000,000</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Over €5M">Over €5,000,000</button>
              </div>
            </div>

            <!-- Year Dropdown -->
            <div class="relative filter-dropdown-container">
              <button class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8">
                <span class="filter-label">Year</span>
                <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
              </button>
              <div class="filter-dropdown-menu hidden absolute top-full left-0 mt-1.5 z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Any Year">Any Year</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="2025">2025</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="2024">2024</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="2023">2023</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Older">2022 & Older</button>
              </div>
            </div>

            <!-- Kilometres Dropdown -->
            <div class="relative filter-dropdown-container">
              <button class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8">
                <span class="filter-label">Kilometres</span>
                <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
              </button>
              <div class="filter-dropdown-menu hidden absolute top-full left-0 mt-1.5 z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Any Mileage">Any Mileage</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="0 Km">0 Km (New)</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Under 1k">Under 1,000 Km</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Under 5k">Under 5,000 Km</button>
              </div>
            </div>

            <!-- Regional Specs Dropdown -->
            <div class="relative filter-dropdown-container">
              <button class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8">
                <span class="filter-label">Regional Specs</span>
                <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
              </button>
              <div class="filter-dropdown-menu hidden absolute top-full left-0 mt-1.5 z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="Any Specs">Any Specs</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="GCC">GCC Specs</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="European">European Specs</button>
                <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold" data-value="USA">USA Specs</button>
              </div>
            </div>

          </div>
        </div>"""

new_scrolling_filters = """          <!-- Scrolling Filter Pills Container -->
          <div class="flex gap-2.5 overflow-x-auto scrollbar-none pb-2 flex-grow select-none filter-scroll-container">
            
            <!-- Country Button -->
            <button id="filter-country-btn" class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8 shrink-0">
              <span class="filter-label">Country</span>
              <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Price Button -->
            <button id="filter-price-btn" class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8 shrink-0">
              <span class="filter-label">Price</span>
              <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Year Button -->
            <button id="filter-year-btn" class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8 shrink-0">
              <span class="filter-label">Year</span>
              <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Kilometres Button -->
            <button id="filter-km-btn" class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8 shrink-0">
              <span class="filter-label">Kilometres</span>
              <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Regional Specs Button -->
            <button id="filter-specs-btn" class="filter-btn flex items-center gap-1 px-3 py-1.5 border border-black/10 dark:border-white/10 rounded-[6px] bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[11px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider h-8 shrink-0">
              <span class="filter-label">Regional Specs</span>
              <svg class="h-2.5 w-2.5 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

          </div>
        </div>

        <!-- Dropdown Menus Container (Outside scrolling wrapper to prevent cut-off bug) -->
        <div id="filter-dropdowns-portal" class="relative">
          
          <!-- Country Dropdown Menu -->
          <div id="menu-country" class="filter-dropdown-menu hidden fixed z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Global">Global</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="UAE">United Arab Emirates</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Germany">Germany</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Monaco">Monaco</button>
          </div>

          <!-- Price Dropdown Menu -->
          <div id="menu-price" class="filter-dropdown-menu hidden fixed z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Price">Any Price</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under €2M">Under €2,000,000</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="€2M - €5M">€2,000,000 - €5,000,000</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Over €5M">Over €5,000,000</button>
          </div>

          <!-- Year Dropdown Menu -->
          <div id="menu-year" class="filter-dropdown-menu hidden fixed z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Year">Any Year</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2025">2025</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2024">2024</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2023">2023</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Older">2022 & Older</button>
          </div>

          <!-- Kilometres Dropdown Menu -->
          <div id="menu-km" class="filter-dropdown-menu hidden fixed z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Mileage">Any Mileage</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="0 Km">0 Km (New)</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under 1k">Under 1,000 Km</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under 5k">Under 5,000 Km</button>
          </div>

          <!-- Regional Specs Dropdown Menu -->
          <div id="menu-specs" class="filter-dropdown-menu hidden fixed z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Specs">Any Specs</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="GCC">GCC Specs</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="European">European Specs</button>
            <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="USA">USA Specs</button>
          </div>"""

html = html.replace(old_scrolling_filters, new_scrolling_filters)

# --- 3. Replace old active filter Javascript logic with new dynamic positioning Javascript logic ---
old_js_logic = """      // 3. Filter Dropdown Toggle & Selection Logic
      const dropdownContainers = document.querySelectorAll('.filter-dropdown-container');
      
      dropdownContainers.forEach(container => {
        const btn = container.querySelector('.filter-btn');
        const menu = container.querySelector('.filter-dropdown-menu');
        const label = container.querySelector('.filter-label');
        const originalText = label.textContent;
        
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          // Close all other menus
          dropdownContainers.forEach(other => {
            if (other !== container) {
              other.querySelector('.filter-dropdown-menu').classList.add('hidden');
            }
          });
          // Toggle current menu
          menu.classList.toggle('hidden');
        });
        
        const items = container.querySelectorAll('.dropdown-item');
        items.forEach(item => {
          item.addEventListener('click', (e) => {
            e.stopPropagation();
            const value = item.getAttribute('data-value');
            
            // Set value and active styling
            label.textContent = value;
            menu.classList.add('hidden');
            
            // Toggle active visual state
            if (value && value !== 'Global' && value !== 'Any Price' && value !== 'Any Year' && value !== 'Any Mileage' && value !== 'Any Specs') {
              btn.classList.add('bg-brand', 'text-white', 'border-brand');
              btn.classList.remove('bg-white', 'dark:bg-zinc-900', 'text-zinc-800', 'dark:text-zinc-200');
            } else {
              // Reset to original state
              label.textContent = originalText;
              btn.classList.remove('bg-brand', 'text-white', 'border-brand');
              btn.classList.add('bg-white', 'dark:bg-zinc-900', 'text-zinc-800', 'dark:text-zinc-200');
            }
          });
        });
      });
      
      // Close dropdowns on click outside
      document.addEventListener('click', () => {
        dropdownContainers.forEach(container => {
          container.querySelector('.filter-dropdown-menu').classList.add('hidden');
        });
      });"""

new_js_logic = """      // 3. Filter Dropdown Toggle & Selection Logic (Fixed Position Portal)
      const filterButtons = [
        { btn: document.getElementById('filter-country-btn'), menu: document.getElementById('menu-country') },
        { btn: document.getElementById('filter-price-btn'), menu: document.getElementById('menu-price') },
        { btn: document.getElementById('filter-year-btn'), menu: document.getElementById('menu-year') },
        { btn: document.getElementById('filter-km-btn'), menu: document.getElementById('menu-km') },
        { btn: document.getElementById('filter-specs-btn'), menu: document.getElementById('menu-specs') },
      ];
      
      const allMenus = document.querySelectorAll('.filter-dropdown-menu');
      
      function closeAllDropdowns() {
        allMenus.forEach(menu => menu.classList.add('hidden'));
      }
      
      filterButtons.forEach(item => {
        if (!item.btn || !item.menu) return;
        
        const label = item.btn.querySelector('.filter-label');
        const originalText = label.textContent;
        
        item.btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const isCurrentlyHidden = item.menu.classList.contains('hidden');
          closeAllDropdowns();
          
          if (isCurrentlyHidden) {
            // Position the menu dynamically below the button in viewport coordinates
            const rect = item.btn.getBoundingClientRect();
            item.menu.style.top = `${rect.bottom + 6}px`;
            item.menu.style.left = `${rect.left}px`;
            item.menu.classList.remove('hidden');
          }
        });
        
        const dropdownItems = item.menu.querySelectorAll('.dropdown-item');
        dropdownItems.forEach(dropItem => {
          dropItem.addEventListener('click', (e) => {
            e.stopPropagation();
            const value = dropItem.getAttribute('data-value');
            label.textContent = value;
            item.menu.classList.add('hidden');
            
            // Highlight active filter state
            if (value && value !== 'Global' && value !== 'Any Price' && value !== 'Any Year' && value !== 'Any Mileage' && value !== 'Any Specs') {
              item.btn.classList.add('bg-brand', 'text-white', 'border-brand');
              item.btn.classList.remove('bg-white', 'dark:bg-zinc-900', 'text-zinc-800', 'dark:text-zinc-200');
            } else {
              label.textContent = originalText;
              item.btn.classList.remove('bg-brand', 'text-white', 'border-brand');
              item.btn.classList.add('bg-white', 'dark:bg-zinc-900', 'text-zinc-800', 'dark:text-zinc-200');
            }
          });
        });
      });
      
      // Close dropdowns on scroll of filters scroll container
      const filterScrollContainer = document.querySelector('.filter-scroll-container');
      if (filterScrollContainer) {
        filterScrollContainer.addEventListener('scroll', closeAllDropdowns);
      }
      
      // Close dropdowns on scroll and resize
      window.addEventListener('scroll', closeAllDropdowns);
      window.addEventListener('resize', closeAllDropdowns);
      
      // Close dropdowns on click outside
      document.addEventListener('click', closeAllDropdowns);"""

html = html.replace(old_js_logic, new_js_logic)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Dropdown clipping and border issues fixed successfully!")
