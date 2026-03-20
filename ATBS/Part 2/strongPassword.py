import re

passwordRegex = re.compile(r'''(
                           ^(?=.*[a-z])                 # At least one lowercase letter
                           (?=.*[A-Z])                  # At least one Uppercase letter
                           (?=.*\d)                     # At least one digit
                           (?=.*[!@#$%^&*()_+\-=\[\]{}|;:'",.<>?/`~])   # At least one special character
                           .{8,}                        # Minimum of 8 characters
                           $
                           )''', re.VERBOSE)

password = input()

def strongPassword(password):
    while True:
        matches = passwordRegex.search(password)
        if matches:
            print('That is one Strong password')
            break
        else:
            print('input a strong password please')
            password = input('Try again: ')

strongPassword(password)