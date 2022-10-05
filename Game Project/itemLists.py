from item import Item
from monster import Monster
from room import Room
#this generates and stores all of the items/monsters in the game
#other files pull from here, helps with randomly forming rooms and and randomly places items

#generate some items
itemList = []
#Item(name,desc,type,cost,damage)
itemList.append(Item("Axe","an axe","weapon", 10,10))
itemList.append(Item("Bow","a bow","weapon",30,20))
itemList.append(Item("Sword","a sword","weapon",5,15))
itemList.append(Item("Hatchet","a hatchet","weapon",3,10))
itemList.append(Item("Spoon","an ineffective spoon","weapon",10,3))
itemList.append(Item("Knife","a butter knife","weapon",5,15))
itemList.append(Item("Fork", "a solid metal fork","weapon",5,15))
itemList.append(Item("Tongs","a pair of metal tongs","weapon",7,20))
itemList.append(Item("Spatula","A trusty spatula","weapon",15,15))
itemList.append(Item("Lighter","A lighter used to turn on the stoves","weapon",20,30))

itemList.append(Item("Plate","a ceramic plate","defense",5,40))
itemList.append(Item("Hat","a knit hat","defense",10,25))
itemList.append(Item("Socks","wool socks","defense",2,10))
itemList.append(Item("Apron","a chefs apron","defense",15,55))
itemList.append(Item("Chef Hat","A puffy chef's hat","defense",5,30))
itemList.append(Item("Pan","A heafty metal pan","defense",30,60))

itemList.append(Item("Parmesan","some nice parmesan cheese to eat","heal",5,30))
itemList.append(Item("Garlic bread","well baked garlic bread","heal",5,10))
itemList.append(Item("Cheddar","some nice cheddar cheese to eat","heal",10,60))
itemList.append(Item("Napkin","a napkin","heal",5,20))

itemList.append(Item("Wine","a nice red wine","spell",10,2))
itemList.append(Item("Fanta","fanta soda","spell",5,1))
itemList.append(Item("Marinara Sauce","marinara sauce for drinking","spell",20,5))
itemList.append(Item("Jello","special jello, very fancy","spell",15,3))

itemList.append(Item("Salt","special salt that can increase your level","ex",40,10))
itemList.append(Item("Pepper","a peppery blend of expirience points","ex",20,4))
itemList.append(Item("Oregano","the secret oregano","ex",50,30))



#generate some monsters
monsterList = []
#monster(name,health, damage,speed, (optional room))
monsterList.append(Monster("Chair Person", 20, 5, 5))
monsterList.append(Monster("Grater",30,10,20))
monsterList.append(Monster('Slime',75,3,30))
monsterList.append(Monster('Bat',10,5,50))
monsterList.append(Monster('Cat',5,10,40))
monsterList.append(Monster('Hound',30,10,20))
monsterList.append(Monster('Meatball Person',30,25,40))
monsterList.append(Monster('Spagetti Person',30,20,60))
monsterList.append(Monster('Customer',40,15,50))
monsterList.append(Monster('Waiter',35,20,75))
monsterList.append(Monster('Valet Driver',20,20,80))
monsterList.append(Monster('Rat',10,15,50))
monsterList.append(Monster("Lasagna monster",30,17,50))


specialList = []
specialList.append(Item("special pasta","one of the three special ingredients","win"))
specialList.append(Item("special sauce","one of the three special ingredients","win"))
specialList.append(Item("special meatball","one of the three special ingredients","win"))



roomList = []
#room(index, description)
roomList.append(Room(1,"A kitchen where cooking is done. There are some stoves and pots and pans"))
roomList.append(Room(2,"A prep room, where cooks get food ready to be cooked"))
roomList.append(Room(3,"A greenhouse, for locally sourced ingredients"))
roomList.append(Room(4,"The Main Dining Room, where eating is done"))
roomList.append(Room(5,"A dining tent outside, for Covid-safe dining"))
roomList.append(Room(6,"A side dining room, for small groups"))
roomList.append(Room(7,"A room for storing pots, pans, dishes, and silverware"))
roomList.append(Room(8,"The sinks and dishwashers for cleaning dishes"))
roomList.append(Room(9,"The pantry, for storing food that doesn't need to be frozen"))
roomList.append(Room(10,"The freezer, for storing food so it won't go bad"))
roomList.append(Room(11,"A long hallway"))
roomList.append(Room(12,"A short hallway"))
roomList.append(Room(13,"A hallway that curves"))
roomList.append(Room(14,"A balcony on the side of the building"))
roomList.append(Room(15,"A jacket room where guests can check their coats"))
