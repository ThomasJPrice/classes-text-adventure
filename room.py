import time

directions = {
    'north': '↑',
    'east': '→',
    'south': '↓',
    'west': '←',
}

def capitaliseFirstLetter(str):
    ls = list(str)
    ls[0] = ls[0].upper()
    return ''.join(ls)

class Room():
    number_of_rooms = 0

    def __init__(self, start_name):
        self._name = start_name
        self._description = None
        self._linked_rooms = {}
        self._character = None
        self._item = None
        Room.number_of_rooms += 1

    # NAME
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


    # DESCRIPTION
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    # LINKED ROOMS
    def link_room(self, room_to_link, direction):
        self._linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self._linked_rooms:
            return self._linked_rooms[direction]
        else:
            print("You can't go that way")
            return False

    # DESCRIBING ROOM
    def describeRoom(self):
        name_len = len(self._name)

        # HYPHENS FOR ROOM NAME
        hyphens = []
        for i in range(name_len):
            hyphens.append('-')
        hyphens = ''.join(hyphens)

        # ROOM NAME
        print(hyphens)
        print(f'{self._name}')
        print(hyphens)

        # DESCRIPTION
        print(f'{self._description}')
        print()

        # LINKED ROOMS
        for direction in self._linked_rooms:
            room = self._linked_rooms[direction]
            print(f"{directions[direction]} {room._name} is {capitaliseFirstLetter(direction)}")

        print()