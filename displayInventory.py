stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    itemNumber = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        itemNumber += v
    print('Total number of items: ' + str(itemNumber))

def addToInventory(inventory, addedItems):
    for item in range(len(addedItems)):
        inventory.setdefault(addedItems[item], 0)
        inventory[addedItems[item]] += 1
        
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
        
