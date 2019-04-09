def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie, datvirtva):
        if datvirtva == 100:
            print("luci must take {} dollars".format(100))
        elif 100 > datvirtva >= 80:
            print("luci must take {} dollars".format(80))
        elif 80 > datvirtva >= 60:
            print("luci must take {} dollars".format(60))
        elif 60 > datvirtva >= 40:
            print("luci must take {} dollars".format(40))
        elif 40 > datvirtva >= 20:
            print("luci must take {} dollars".format(20))
        elif 20 > datvirtva >= 0:
            print("luci must take {} dollars".format(0))
        lie -= 3
        return method_to_decorate(self, lie, datvirtva)
    return wrapper


class lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie, datvirtva):
        print()


l = lucy()
l.sayYourAge(-3, 80)
