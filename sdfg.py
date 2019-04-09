list = [1, [9, [[[[[2]]]]]], [[[2], [12, [2]], [10]]]]


def make_list_flat(l):
    flist = []
    flist.extend([l]) if (type(l) is not list) else [flist.extend(make_list_flat(e)) for e in l]
    return flist


a = [[1, 2], [[[[3, 4, 5], 6]]], 7, [8, [9, [10, 11], 12, [13, 14, [15, [[16, 17], 18]]]]]]
flist = make_list_flat(a)
print(flist)
