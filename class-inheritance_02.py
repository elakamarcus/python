#!/bin/python3

class SpaceShip:
    def __init__(self, id, health, x, y):
        self.id = id
        self.health = int(health)
        self.x = x
        self.y = y

    def __del__(self):
        print("{} was destroyed.".format(self.id))
        del self
    
    def takeDMG(self, hit):
        self.health -= hit
        if self.health < 0:
            del self

    def isAlive(self):
        if(self.health >= 0):
            return True
        return False

    def isDead(self):
        if(self.health <= 0):
            return True
        return False

    def recvHealing(self, hp):
        self.health += hp
    
    def shipID(self):
        print("|------------------")
        print("| Ship ID      : {}".format(self.id))
        print("| Ship health  : {}%".format(self.health))
        print("| Ship location: {}, {}".format(self.x, self.y))
        print("|------------------")


class Destroyer(SpaceShip):
    def __init__(self, id, health, x, y, weapon, ammo):
        super().__init__(id, health, x, y)
        self.weapon = weapon
        self.ammo = ammo
        self.shipclass = "Destroyer"
        self.damagerate = 30

    def shipinfo(self):
        print("|---Destroyer class ship info")
        print("| Ship ID      :", self.id)
        print("| Ship type    :", self.shipclass)
        print("| Ship location: ({}, {})".format(self.x, self.y))
        print("| Ship armament:", self.weapon)
        print("| Ship ammo    : {}%".format(self.ammo))
        print("| Ship health  : {}%".format(self.health))
        print("|----------------------------")
    
    def attackDMG(self, targetship):
        print("|---------Attack----------")
        print("| {} is firing {} at {}, causing {} damage".format(self.id, self.weapon, targetship.id, self.damagerate))
        targetship.takeDMG(30)
        self.ammo -= 1
        print("| {} has {} hp remaining".format(targetship.id, targetship.health))
        print("|-------------------------")

class Medic(SpaceShip):
    def __init__(self, id, health, x, y, healingrate):
        super().__init__(id, health, x, y)
        self.healingrate = healingrate
        self.shipclass = "Medic"

    def shipinfo(self):
        print("|---Medic class ship info")
        print("| Ship ID      :", self.id)
        print("| Ship type    :", self.shipclass)
        print("| Ship location: ({}, {})".format(self.x, self.y))
        print("| Ship healing : {} hp/s".format(self.healingrate))
        print("| Ship health  : {}%".format(self.health))
        print("|-------------------------")

    def giveHealing(self, ship):
        print("|---------Healing---------")
        print("| {} is healing {} with {} HP".format(self.id, ship.id, self.healingrate))
        ship.recvHealing(self.healingrate)
        print("| {}'s health is now {}".format(ship.id, ship.health))
        print("|-------------------------")

    def __del__(self):
        print("{} was destroyed and is no more.".format(self.id))
        del self

def spaceMain():
    x = Destroyer("Foehammer", 100, 14, 48, "Photon torpedoes", 78)
    x.shipinfo() 
    #x.shipinfo()
    y = Medic("Pathways", 100, 13, 50, 50)
    y.shipID()
    #y.shipID()
    #y.shipinfo()

    for a in range(5):
        x.attackDMG(y)
#    while(True):
#        x.attackDMG(y)
#        if(y.health < 0):
#            y.__del__()
#            break

def main():
    spaceMain()

if __name__ == '__main__':
    spaceMain()