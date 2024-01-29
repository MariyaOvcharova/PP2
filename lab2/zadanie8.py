thisset = {"apple", "banana", "cherry"}
print(thisset)

set = {1, 2, True, "meme"}
#True 1 FAlse 0 одно и то же
print(set)

print(len(set))

print(type(set))

for x in set:
    print(x)

print(1 in set)

set.add(False)

print(set)

set1 = ["define", 300]
set.update(set1)
print(set)

set.remove(300)
set.discard(False)
print(set)

set.pop()
print(set)

#del set or set.clear() очищает

set3 = {"a", "molli"}
set5 = {"zabka"}

set4 = set.union(set3)
print(set4)

set6 = set.update(set5)
print(set6)

set7 = {"meme", 2}
set8 = {"meme",}

set.intersection_update(set7)

print(set)


z = set.intersection(set8)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x1 = {"apple", "banana", "cherry"}
y1= {"google", "microsoft", "apple"}
z = x1.symmetric_difference(y1)

print(z)