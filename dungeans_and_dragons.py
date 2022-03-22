import random

class Elf(object):
    def __init__(self, name):
        self.name = name
        self.attack = 10
        self.defend = 8
        self.body = 9

class Dwarf(object):
    def __init__(self, name):
        #add attributes
        self.name=name
        self.defend=5
        self.attack=8
        self.body=5
    #add methods
    def talk(self):
        print("I'm a blade-man, I will cut you!!!!!")

osys=Dwarf("Osys")
print("Dwarf name is {}".format(osys.name))
osys.talk()

esseden=Elf("Esseden")
print("Elf name = {}".format(esseden.name))
print("Esseden body value = {}".format(esseden.body))

osys_attack_roll=random.randrange(1, osys.attack+1)
print("Osys attack roll = {}".format(osys_attack_roll))

esseden_defend_roll=random.randrange(1, esseden.defend+1)
print("Esseden defend roll = {}".format(esseden_defend_roll))

damage = osys_attack_roll -esseden_defend_roll
if damage > 0:
    esseden.body -= damage
print("Esseden body value = {}".format(esseden.body))