def decor(func):
    def argumentebi(lost):
        vowels = []
        count = 0
        for each in lost:
            if each in ('a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"):
                vowels.append(each)
                count += 1
        print("there is {} vowels in our String !".format(count))
        print("This is vowels from string : {} \n \n ".format(vowels))
        return decor(func)

    return argumentebi


def censor(func):
    def finding(lost):
        censorship = ["i hate python", "fuck python", "my project sucks", "i hate coding",
                      "python is the worst language"]
        for each in censorship:
            if each in lost:
                print("Don't be a dickhead! USE CENSURE! + python The best ;)")
                break
        return censor(func)
    return finding


@censor
def strout(lost):
    print()


@decor
def strouh(lost):
    print()


raimesia = "i am vigaca and i want to say that python is the worst language ever made"
strouh(raimesia)
strout(raimesia)

