catNames = []

while True:
    print('Enter the name of Cat ' + str(len(catNames) + 1) + ' ( Or enter to stop.):' )
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames :
    print(" " + name)