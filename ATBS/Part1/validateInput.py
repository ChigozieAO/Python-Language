while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal() :
        break
    else:
        print('Enter a valid age please ( numbers only)')
while True: 
    print('Enter your password')
    password = input()
    if password.isalnum() :
        break
    else :
        print('Enter a valid password goddamnit (letters and numbers only)')