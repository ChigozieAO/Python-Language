import os, re

NewFile = input('Please enter the path of the file to be used: ')
NewFilepath = os.path.abspath(NewFile)
print(NewFilepath)

if os.path.exists(NewFilepath):
    print("File exists.")
    mode = 'r' 
else:
    print('This file does not exist. Creating a new file.')
    mode = 'w'

# Open once and keep the file object
with open(NewFile, mode) as file:
    if mode == 'w':
        file.write("")  # empty file
        NewFileContent = ""
    else:
        NewFileContent = file.read()

def NewMadLibs(text):
    SpeechParts = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)', re.I)
    
    # Find all placeholders
    placeholders = SpeechParts.findall(text)
    
    result = text
    for placeholder in placeholders:
        placeholder = placeholder.upper() 
        if placeholder == 'ADJECTIVE':
            word = input('Enter an adjective:\n')
        elif placeholder == 'NOUN':
            word = input('Enter a noun:\n')
        elif placeholder == 'ADVERB':
            word = input('Enter an adverb:\n')
        elif placeholder == 'VERB':
            word = input('Enter a verb:\n')
        else:
            continue
        
        # Replace one occurrence at a time
        result = SpeechParts.sub(word, result, count=1)

    return result

# Run mad libs
filled_text = NewMadLibs(NewFileContent)

# Show result
print("\nResult:\n")
print(filled_text)

# Save to new file
new_FileName = 'new_source.txt'
with open(new_FileName, 'w') as new_file:
    new_file.write(filled_text)

print("The file is saved as 'new_source.txt'")