import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/brands.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- Replace the old brand grid with 16 high-definition logo cards ---
old_grid_start = '        <!-- Brands Selection Grid (Same width / height items with 12px border radius) -->'
old_grid_end = '        </div>\n\n      </div>\n    </section>'

# Let's locate the grid block and replace it cleanly
grid_index = html.find(old_grid_start)
if grid_index != -1:
    before_grid = html[:grid_index]
    after_grid_index = html.find('<!-- NATIVE STICKY BOTTOM NAVIGATION', grid_index)
    after_grid = html[after_grid_index:]
    
    new_grid_content = """        <!-- Brands Selection Grid (Same width / height items with 12px border radius) -->
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 md:gap-5 w-full select-none">
          
          <!-- BRAND 1: BUGATTI (Active -> Links to listings.html?brand=bugatti) -->
          <a href="listings.html?brand=bugatti" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/bugatti-logo.png" class="w-full h-full object-contain" alt="Bugatti Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">BUGATTI</span>
          </a>

          <!-- BRAND 2: FERRARI -->
          <a href="listings.html?brand=ferrari" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/ferrari-logo.png" class="w-full h-full object-contain" alt="Ferrari Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">FERRARI</span>
          </a>

          <!-- BRAND 3: LAMBORGHINI -->
          <a href="listings.html?brand=lamborghini" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/lamborghini-logo.png" class="w-full h-full object-contain" alt="Lamborghini Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">LAMBORGHINI</span>
          </a>

          <!-- BRAND 4: KOENIGSEGG -->
          <a href="listings.html?brand=koenigsegg" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/koenigsegg-logo.png" class="w-full h-full object-contain" alt="Koenigsegg Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">KOENIGSEGG</span>
          </a>

          <!-- BRAND 5: PAGANI -->
          <a href="listings.html?brand=pagani" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/pagani-logo.png" class="w-full h-full object-contain" alt="Pagani Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">PAGANI</span>
          </a>

          <!-- BRAND 6: PORSCHE -->
          <a href="listings.html?brand=porsche" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/porsche-logo.png" class="w-full h-full object-contain" alt="Porsche Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">PORSCHE</span>
          </a>

          <!-- BRAND 7: MCLAREN -->
          <a href="listings.html?brand=mclaren" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/mclaren-logo.png" class="w-full h-full object-contain" alt="McLaren Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">McLAREN</span>
          </a>

          <!-- BRAND 8: ASTON MARTIN -->
          <a href="listings.html?brand=astonmartin" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/aston-martin-logo.png" class="w-full h-full object-contain" alt="Aston Martin Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">ASTON MARTIN</span>
          </a>

          <!-- BRAND 9: MASERATI -->
          <a href="listings.html?brand=maserati" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/maserati-logo.png" class="w-full h-full object-contain" alt="Maserati Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">MASERATI</span>
          </a>

          <!-- BRAND 10: BENTLEY -->
          <a href="listings.html?brand=bentley" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/bentley-logo.png" class="w-full h-full object-contain" alt="Bentley Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">BENTLEY</span>
          </a>

          <!-- BRAND 11: ROLLS-ROYCE -->
          <a href="listings.html?brand=rollsroyce" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/rolls-royce-logo.png" class="w-full h-full object-contain" alt="Rolls-Royce Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">ROLLS-ROYCE</span>
          </a>

          <!-- BRAND 12: MERCEDES-BENZ -->
          <a href="listings.html?brand=mercedesbenz" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/mercedes-benz-logo.png" class="w-full h-full object-contain" alt="Mercedes-Benz Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">MERCEDES-BENZ</span>
          </a>

          <!-- BRAND 13: BMW -->
          <a href="listings.html?brand=bmw" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/bmw-logo.png" class="w-full h-full object-contain" alt="BMW Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">BMW</span>
          </a>

          <!-- BRAND 14: AUDI -->
          <a href="listings.html?brand=audi" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/audi-logo.png" class="w-full h-full object-contain" alt="Audi Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">AUDI</span>
          </a>

          <!-- BRAND 15: LOTUS -->
          <a href="listings.html?brand=lotus" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/lotus-logo.png" class="w-full h-full object-contain" alt="Lotus Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">LOTUS</span>
          </a>

          <!-- BRAND 16: RIMAC -->
          <a href="listings.html?brand=rimac" class="group flex flex-col items-center justify-center p-4 md:p-5 bg-white dark:bg-zinc-900/40 border border-black/[0.08] dark:border-white/10 rounded-[12px] hover:border-brand/40 hover:shadow-card transition-all duration-300 cursor-pointer">
            <div class="h-20 w-20 md:h-28 md:w-28 flex items-center justify-center bg-white rounded-[12px] p-2.5 transition-all duration-300 group-hover:scale-105 border border-black/5 shadow-sm">
              <img src="https://www.carlogos.org/car-logos/rimac-logo.png" class="w-full h-full object-contain" alt="Rimac Logo" />
            </div>
            <span class="text-[10px] font-bold tracking-widest text-zinc-400 dark:text-zinc-500 uppercase mt-3.5 group-hover:text-brand transition-colors duration-200">RIMAC</span>
          </a>

        </div>
      </div>
    </section>"""
    
    updated_html = before_grid + new_grid_content + after_grid
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_html)
    
    print("16 Supercar logos with expanded image dimensions generated in brands.html successfully!")
else:
    print("Error: Could not find old grid start point in brands.html")
