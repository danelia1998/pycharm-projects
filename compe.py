
list = [much for much in range(1 ,20) if much % 2 == 1]
print(list)

list2 = [hah for hah in range(1, 20) if hah % 2 == 0]
print(list2)

dict = {list[each]: list2[each] for each in range(len(list))}

print(dict)
