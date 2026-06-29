import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/brands.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- Replace Brand Logos Grid in brands.html with image URLs and white badge backing ---
old_grid = """        <!-- Brands Selection Grid (Same width / height items with 12px border radius) -->
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 md:gap-5 w-full select-none">
          
          <!-- BRAND 1: BUGATTI (Active -> Links to listings.html?brand=bugatti) -->
          <a href="listings.html?brand=bugatti" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Bugatti Red Oval Stylized SVG -->
              <svg viewBox="0 0 100 60" class="w-full h-full object-contain">
                <ellipse cx="50" cy="30" rx="46" ry="26" fill="#bc1919" stroke="#ffffff" stroke-width="2"/>
                <text x="50" y="38" font-family="'Montserrat', sans-serif" font-weight="900" font-size="14" fill="#ffffff" text-anchor="middle" letter-spacing="1">BUGATTI</text>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">BUGATTI</span>
          </a>

          <!-- BRAND 2: FERRARI -->
          <a href="listings.html?brand=ferrari" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Ferrari Yellow Shield Stylized SVG -->
              <svg viewBox="0 0 60 80" class="w-full h-full object-contain">
                <path d="M5,10 C5,10 5,60 30,75 C55,60 55,10 55,10 Z" fill="#ffeb3b" stroke="#000000" stroke-width="1.5"/>
                <!-- Prancing Horse silhouette -->
                <path d="M26,22 C26,22 28,18 28,14 C28,10 26,10 26,10 C26,10 32,12 30,18 C28,24 34,26 34,32 C34,38 31,42 27,45 C27,45 32,55 35,62 C35,62 31,64 28,57 C25,50 24,42 24,42 L21,55 L18,52 L22,38 C22,38 18,34 16,36 C14,38 15,44 15,44 C15,44 11,36 14,28 C17,20 22,25 24,24 Z" fill="#000000"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">FERRARI</span>
          </a>

          <!-- BRAND 3: LAMBORGHINI -->
          <a href="listings.html?brand=lamborghini" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Lamborghini Shield Stylized SVG -->
              <svg viewBox="0 0 60 70" class="w-full h-full object-contain">
                <path d="M5,5 C15,2 45,2 55,5 C55,5 58,45 30,65 C2,45 5,5 5,5 Z" fill="#18181b" stroke="#d4af37" stroke-width="2"/>
                <path d="M30,10 L15,35 L25,35 L20,55 L45,25 L33,25 Z" fill="#d4af37"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">LAMBORGHINI</span>
          </a>

          <!-- BRAND 4: KOENIGSEGG -->
          <a href="listings.html?brand=koenigsegg" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Koenigsegg Gold-Orange Shield Stylized SVG -->
              <svg viewBox="0 0 60 75" class="w-full h-full object-contain">
                <path d="M5,5 L55,5 C55,5 58,40 30,70 C2,40 5,5 5,5 Z" fill="#bc1919" stroke="#d4af37" stroke-width="2"/>
                <g fill="#ffeb3b">
                  <polygon points="15,15 30,30 45,15 30,10"/>
                  <polygon points="15,35 30,50 45,35 30,30"/>
                  <polygon points="15,55 30,65 45,55 30,50"/>
                </g>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">KOENIGSEGG</span>
          </a>

          <!-- BRAND 5: PAGANI -->
          <a href="listings.html?brand=pagani" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Pagani Minimalist Oval Badge SVG -->
              <svg viewBox="0 0 80 50" class="w-full h-full object-contain">
                <rect x="5" y="5" width="70" height="40" rx="20" fill="#27272a" stroke="#d4af37" stroke-width="2"/>
                <text x="40" y="31" font-family="'Montserrat', sans-serif" font-weight="900" font-size="16" fill="#d4af37" text-anchor="middle" letter-spacing="2">PAGANI</text>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">PAGANI</span>
          </a>

          <!-- BRAND 6: PORSCHE -->
          <a href="listings.html?brand=porsche" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Porsche Gold Shield Stylized SVG -->
              <svg viewBox="0 0 60 70" class="w-full h-full object-contain">
                <path d="M5,5 C10,5 50,5 55,5 C55,5 56,42 30,65 C4,42 5,5 5,5 Z" fill="#d4af37" stroke="#000000" stroke-width="1.5"/>
                <rect x="15" y="15" width="10" height="15" fill="#000000"/>
                <rect x="35" y="15" width="10" height="15" fill="#bc1919"/>
                <rect x="15" y="35" width="10" height="15" fill="#bc1919"/>
                <rect x="35" y="35" width="10" height="15" fill="#000000"/>
                <circle cx="30" cy="30" r="6" fill="#d4af37"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">PORSCHE</span>
          </a>

          <!-- BRAND 7: MCLAREN -->
          <a href="listings.html?brand=mclaren" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- McLaren Typography Speedmark SVG -->
              <svg viewBox="0 0 100 50" class="w-full h-full object-contain">
                <text x="10" y="32" font-family="'Montserrat', sans-serif" font-weight="900" font-size="16" fill="#bc1919" letter-spacing="0.5">McLAREN</text>
                <path d="M85,15 C95,20 95,30 80,30 C75,30 82,22 85,15 Z" fill="#ff9800"/>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">McLAREN</span>
          </a>

          <!-- BRAND 8: ASTON MARTIN -->
          <a href="listings.html?brand=astonmartin" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-zinc-50 dark:bg-zinc-950/60 rounded-[12px] p-2 transition-all duration-300 group-hover:scale-105">
              <!-- Aston Martin Wings Stylized SVG -->
              <svg viewBox="0 0 100 40" class="w-full h-full object-contain">
                <path d="M5,20 C35,10 65,10 95,20 C85,25 15,25 5,20 Z" fill="#2e7d32" stroke="#ffffff" stroke-width="1"/>
                <line x1="50" y1="12" x2="50" y2="28" stroke="#ffffff" stroke-width="1.5"/>
                <line x1="25" y1="17" x2="75" y2="17" stroke="#ffffff" stroke-width="1.5"/>
                <text x="50" y="24" font-family="'Montserrat', sans-serif" font-weight="800" font-size="6" fill="#ffffff" text-anchor="middle">ASTON MARTIN</text>
              </svg>
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">ASTON MARTIN</span>
          </a>

        </div>"""

