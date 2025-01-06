from gameinfo import GameInfo
from room import Room
from character import Character, Enemy
from item import Item

import os
import time

GAMEINFO = GameInfo()
GAMEINFO.welcome()


def capitaliseFirstLetter(str):
    ls = list(str)
    ls[0] = ls[0].upper()
    return ''.join(ls)


def clearScreen(duration=0):
    time.sleep(duration)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# ================
# LAYING OUT ROOMS
# ================
corridor = Room('The Abandoned Hall')
corridor._description = 'A dimly lit corridor with cobwebs hanging from the walls. The air smells of mildew and decay. Faint whispers can be heard echoing.'

library = Room('The Forgotten Library')
library._description = 'A massive library filled with dusty, ancient books. The shelves are teeming with forgotten knowledge, and strange symbols are etched into the floor.'

kitchen = Room('The Kitchen')
kitchen._description = 'A spacious kitchen with a rustic charm. Wooden cabinets line the walls, filled with dusty jars and dried herbs. A large stove sits in the corner, with a pot simmering on top.'

attic = Room('The Old Attic')
attic._description = 'Worn stairs lead to this lofty area. Moss crawled up the walls and the window panes rattled, sensing your presence.'

garden = Room('The Overgrown Garden')
garden._description = 'Although there were scattered shrubs and a large oak tree, the garden appeared desolate and grey. Howls of the wind beckoned you.'

# =============
# LINKING ROOMS
# =============
corridor.link_room(library, 'west')
corridor.link_room(kitchen, 'east')

library.link_room(corridor, 'east')
library.link_room(attic, 'south')

kitchen.link_room(corridor, 'west')
kitchen.link_room(garden, 'north')

attic.link_room(library, 'north')

garden.link_room(kitchen, 'south')

# =================
# ADDING CHARACTERS
# =================

# FRIENDLY
owl = Character('The Wise Owl', 'A majestic owl with piercing eyes.')
owl.conversation = 'Knowledge is power. But power comes at a price.'
library._character = owl
owl.bribe_item = 'Shiny Coin'
owl.bribe_info = 'She needs comforting. She needs a friend.'


gnome = Character('Gnome Gardener',
                  'A small, bearded gnome with a green thumb.')
gnome.conversation = 'The garden is my domain. Tread carefully, stranger.'
garden._character = gnome
gnome.bribe_item = 'Rusty Coin'
gnome.bribe_info = "A glimmer of gold will outshine greed. What is soft in hand can strike with might, where hunger dares to tread. Seek the shimmer in the heart of the kitchen, and the goblin's grasp shall loosen."

# ENEMIES
goblin = Enemy('Greedy Goblin', 'A small, green-skinned creature with sharp teeth.')
goblin.weakness = 'Golden Spoon'
kitchen._character = goblin

doll = Enemy('Creepy Doll', 'A life-sized doll with button eyes.')
doll.weakness = 'Stuffed Bear'
attic._character = doll

# ============
# ADDING ITEMS
# ============
spoon = Item('Golden Spoon', 'A beautifully crafted golden spoon.')
kitchen._item = spoon

bear = Item('Stuffed Bear', 'A fluffy teddy bear with a missing eye.')
attic._item = bear

garden_coin = Item('Shiny Coin', 'A gleaming silver coin.')
garden._item = garden_coin

corridor_coin = Item('Rusty Coin', 'An old, rusted coin.')
corridor._item = corridor_coin

# =========
# GAME LOOP
# =========
current_room = corridor
inventory = []
killCount = 0

# START
clearScreen()
GAMEINFO.welcome()
start = input("Press any key to start the game. ")

while True and killCount < 2:
    clearScreen()

    current_room.describeRoom()

    # DISPLAY INVENTORY
    if inventory:
        print('Inventory:')
        for item in inventory:
            print(f' - {item}')
        print()

    # HANDLE ITEM/CHARACTER LOGIC
    if current_room._character:
        current_room._character.describe()
        
    if current_room._item:
        current_room._item.describe()

    sufficientAnswer = False
    while not sufficientAnswer:

        command = input('> ').lower()

        # MOVING
        if command in ['north', 'east', 'south', 'west']:
            new_room = current_room.move(command)

            if (new_room):
                sufficientAnswer = True
                current_room = new_room
            else:
                print()
                
        elif command == 'take':
            if current_room._item:
                current_room._item.take(inventory)
                current_room._item = None
            else:
                print("There is nothing to take here.\n")

        elif command == 'bribe':
            if current_room._character:
                current_room._character.bribe(inventory)
            else:
                print("There is no one to bribe here.\n")
                
        elif command == 'talk':
            if current_room._character:
                current_room._character.talk()
            else:
                print("There is no one to talk to here.\n")
                
        elif command == 'fight':
            if current_room._character:
                if isinstance(current_room._character, Enemy):
                    if current_room._character.weakness in inventory:
                        print(f'\nYou defeat the {current_room._character.name} with the {current_room._character.weakness}.')
                        current_room._character = None
                        time.sleep(1.5)
                        killCount += 1
                        sufficientAnswer = True
                    else:
                        print(f'\nThe {current_room._character.name} is too strong for you.')
                        time.sleep(1.5)
                        killCount = 999
                        sufficientAnswer = True
                else:
                    print(f'\nYou cannot fight {current_room._character.name}.')
            else:
                print("\nThere is no one to fight here.")
                
            print()
                
        elif command == 'help' or command == '?':
            GAMEINFO.help()
            
        elif command == 'quit':
            GAMEINFO.credits()
            exit()

        else:
            print("Command not recognised.\n")


if killCount == 2:
    clearScreen()
    print("You have defeated the enemies and won the game!")
    GAMEINFO.credits()
else:
    clearScreen()
    print("You have lost the game.")
    GAMEINFO.credits()