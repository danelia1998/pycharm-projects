import random


def decorator(funqcia):
    def checker(listo):
        for each in listo:
            print(each, " ლარი")

    return checker


@decorator
def randomizer(listo):
    print()




listo = []
for each in range(10):
    listo.append(random.randrange(1, 100))
    
randomizer(listo)