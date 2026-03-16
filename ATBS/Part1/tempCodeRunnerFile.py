#! python3
# pw.py - An insecure password locker

PASSWORDS = {'email': 'B448F4HU83EU83U383HF8', 'blog': '7AU4XND2I39RI030O0CE02IX9', 'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2 :
    print('Usage: python pw-py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else: 
    print('There is no account name: ' + account)