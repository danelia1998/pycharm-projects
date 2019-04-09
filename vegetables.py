import datetime
import random


class Plant:
    def __init__(self, name, season):
        self.name = name
        self.season = season

    def info(self):
        print("This Plant is {} and ".format(self.name), "its seazon is {} !".format(self.season))

    def watering(self):
        if self.season is 'summer':
            print("watering needed 2 to 3 times per day\n")
        if self.season is 'winter':
            print("watering needed 1 times per day\n")
        if self.season is 'autumn':
            print("watering needed 2 times per day\n")
        if self.season is 'spring':
            print("watering needed 2 times per day\n")


class Apple(Plant):
    history = []

    def __init__(self, name, season, color):
        super().__init__(name, season)
        self.color = color
        Apple.history.append(self.color)

    def __add__(self, other):
        if self.color == 'red' and other.color == 'yellow' or self.color == 'yellow' and other.color == 'red':
            print('Mixing {} amd {} Trees! \nAnd there is Orange tree\n'.format(self.color, other.color))

        elif self.color == 'blue' and other.color == 'yellow' or self.color == 'yellow' and other.color == 'blue':
            print('Mixing {} amd {} Trees! \nAnd there is Green tree\n'.format(self.color, other.color))

        elif self.color == 'blue' and other.color == 'red' or self.color == 'red' and other.color == 'blue':
            print('Mixing {} amd {} Trees! \nAnd there is Purple tree\n'.format(self.color, other.color))

        else:
            print('Error\n')


class GodDamnPotato(Plant):
    def __init__(self, name, season, shelter_time):
        super().__init__(name, season)
        self.shelter_time = shelter_time

    def validPotato(self, dates):
        now = datetime.datetime.now()
        dates = dates.split('.')
        if ((int(now.month) * 30) + int(now.day)) - ((int(dates[1]) * 30) + int(dates[0])) < int(self.shelter_time):
            print("{} days out of {} days have passed, Your potato is ok!\n".format(
                ((int(now.month) * 30) + int(now.day)) - ((int(dates[1]) * 30) + int(dates[0])), self.shelter_time))
        else:
            print("{} days out of {} days have passed, Your potato is already spoiled!\n".format(
                ((int(now.month) * 30) + int(now.day)) - ((int(dates[1]) * 30) + int(dates[0])), self.shelter_time))


class Mosavali(Plant):

    def mosavlianoba(func):
        def mosRaodenoba(arg1):
            print("{} mcenaris mosavlianoba aris {} tona".format(arg1.name, random.randrange(1, 200)))
            return Mosavali.mosavlianoba(func)

        return mosRaodenoba

    @mosavlianoba
    def raimeFun(self):
        print("dato")


tree = Apple('gloria', 'summer', "red")
tree.info()
tree.watering()
tree2 = Apple('biscuit', 'winter', 'yellow')
tree2.info()
tree2.watering()
tree3 = tree + tree2

Potatoe = GodDamnPotato('walkis', 'autumn', 10)
Potatoe.validPotato("2.4.2019")

mos = Mosavali('Apple', 'summer')
mos.raimeFun()
