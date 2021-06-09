def displayInventory(inventory):
    total = 0
    print("Inventory: ")
    for k,v in inventory.items():
        print( str(v) + " " + str(k))
        total+=v
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if(addedItems[i] in inventory.keys()):
            inventory[addedItems[i]]+=1
        else:
            inventory.setdefault(addedItems[i], 1)




inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']




    
        
