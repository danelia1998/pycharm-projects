import time
import random


class Duel:
    dict = {}

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        print("hello my name is {} i am ready to duel!".format(self.name))

    def givingRandomWeapon(self):
        print("i got cool pistol! and i have only one bullet to kill my oponent...")
        self.damage = self.damage - (random.randrange(0, 2))
        Duel.dict[self.name] = self.damage

    def countDown(self):
        print("THE DUEL BEGINS!")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("SHOT!!!")
        for key, value in Duel.dict.items():
            if value == 0:
                print("{} is dead...".format(key))
            else:
                print("WOW, {} is still alive,he is lucky one!!!!".format(key))


soldier1 = Duel("Pushkin", 1, 1)
soldier2 = Duel("Dantes", 1, 1)

Duel.givingRandomWeapon(soldier1)
Duel.givingRandomWeapon(soldier2)

Duel.countDown(soldier1)