new_grid = """        <!-- Brands Selection Grid (Same width / height items with 12px border radius) -->
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 md:gap-5 w-full select-none">
          
          <!-- BRAND 1: BUGATTI (Active -> Links to listings.html?brand=bugatti) -->
          <a href="listings.html?brand=bugatti" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/bugatti-logo.png" class="w-full h-full object-contain" alt="Bugatti Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">BUGATTI</span>
          </a>

          <!-- BRAND 2: FERRARI -->
          <a href="listings.html?brand=ferrari" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/ferrari-logo.png" class="w-full h-full object-contain" alt="Ferrari Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">FERRARI</span>
          </a>

          <!-- BRAND 3: LAMBORGHINI -->
          <a href="listings.html?brand=lamborghini" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/lamborghini-logo.png" class="w-full h-full object-contain" alt="Lamborghini Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">LAMBORGHINI</span>
          </a>

          <!-- BRAND 4: KOENIGSEGG -->
          <a href="listings.html?brand=koenigsegg" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/koenigsegg-logo.png" class="w-full h-full object-contain" alt="Koenigsegg Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">KOENIGSEGG</span>
          </a>

          <!-- BRAND 5: PAGANI -->
          <a href="listings.html?brand=pagani" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/pagani-logo.png" class="w-full h-full object-contain" alt="Pagani Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">PAGANI</span>
          </a>

          <!-- BRAND 6: PORSCHE -->
          <a href="listings.html?brand=porsche" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/porsche-logo.png" class="w-full h-full object-contain" alt="Porsche Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">PORSCHE</span>
          </a>

          <!-- BRAND 7: MCLAREN -->
          <a href="listings.html?brand=mclaren" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/mclaren-logo.png" class="w-full h-full object-contain" alt="McLaren Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">McLAREN</span>
          </a>

          <!-- BRAND 8: ASTON MARTIN -->
          <a href="listings.html?brand=astonmartin" class="group flex flex-col items-center justify-center p-6 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-16 w-16 md:h-20 md:w-20 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/aston-martin-logo.png" class="w-full h-full object-contain" alt="Aston Martin Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-4 group-hover:text-brand transition-colors duration-200">ASTON MARTIN</span>
          </a>

        </div>"""

html = html.replace(old_grid, new_grid)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("HD PNG Brand logo images from carlogos.org integrated successfully!")
