import os

listings_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"
details_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/details.html"

# --- 1. Modify listings.html main display border ---
with open(listings_path, "r", encoding="utf-8") as f:
    listings_html = f.read()

# Old:
# <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">
listings_html = listings_html.replace(
    '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/5 dark:border-white/5">',
    '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-950 rounded-[6px] overflow-hidden group select-none border border-black/10 dark:border-white/10">'
)

with open(listings_path, "w", encoding="utf-8") as f:
    f.write(listings_html)


# --- 2. Modify details.html main display border and border radius ---
with open(details_path, "r", encoding="utf-8") as f:
    details_html = f.read()

# Old:
# <div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-900 rounded-[12px] overflow-hidden border border-black/10 dark:border-white/10 select-none shadow-sm">
details_html = details_html.replace(
    '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-900 rounded-[12px] overflow-hidden border border-black/10 dark:border-white/10 select-none shadow-sm">',
    '<div class="relative w-full aspect-[3/2] bg-zinc-100 dark:bg-zinc-900 rounded-[6px] overflow-hidden border border-black/10 dark:border-white/10 select-none shadow-sm">'
)

with open(details_path, "w", encoding="utf-8") as f:
    f.write(details_html)

print("Standardized border radius (rounded-[6px]) and border color weights applied to all images successfully!")
