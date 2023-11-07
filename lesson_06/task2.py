import random

list_1 = []
list_2 = []
list_3 = []
while len(list_1) != 10:
    list_1.append(random.randint(0, 10))
    list_2.append(random.randint(0, 10))

for i in list_1:
    if i in list_2 and i not in list_3:
        list_3.append(i)


