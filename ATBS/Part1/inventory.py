knapSack = {'Sword': 9, 'War-Axe': 2, 'Gold': 75, 'Potions': 20, 'Food': 12, 'Armor': 8, 'Spells': 6}
dragonLoot = ['Gold', 'Ruby', 'Gold', 'Dagger', 'Gold']

def inventory(inventory) :
    print('Inventory :')
    totalItems = 0
    for k, v in inventory.items() :
        print(str(v) + '  ' + k)
        totalItems += v
    print('Total number of loot is : ' +str(totalItems))

def addInventory(inventory, added) :
    for item in added :
        if item in inventory:
            inventory[item] += 1
        else :
            inventory[item] = 1
    


inventory(knapSack)
addInventory(knapSack, dragonLoot)
inventory(knapSack)