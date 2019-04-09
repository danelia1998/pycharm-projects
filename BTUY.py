def checker(list):
    for each in list:
        number = list.count(each)
        if number > 1 :
            while each in list:
                list.remove(each)
        print(each,number)

def main():
    list = input("shemoiyvanet nebismieri winadadeba").lower().split(" ")
    checker(list)
if __name__ == '__main__':
    main()