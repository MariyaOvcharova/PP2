list = [1, 3 , 4]
list1 = ["lol", "kek"]
list3 = ["lol", "kek", "chebyreck"]
list2 = list + list1
print(list2)

list = [1, 3 , 4]
list1 = ["lol", "kek"]

for x in list:
    list1.append(x)

print(list2)

list3.extend(list)
print(list3)