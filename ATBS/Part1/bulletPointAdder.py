#! python3
# bulletPointAdder.py - adds bullet point to wikis


import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)) :
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)