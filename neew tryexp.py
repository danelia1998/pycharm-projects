def testFunction(func):
    def checker(arg, arg2, arg3):
        try:
            open('{}'.format(arg), 'r')
        except:
            print("there isn't file like this {}".format(arg))
        print()

        try:
            val = int(arg2)
            print("this input isn't string")
        except ValueError:
            print("this input :'{}' is string !".format(arg2))

        print()
        try:
            val2 = int(arg3)
            print("this input:'{}' is integer!".format(arg3))
        except ValueError:
            print("That not an int!")
        return testFunction(func)

    return checker


@testFunction
def function(arg, arg2, agr3):
    print()


arg = input("enter some TXT file to open it")
arg2 = input("enter some string")
arg3 = input("enter some integer")
function(arg, arg2, arg3)
