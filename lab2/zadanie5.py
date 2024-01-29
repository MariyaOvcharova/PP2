list = [1, 3, 12, 67, 4, 2]
list.sort()
print(list)

list1 = ["ananas", "apelsin", "abrikos"]
list1.sort()
print(list1)

list.sort(reverse = True)
print(list)


def new(n):
    return abs(n-1000)

listick = [1, 193, 924, 27]
listick.sort(key = new)
print(listick)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.reverse()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

copy = listick.copy()
print(copy)

copy1 = list(thislist)
print(copy1)
