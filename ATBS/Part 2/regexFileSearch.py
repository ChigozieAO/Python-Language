import os, re

def Input_Folder():
    Search_Folder = input('Please provide a folder path:')
    FileList = os.listdir(Search_Folder)
    Search_Regex = input('Please provide a regex to search for:')
    RegexCompile = re.compile(Search_Regex)
    
    
    for file in FileList:
        
        if file.endswith('.txt'):
            # changed to full path 
            full_path = os.path.join(Search_Folder, file)
            print(full_path)   
            
            count = 0
            with open(full_path, 'r') as f:
                txt_filecontent = f.read()
                match = re.search(RegexCompile, txt_filecontent)
                if match:
                    count += 1
            print('There were ' + str(count) + ' matches of your regex found.')

Input_Folder()