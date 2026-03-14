myPets = ['Bigfoot', 'fat', 'Ate']

print('Enter a pet name: ')
name = input()
if name not in myPets :
    print('I have no such pet')
else: 
    print(name + ' is my pet')