import os

index_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/index.html"
listings_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"
details_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/details.html"

# Helper function to replace padding in a file content
def reduce_paddings(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Define simple string replacements to halve the horizontal gutters (50% reduction):
    # px-4 -> px-2
    # md:px-12 -> md:px-6
    # px-12 -> px-6
    
    # Let's perform precise replacements based on actual class usage:
    replacements = [
        # 1. Main sections
        ('pb-10 px-4 md:px-12', 'pb-10 px-2 md:px-6'),
        ('py-10 px-4 md:py-12 md:px-12', 'py-10 px-2 md:py-12 md:px-6'),
        ('py-10 px-4 md:px-12', 'py-10 px-2 md:px-6'),
        ('border-t border-zinc-100 dark:border-zinc-800 py-10 px-4 md:py-12 md:px-12', 'border-t border-zinc-100 dark:border-zinc-800 py-10 px-2 md:py-12 md:px-6'),
        ('border-t border-zinc-150 dark:border-zinc-800 py-10 px-4 md:py-12 md:px-12', 'border-t border-zinc-150 dark:border-zinc-800 py-10 px-2 md:py-12 md:px-6'),
        
        # 2. Footers & Headers
        ('px-4 md:px-12 border-b border-black/[0.08] dark:border-white/[0.1]', 'px-2 md:px-6 border-b border-black/[0.08] dark:border-white/[0.1]'),
        ('max-w-[100rem] px-4 md:px-12 py-12', 'max-w-[100rem] px-2 md:px-6 py-12'),
        ('px-4 py-4 md:py-6 md:px-12 flex items-center justify-between transition-colors duration-300', 'px-2 py-4 md:py-6 md:px-6 flex items-center justify-between transition-colors duration-300'),
        ('px-4 md:px-12 py-4 border-b shadow-xl', 'px-2 md:px-6 py-4 border-b shadow-xl'),
        ('bg-white dark:bg-zinc-950 px-4 py-4 md:py-5 border-b border-black/[0.06] dark:border-white/5', 'bg-white dark:bg-zinc-950 px-2 py-4 md:py-5 border-b border-black/[0.06] dark:border-white/5'),
        
        # 3. Other minor occurrences
        ('w-full max-w-[48rem] mx-auto mt-2 mb-4 px-1 md:px-0', 'w-full max-w-[48rem] mx-auto mt-2 mb-4 px-0.5 md:px-0'),
        ('w-full max-w-[48rem] mx-auto mb-6 flex items-center justify-start md:justify-center px-1 md:px-0', 'w-full max-w-[48rem] mx-auto mb-6 flex items-center justify-start md:justify-center px-0.5 md:px-0'),
        ('w-full max-w-[48rem] mx-auto mb-6 px-1 md:px-0', 'w-full max-w-[48rem] mx-auto mb-6 px-0.5 md:px-0'),
        ('detail-body-container pt-16 md:pt-20 pb-10 px-4 md:px-12', 'detail-body-container pt-16 md:pt-20 pb-10 px-2 md:px-6'),
        ('pt-16 md:pt-20 pb-10 px-4 md:px-12', 'pt-16 md:pt-20 pb-10 px-2 md:px-6'),
    ]

    initial_len = len(content)
    replaced_count = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            replaced_count += 1
            
    # Also do generic replace for leftover px-4 md:px-12
    if 'px-4 md:px-12' in content:
        content = content.replace('px-4 md:px-12', 'px-2 md:px-6')
        replaced_count += 1

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Processed {os.path.basename(file_path)}: Applied {replaced_count} layout padding replacements.")

reduce_paddings(index_path)
reduce_paddings(listings_path)
reduce_paddings(details_path)

print("Horizontal padding reduction by 50% successfully applied globally!")
