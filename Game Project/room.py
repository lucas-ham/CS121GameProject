import random

class Room:
    def __init__(self, index, description):
        self.index = index
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0].lower() == direction.lower():
                return e[1]
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
    def checkForItem(self,item):
        #checks if an item (by name) is already available to pickup in the room
        for i in self.items:
            if i.name.lower() == item:
                return True
        return False
    def checkForMonster(self,monster):
        #checks if a monster is already in a given room
        for m in self.monsters:
            if m.name.lower() == monster:
                return True
        return False
    def checkForConnection(self,roomIndex):
        for n in self.exits:
            if n[1].index == roomIndex:
                return True
        return False
    def checkForDir(self,dir):
        for n in self.exits:
            if n[0] == dir:
                return True
        return False
