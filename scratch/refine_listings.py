import os
import re

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Header Refinement ---
old_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-zinc-950 dark:bg-zinc-950/80 backdrop-blur-md px-4 py-4 md:py-6 md:px-12 flex items-center justify-between border-b border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-between">
        <div class="flex items-center gap-4">
          <button popovertarget="mobile-menu" aria-label="Open navigation menu"
            class="text-white hover:text-[#c9c9c9] active:text-[#c9c9c9] active:scale-95 transition-all duration-200">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current md:h-7 md:w-7" fill="none"
              viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>

          <button popovertarget="search-popover" aria-label="Search listings"
            class="text-white hover:text-[#c9c9c9] active:text-[#c9c9c9] active:scale-95 transition-all duration-200">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current md:h-7 md:w-7" fill="none"
              viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </button>
        </div>

        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>

        <div class="flex items-center gap-4">
          <button id="theme-toggle-btn" aria-label="Toggle dark mode"
            class="text-white hover:text-[#c9c9c9] active:text-[#c9c9c9] active:scale-95 transition-all duration-200">
            <svg id="sun-icon" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current hidden" fill="none"
              viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707-.707M12 8a4 4 0 100 8 4 4 0 000-8z" />
            </svg>
            <svg id="moon-icon" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current" fill="none"
              viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
            </svg>
          </button>

          <button popovertarget="profile-popover" aria-label="View profile"
            class="text-white hover:text-[#c9c9c9] active:text-[#c9c9c9] active:scale-95 transition-all duration-200">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current" fill="none" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </button>
        </div>
      </div>
    </header>"""

new_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-zinc-950 dark:bg-zinc-950/80 backdrop-blur-md px-4 py-4 md:py-5 border-b border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-center relative">
        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>
        <!-- Hidden Compatibility Container for main.js element selector checks -->
        <div class="hidden">
          <button id="theme-toggle-btn">
            <span id="sun-icon"></span>
            <span id="moon-icon"></span>
          </button>
        </div>
      </div>
    </header>"""

html = html.replace(old_header, new_header)

# --- 2. Profile Popover Radius & Inputs ---
html = html.replace('class="user-profile-dropdown bg-white dark:bg-zinc-900 text-zinc-900 dark:text-white p-6 rounded-2xl shadow-2xl border border-zinc-100 dark:border-zinc-800/80 transition-colors duration-300 w-[320px] sm:w-[350px]"',
                    'class="user-profile-dropdown bg-white dark:bg-zinc-900 text-zinc-900 dark:text-white p-6 rounded-[12px] shadow-2xl border border-zinc-100 dark:border-zinc-800/80 transition-colors duration-300 w-[320px] sm:w-[350px]"')

html = html.replace('class="w-full text-xs px-3 py-2 rounded-lg bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 focus:outline-none focus:border-brand transition-colors duration-200 text-zinc-900 dark:text-white placeholder-zinc-400"',
                    'class="w-full text-xs px-3 py-2 rounded-[6px] bg-zinc-50 dark:bg-zinc-950 border border-zinc-200 dark:border-zinc-800 focus:outline-none focus:border-brand transition-colors duration-200 text-zinc-900 dark:text-white placeholder-zinc-400"')

html = html.replace('class="w-full bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-2.5 rounded-lg active:scale-[0.98] transition-all duration-200 shadow-md"',
                    'class="w-full bg-zinc-900 dark:bg-white text-white dark:text-black hover:bg-zinc-800 dark:hover:bg-zinc-100 font-bold text-xs uppercase tracking-wider py-2.5 rounded-[6px] active:scale-[0.98] transition-all duration-200 shadow-md"')

