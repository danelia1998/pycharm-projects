def checker(list, sia):
    for each in list:
        try:
            print(int(each))
            sia.append(each)
        except:
            list.extend(each)
    print(sia)


def main():
    multi_dimensional_array = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]
    sia = []
    checker(multi_dimensional_array, sia)
if __name__ == '__main__':
    main()
