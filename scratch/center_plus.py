import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Replace the bottom nav container to use grid grid-cols-5 layout instead of flex justify-around ---
# Old:
# <nav class="fixed bottom-0 left-0 right-0 z-50 bg-white/90 dark:bg-zinc-900/90 backdrop-blur-md border-t border-black/[0.08] dark:border-white/10 md:hidden flex items-center justify-around h-16 px-4 shadow-lg select-none">
html = html.replace(
    '<nav class="fixed bottom-0 left-0 right-0 z-50 bg-white/90 dark:bg-zinc-900/90 backdrop-blur-md border-t border-black/[0.08] dark:border-white/10 md:hidden flex items-center justify-around h-16 px-4 shadow-lg select-none">',
    '<nav class="fixed bottom-0 left-0 right-0 z-50 bg-white/90 dark:bg-zinc-900/90 backdrop-blur-md border-t border-black/[0.08] dark:border-white/10 md:hidden grid grid-cols-5 items-center h-16 px-1 shadow-lg select-none">'
)

# --- 2. Make each navigation element have w-full to align correctly inside its column ---
# Home link replacement:
# Old:
# <a href="index.html" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">
html = html.replace(
    '<a href="index.html" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">',
    '<a href="index.html" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1 w-full text-center">'
)

# Favorites link replacement:
# Old:
# <a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">
html = html.replace(
    '<a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">',
    '<a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1 w-full text-center">'
)

# Plus button link & div replacement (change h-13 w-13 p-3 to h-14 w-14 flex items-center justify-center):
old_plus_button = """      <!-- Highlighted Place Ad (Center Button) -->
      <a href="listings.html" class="flex flex-col items-center justify-center -translate-y-4 shrink-0 relative select-none" aria-label="Place an ad">
        <div class="h-13 w-13 p-3 bg-brand text-white rounded-full flex items-center justify-center shadow-lg hover:scale-105 active:scale-95 transition-all duration-200 border-4 border-zinc-50 dark:border-zinc-950">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current" fill="none" viewBox="0 0 24 24" stroke-width="3">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </div>
      </a>"""

new_plus_button = """      <!-- Highlighted Place Ad (Center Button) -->
      <a href="listings.html" class="flex flex-col items-center justify-center -translate-y-4 shrink-0 relative select-none w-full" aria-label="Place an ad">
        <div class="h-14 w-14 bg-brand text-white rounded-full flex items-center justify-center shadow-lg hover:scale-105 active:scale-95 transition-all duration-200 border-4 border-zinc-50 dark:border-zinc-950">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 stroke-current" fill="none" viewBox="0 0 24 24" stroke-width="3">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </div>
      </a>"""

html = html.replace(old_plus_button, new_plus_button)

# Chats link replacement:
# Old:
#       <!-- Chats tab -->
#       <a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">
html = html.replace(
    '      <!-- Chats tab -->\n      <a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">',
    '      <!-- Chats tab -->\n      <a href="#" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1 w-full text-center">'
)

# Menu button replacement:
# Old:
#       <!-- Menu tab (Triggers standard drawer) -->
#       <button popovertarget="mobile-menu" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">
html = html.replace(
    '      <!-- Menu tab (Triggers standard drawer) -->\n      <button popovertarget="mobile-menu" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1">',
    '      <!-- Menu tab (Triggers standard drawer) -->\n      <button popovertarget="mobile-menu" class="flex flex-col items-center justify-center text-zinc-400 dark:text-zinc-500 hover:text-zinc-800 dark:hover:text-zinc-200 transition-colors duration-200 py-1 w-full text-center">'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Bottom navigation centered plus button layouts applied successfully!")
