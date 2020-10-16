inventory = {
    'arrow': 1,
    'gold coin': 2,
    'rope': 3,
    'torch': 0,
    'dagger': 5
}

def logInventory(inventory):
    total_items = 0
    for item, quantity in inventory.items():
        print(str(quantity)+' '+item)
        total_items += quantity
    print("Total number of items: "+str(total_items))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInv(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item,0)
            inventory[item] += 1
    
    logInventory(inventory)

addToInv(inventory, dragonLoot)


# logInventory(inventory)