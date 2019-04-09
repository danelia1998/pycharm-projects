from datetime import date

def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)

    return wrapper


def birthday(func):
    def birthdayTime(self, birthDate):

        print(birthDate)
        age = date.today() - birthDate
        print(age.days)

        return func(self, birthDate)

    return birthdayTime


class lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("{} ის, ვარ და რამდენის გეგონე? ".format(self.age + lie))

    @birthday
    def Birthdaytimes(self,birthDate):
        print()


l = lucy()

l.sayYourAge(-3)

l.Birthdaytimes(date(1999,9,19))
