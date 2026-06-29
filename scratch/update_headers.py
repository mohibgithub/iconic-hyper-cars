import os

listings_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"
details_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/details.html"

# --- 1. Modify listings.html header ---
with open(listings_path, "r", encoding="utf-8") as f:
    listings_html = f.read()

old_listings_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-zinc-950 dark:bg-zinc-950/80 backdrop-blur-md px-4 py-4 md:py-5 border-b border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-center relative">
        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>"""

new_listings_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-white dark:bg-zinc-950 px-4 py-4 md:py-5 border-b border-black/[0.06] dark:border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-center relative">
        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-zinc-950 dark:text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>"""

listings_html = listings_html.replace(old_listings_header, new_listings_header)

with open(listings_path, "w", encoding="utf-8") as f:
    f.write(listings_html)


# --- 2. Modify details.html header ---
with open(details_path, "r", encoding="utf-8") as f:
    details_html = f.read()

old_details_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-zinc-950 dark:bg-zinc-950/80 backdrop-blur-md px-4 py-4 md:py-5 border-b border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-center relative">
        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>"""

new_details_header = """    <!-- MAIN HEADER SECTION -->
    <header
      class="main-header absolute top-0 left-0 right-0 z-40 bg-white dark:bg-zinc-950 px-4 py-4 md:py-5 border-b border-black/[0.06] dark:border-white/5 transition-colors duration-300 shrink-0">
      <div class="max-w-[100rem] mx-auto w-full flex items-center justify-center relative">
        <a href="index.html" class="flex flex-col items-center text-center select-none font-logo group">
          <span
            class="text-[16.4px] md:text-1xl font-extrabold tracking-widest text-zinc-950 dark:text-white transition-colors font-iconic">ICONIC</span>
          <span
            class="text-[10px] md:text-[13px] font-bold tracking-wider text-brand transition-colors uppercase -mt-0.5 md:mt-0 font-montserrat">HYPERCARS</span>
        </a>"""

details_html = details_html.replace(old_details_header, new_details_header)

with open(details_path, "w", encoding="utf-8") as f:
    f.write(details_html)

print("Dynamic themed headers applied to listings.html and details.html subpages successfully!")
