list_1 = range(1, 101)
list_2 = []
c = 0
while c < 100:
    if list_1[c] % 7 == 0 and list_1[c] % 5 != 0:
        list_2.append(c+1)
    c += 1
print(list_2)
