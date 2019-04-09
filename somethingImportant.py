def hamburger(func):
    def wrapper():
        print("bread")
        func()

    return wrapper


def bread(func):
    def wrapper():
        print()
        func()
        print("<\_______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#pomidori#")
        print("#yveli")
        func()
        print("-sousi-")

    return wrapper


@hamburger
@bread
@ingredients
def sandwich(food="--bekoni-"):
    print(food)


sandwich()