html = html.replace('class="w-full flex items-center justify-center gap-2 border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 hover:bg-zinc-100 dark:hover:bg-zinc-900 text-zinc-700 dark:text-zinc-300 font-semibold text-[11px] uppercase tracking-wider py-2.5 rounded-lg active:scale-[0.98] transition-all duration-200"',
                    'class="w-full flex items-center justify-center gap-2 border border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-950 hover:bg-zinc-100 dark:hover:bg-zinc-900 text-zinc-700 dark:text-zinc-300 font-semibold text-[11px] uppercase tracking-wider py-2.5 rounded-[6px] active:scale-[0.98] transition-all duration-200"')

# --- 3. Main Spacing & Search Bar Border Radius ---
html = html.replace('pt-20 md:pt-28 pb-10 px-4 md:px-12', 'pt-14 md:pt-16 pb-10 px-4 md:px-12')
html = html.replace('rounded-xl px-4 py-3 shadow-sm focus-within:border-brand', 'rounded-[6px] px-4 py-3 shadow-sm focus-within:border-brand')

# --- 4. Filters with vertical line | and functional dropdowns ---
old_filters_area = """        <!-- 2. Horizontal Scroll Filter Pills -->
        <div class="w-full max-w-[48rem] mx-auto mb-6 overflow-x-auto scrollbar-none px-1 md:px-0">
          <div class="flex gap-2.5 pb-2 min-w-max">
            
            <!-- Filter Main Pill -->
            <button class="filter-pill flex items-center gap-1.5 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
              </svg>
              <span>Filters</span>
            </button>

            <!-- Country Pill -->
            <button class="filter-pill flex items-center gap-1 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <span>Country</span>
              <svg class="h-3 w-3 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Price Pill -->
            <button class="filter-pill flex items-center gap-1 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <span>Price</span>
              <svg class="h-3 w-3 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Year Pill -->
            <button class="filter-pill flex items-center gap-1 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <span>Year</span>
              <svg class="h-3 w-3 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

            <!-- Kilometres Pill -->
            <button class="filter-pill flex items-center gap-1 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <span>Kilometres</span>
            </button>

            <!-- Regional Specs Pill -->
            <button class="filter-pill flex items-center gap-1 px-4 py-2 border border-black/10 dark:border-white/10 rounded-full bg-white dark:bg-zinc-900 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-[12px] font-bold text-zinc-800 dark:text-zinc-200 transition-all duration-200 uppercase tracking-wider">
              <span>Regional Specs</span>
              <svg class="h-3 w-3 fill-current opacity-70" viewBox="0 0 24 24"><polygon points="6,9 12,15 18,9"/></svg>
            </button>

          </div>
        </div>"""

