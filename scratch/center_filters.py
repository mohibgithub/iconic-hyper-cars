import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Center the filter bar on desktop & left-align on mobile ---
# Old parent container:
# <div class="w-full max-w-[48rem] mx-auto mb-6 flex items-center px-1 md:px-0">
html = html.replace(
    '<div class="w-full max-w-[48rem] mx-auto mb-6 flex items-center px-1 md:px-0">',
    '<div class="w-full max-w-[48rem] mx-auto mb-6 flex items-center justify-start md:justify-center px-1 md:px-0">'
)

# Old scrolling container:
# <div class="flex gap-2.5 overflow-x-auto scrollbar-none pb-2 flex-grow select-none filter-scroll-container">
html = html.replace(
    '<div class="flex gap-2.5 overflow-x-auto scrollbar-none pb-2 flex-grow select-none filter-scroll-container">',
    '<div class="flex gap-2.5 overflow-x-auto scrollbar-none pb-2 flex-grow md:flex-none select-none filter-scroll-container justify-start md:justify-center">'
)

# --- 2. Remove the old #filter-dropdowns-portal block ---
portal_block = """        <!-- Dropdown Menus Container (Outside scrolling wrapper to prevent cut-off bug) -->
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
          </div>

        </div>"""

html = html.replace(portal_block, "")

# --- 3. Place Dropdown Menus Container at the bottom of the body (just before <!-- SCRIPTS -->) ---
# We will make them use `absolute` instead of `fixed` positioning, so they align to document bounds.
bottom_portals = """    <!-- Filter Dropdown Menus (Body level absolute portal) -->
    <div id="menu-country" class="filter-dropdown-menu hidden absolute z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Global">Global</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="UAE">United Arab Emirates</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Germany">Germany</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Monaco">Monaco</button>
    </div>

    <div id="menu-price" class="filter-dropdown-menu hidden absolute z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Price">Any Price</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under €2M">Under €2,000,000</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="€2M - €5M">€2,000,000 - €5,000,000</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Over €5M">Over €5,000,000</button>
    </div>

    <div id="menu-year" class="filter-dropdown-menu hidden absolute z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Year">Any Year</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2025">2025</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2024">2024</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="2023">2023</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Older">2022 & Older</button>
    </div>

    <div id="menu-km" class="filter-dropdown-menu hidden absolute z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Mileage">Any Mileage</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="0 Km">0 Km (New)</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under 1k">Under 1,000 Km</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Under 5k">Under 5,000 Km</button>
    </div>

    <div id="menu-specs" class="filter-dropdown-menu hidden absolute z-50 min-w-[160px] bg-white dark:bg-zinc-900 border border-black/10 dark:border-white/10 rounded-[6px] shadow-lg py-1 text-[11px]">
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="Any Specs">Any Specs</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="GCC">GCC Specs</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="European">European Specs</button>
      <button class="dropdown-item w-full text-left px-3 py-2 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-colors uppercase tracking-wider font-bold text-zinc-800 dark:text-zinc-200" data-value="USA">USA Specs</button>
    </div>

  <!-- SCRIPTS -->"""

html = html.replace("  <!-- SCRIPTS -->", bottom_portals)

# --- 4. Update JavaScript positioning coordinates using window.scrollY and absolute placement ---
old_js_pos = """          if (isCurrentlyHidden) {
            // Position the menu dynamically below the button in viewport coordinates
            const rect = item.btn.getBoundingClientRect();
            item.menu.style.top = `${rect.bottom + 6}px`;
            item.menu.style.left = `${rect.left}px`;
            item.menu.classList.remove('hidden');
          }"""

new_js_pos = """          if (isCurrentlyHidden) {
            // Position the menu dynamically below the button in absolute coordinates
            const rect = item.btn.getBoundingClientRect();
            item.menu.style.top = `${rect.bottom + window.scrollY + 6}px`;
            item.menu.style.left = `${rect.left + window.scrollX}px`;
            item.menu.classList.remove('hidden');
          }"""

html = html.replace(old_js_pos, new_js_pos)

# --- 5. Remove window scroll listener since dropdowns are absolute and scroll naturally ---
# But keep resize & horizontal container scroll listeners to hide them.
old_js_scroll = """      // Close dropdowns on scroll and resize
      window.addEventListener('scroll', closeAllDropdowns);
      window.addEventListener('resize', closeAllDropdowns);"""

new_js_scroll = """      // Close dropdowns on filters container scroll or resize
      window.addEventListener('resize', closeAllDropdowns);"""

html = html.replace(old_js_scroll, new_js_scroll)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Filters centering and dropdown positioning adjustments applied successfully!")
