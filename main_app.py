from items import *
from inventory import Inventory

weapon = Weapon(name="Bandook", description="old world war gun", power="45 mm bullets")
weapon_1 = Weapon(name="sword", description="Japanese Katana", power="very sharp")

inventory = Inventory()

inventory.add(weapon)
inventory.add(weapon_1)

print(len(inventory))


for items in inventory:
    print(items.name)
