birthdays = { "Alice": "Apr 1", "Bob": "Mar 6", "Sam": "Jun 19"}

while True :
    print("Enter a name: (blank to quit)")
    name = input()
    if name == '':
        break
    if name in birthdays :
        print(birthdays[name] + ' is the birthday of ' + name)
    else :
        print('I do not have birthday information for ' + name)
        print('What is there birthday? ')
        bday = input()
        birthdays[name] = bday
        print('Database updated')