def printPicnic(itemDict, leftWidth, rightWidth) :
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items() :
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'Apples': 2, 'Cookies': 8000, 'Cups': 4}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)