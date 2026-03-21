#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
#   python mcb.pyw <keyword>            - Loads keyword to clipboard.
#   python mcb.pyw save <keyword>       - Saves clipboard to keyword.
#   python mcb.pyw list                 - Loads all keywords to clipboard.
#   python mcb.pyw delete <keyword>     - Deletes one keyword.
#   python mcb.pyw deleteall            - Deletes ALL saved keywords (asks for confirmation).

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

# Delete one keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    keyword = sys.argv[2]
    if keyword in mcbShelf:
        del mcbShelf[keyword]
        print(f"Deleted keyword: {keyword}")
    else:
        print(f"Keyword '{keyword}' not found.")

# Delete all keywords
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'deleteall':
    if len(mcbShelf) == 0:
        print("Nothing to delete (shelf is already empty).")
    else:
        confirm = input(f"Are you sure you want to delete ALL {len(mcbShelf)} items? (yes/no): ").strip().lower()
        if confirm in ('yes', 'y'):
            mcbShelf.clear()
            print("All keywords deleted.")
        else:
            print("Delete all cancelled.")

# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        keys = list(mcbShelf.keys())
        if keys:
            pyperclip.copy('\n'.join(keys))
            print("Keywords copied to clipboard:")
            print(', '.join(keys))
        else:
            print("No keywords saved yet.")
            pyperclip.copy("")
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f"Content for '{sys.argv[1]}' copied to clipboard.")
    else:
        print(f"Keyword '{sys.argv[1]}' not found.")

mcbShelf.close()