new_filters_area = """        <!-- 2. Horizontal Scroll Filter Pills -->
        <div class="w-full max-w-[48rem] mx-auto mb-6 flex items-center px-1 md:px-0">
          <!-- Filter Label -->
          <div class="flex items-center gap-1.5 text-zinc-800 dark:text-zinc-200 shrink-0">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-brand fill-none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <line x1="4" y1="21" x2="4" y2="14" /><line x1="4" y1="10" x2="4" y2="3" />
              <line x1="12" y1="21" x2="12" y2="12" /><line x1="12" y1="8" x2="12" y2="3" />
              <line x1="20" y1="21" x2="20" y2="16" /><line x1="20" y1="12" x2="20" y2="3" />
              <line x1="2" y1="14" x2="6" y2="14" />
              <line x1="10" y1="8" x2="14" y2="8" />
              <line x1="18" y1="16" x2="22" y2="16" />
            </svg>
            <span class="text-[13px] font-bold uppercase tracking-wider font-logo">Filters</span>
          </div>

          <!-- Vertical Divider -->
          <span class="h-5 w-px bg-zinc-300 dark:bg-zinc-850 mx-3 shrink-0">|</span>

          <!-- Scrolling Filter Pills Container -->
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

html = html.replace(old_filters_area, new_filters_area)

# --- 5. Card Container, Overlays, Sizing, SVGs ---
old_card_area = """          <!-- CARD 1: BUGATTI CHIRON -->
          <div class="listing-card bg-white dark:bg-zinc-900/40 border border-black/15 dark:border-white/10 rounded-2xl overflow-hidden shadow-card hover:shadow-card-hover transition-all duration-300 flex flex-col md:flex-row p-3 md:p-4 gap-4">
            
            <!-- Left Side: Image Gallery -->
            <div class="w-full md:w-[42%] shrink-0">
              <!-- Main Image Display -->
              <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-xl overflow-hidden group select-none border border-black/5 dark:border-white/5">
                <img src="assets/images/chiron.png" alt="Bugatti Chiron Super Sport"
                  class="main-car-img w-full h-full object-cover pointer-events-none transition-transform duration-500 group-hover:scale-[1.03]" />
                
                <!-- Overlay Badges -->
                <span class="absolute top-2.5 left-2.5 bg-brand text-white text-[9px] font-bold uppercase px-2.5 py-1 rounded-[6px] shadow-md tracking-wider">CAR OF THE WEEK</span>
                
                <div class="absolute top-2.5 right-2.5 flex items-center gap-2">
                  <!-- Share -->
                  <button class="bg-black/40 hover:bg-black/60 backdrop-blur-sm p-1.5 rounded-lg text-white active:scale-90 transition-all duration-200" aria-label="Share listing">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                      <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" y1="2" x2="12" y2="15"/>
                    </svg>
                  </button>
                  <!-- Favorite -->
                  <button class="fav-btn bg-black/40 hover:bg-black/60 backdrop-blur-sm p-1.5 rounded-lg text-white active:scale-90 transition-all duration-200" aria-label="Add to favorites">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 fav-heart stroke-current" fill="none" viewBox="0 0 24 24" stroke-width="2.5">
                      <path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- 3 Smaller Thumbnails underneath -->
              <div class="flex gap-2 mt-2 select-none">
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-lg overflow-hidden border border-brand dark:border-brand cursor-pointer transition-all duration-200">
                  <img src="assets/images/chiron.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 1" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-lg overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200">
                  <img src="assets/images/mercedes_one.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 2" />
                </div>
                <div class="thumb-wrapper flex-1 aspect-[3/2] rounded-lg overflow-hidden border border-black/10 dark:border-white/10 cursor-pointer hover:border-brand/40 transition-all duration-200 relative">
                  <img src="assets/images/ferrari_enzo.png" class="thumb-img w-full h-full object-cover bg-zinc-100 dark:bg-zinc-950 p-0.5" alt="Bugatti Chiron angle 3" />
                  <div class="absolute inset-0 bg-black/50 flex items-center justify-center text-white font-bold text-[10px] tracking-wide">+20</div>
                </div>
              </div>
            </div>"""

new_card_area = """          <!-- CARD 1: BUGATTI CHIRON -->
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
            </div>"""

html = html.replace(old_card_area, new_card_area)

# --- 6. Call & WhatsApp Buttons Size & SVG Icons ---
old_buttons_area = """                <!-- Call / WhatsApp Buttons -->
                <div class="flex items-center gap-2 w-full sm:w-auto shrink-0 select-none">
                  <a href="tel:+971500000000" class="flex-1 sm:flex-none border border-black/15 dark:border-white/15 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-900 dark:text-white rounded-[6px] px-4 py-2 font-bold text-xs uppercase active:scale-95 transition-all duration-300 flex items-center justify-center gap-1.5 h-9 shadow-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.94.725l.548 2.2a1 1 0 01-.321.988l-1.305.98a10.582 10.582 0 004.872 4.872l.98-1.305a1 1 0 01.988-.321l2.2.548a1 1 0 01.725.94V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                    </svg>
                    <span>Call</span>
                  </a>
                  <a href="https://wa.me/971500000000" target="_blank" class="flex-grow sm:flex-none bg-[#25D366] hover:bg-[#20ba59] text-white rounded-[6px] px-4 py-2 font-bold text-xs uppercase active:scale-95 transition-all duration-300 flex items-center justify-center gap-1.5 h-9 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.513 2.262 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.724-1.458L0 24zm5.835-3.321c1.605.952 3.123 1.488 4.703 1.489 5.485 0 9.948-4.464 9.951-9.95.002-2.658-1.03-5.155-2.906-7.03C15.767 3.313 13.275 2.28 10.61 2.28c-5.496 0-9.96 4.463-9.963 9.95-.001 1.761.47 3.477 1.362 5.006l-.974 3.56 3.654-.959c1.516.827 3.012 1.343 4.808 1.343zm11.98-7.79c-.294-.146-1.736-.857-2.006-.956-.269-.099-.465-.147-.659.146-.196.293-.755.955-.927 1.151-.171.196-.341.221-.635.074-.293-.146-1.242-.458-2.366-1.46-1.264-1.127-1.748-2.52-1.993-2.936-.245-.417-.026-.643.121-.788.132-.132.294-.342.441-.513.147-.171.196-.293.294-.489.098-.195.049-.367-.025-.513-.074-.147-.659-1.587-.903-2.172-.237-.57-.479-.493-.659-.502-.17-.008-.367-.01-.563-.01-.196 0-.513.073-.781.366-.269.293-1.028 1.002-1.028 2.443 0 1.44 1.051 2.834 1.198 3.03.147.195 2.068 3.158 5.01 4.437.699.304 1.246.486 1.671.621.703.223 1.342.192 1.847.117.564-.085 1.736-.71 1.98-.1.396 2.445-.636 1.736-1.393-.118-.171-.78-.293-1.029-.489"/></svg>
                    <span>WhatsApp</span>
                  </a>
                </div>"""

new_buttons_area = """                <!-- Call / WhatsApp Buttons -->
                <div class="flex items-center gap-2 w-full sm:w-auto shrink-0 select-none">
                  <a href="tel:+971500000000" class="flex-1 sm:flex-none border border-black/15 dark:border-white/15 hover:bg-zinc-100 dark:hover:bg-zinc-800 text-zinc-900 dark:text-white rounded-[6px] px-4 py-2 font-bold text-xs uppercase active:scale-95 transition-all duration-300 flex items-center justify-center gap-2 h-10 shadow-sm">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 stroke-current" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                    </svg>
                    <span>Call</span>
                  </a>
                  <a href="https://wa.me/971500000000" target="_blank" class="flex-1 sm:flex-none bg-[#25D366] hover:bg-[#20ba59] text-white rounded-[6px] px-4 py-2 font-bold text-xs uppercase active:scale-95 transition-all duration-300 flex items-center justify-center gap-2 h-10 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 fill-current" viewBox="0 0 448 512">
                      <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
                    </svg>
                    <span>WhatsApp</span>
                  </a>
                </div>"""

html = html.replace(old_buttons_area, new_buttons_area)

# --- 7. Bottom Script Logic (Filter Dropdown interaction & outside clicks) ---
old_js_filters = """      // 3. Filter Pill Active State Toggling
      const filterPills = document.querySelectorAll('.filter-pill');
      filterPills.forEach(pill => {
        pill.addEventListener('click', () => {
          pill.classList.toggle('bg-brand');
          pill.classList.toggle('text-white');
          pill.classList.toggle('border-brand');
          pill.classList.toggle('bg-white');
          pill.classList.toggle('dark:bg-zinc-900');
          pill.classList.toggle('text-zinc-800');
          pill.classList.toggle('dark:text-zinc-200');
          
          const svg = pill.querySelector('svg');
          if (svg) {
            svg.classList.toggle('text-white');
          }
        });
      });"""

new_js_filters = """      // 3. Filter Dropdown Toggle & Selection Logic
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

html = html.replace(old_js_filters, new_js_filters)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Listings refinements successfully applied!")
