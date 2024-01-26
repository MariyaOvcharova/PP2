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

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
"""добавляет в список с другого списка или массива"""
print(thislist)

thislist.remove("banana")
thislist.pop(3)
del thislist[0]
print(thislist)

# thislist.clear()
# print(thislist)

for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

print(".")

i=0
while i<len(thislist):
    print(thislist[i])
    i += 1

print(".")
[print(x) for x in thislist]

