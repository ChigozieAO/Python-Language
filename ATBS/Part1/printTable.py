tableData = [['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

def printTable(tables) :
    colwidths = [0] * len(tableData)

    for col in range(len(tables)):
        for i in tables[col] :
            if len(i) > colwidths[col]:
                colwidths[col] = len(i)

    for row in range(len(tables[0])) :
        for col in range(len(tables)):
            print(tables[col][row].rjust(colwidths[col]), end=' ')
        print()


printTable(tableData)
       
    

