list = ["Yarick", "Andrey", "Timur"]
print(list)
print(len(list))

list1 = ["sobachka", 1, 0.3]
print(list1)
print(type(list1))

list2 = (("sobachka", 1, 0.3))
print(list2)
print(type(list2))

list1 = ["sobachka", 1, 0.3]
print(list1[0])
print(list1[-2])

print(list[:2])
print(list[:-2])

if "Andrey" in list:
    print("razocharovanie")


list[2]="Danil"
print (list)

list4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list4[1:3] = ["blackcurrant", "watermelon"]
print(list4)

list.insert(4, "Kirill")
print(list)