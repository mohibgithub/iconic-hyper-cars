import os

file_path = "/Users/mohdmohib/Documents/Client/iconic-hyper-cars/listings.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# --- 1. Replace Javascript dropdown positioning logic with boundary checks ---
old_js_pos = """          if (isCurrentlyHidden) {
            // Position the menu dynamically below the button in absolute coordinates
            const rect = item.btn.getBoundingClientRect();
            item.menu.style.top = `${rect.bottom + window.scrollY + 6}px`;
            item.menu.style.left = `${rect.left + window.scrollX}px`;
            item.menu.classList.remove('hidden');
          }"""

new_js_pos = """          if (isCurrentlyHidden) {
            // Position the menu dynamically below the button in absolute coordinates
            const rect = item.btn.getBoundingClientRect();
            
            // Temporarily unhide to measure actual offset width
            item.menu.classList.remove('hidden');
            const menuWidth = item.menu.offsetWidth || 160;
            item.menu.classList.add('hidden');
            
            const viewportWidth = window.innerWidth;
            let leftPos = rect.left + window.scrollX;
            
            // Align dropdown right-edge to button right-edge if it overflows screen boundaries
            if (rect.left + menuWidth > viewportWidth) {
              leftPos = rect.right + window.scrollX - menuWidth - 4; // 4px padding offset
            }
            
            // Guard left viewport boundary
            if (leftPos < 8) {
              leftPos = 8;
            }
            
            item.menu.style.top = `${rect.bottom + window.scrollY + 6}px`;
            item.menu.style.left = `${leftPos}px`;
            item.menu.classList.remove('hidden');
          }"""

html = html.replace(old_js_pos, new_js_pos)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Responsive overflow positioning for filter dropdowns applied successfully!")
