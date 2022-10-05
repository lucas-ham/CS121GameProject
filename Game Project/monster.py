import random
import updater
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Monster:
    def __init__(self, name, health, damage, speed, room = None):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.room = room

        #two attributes used in fighting
        self.speed = speed
        self.damage = damage

        if room is not None:
            room.addMonster(self)
            updater.register(self)
    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def putInRoom(self, room):
        self.room = room
        room.addMonster(self)
        updater.register(self)
    def inspect(self):
        clear()
        print("This is the info for",self.name)
        print(self.name,"does",self.damage,"damage per attack")
        print(self.name,"has",self.health,"health")
        print(self.name,"has a speed rating of",self.speed)
        print()
        input("Press enter to continue...")
    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)
