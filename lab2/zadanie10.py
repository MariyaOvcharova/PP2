dict = {
    "earth":"zemlya",
    "water":"voda",
    "fire":"ogon'"
}

for x in dict:
    print(x)
    print(dict[x])

for x in dict.values():
    print(x)

for x in dict.keys():
    print(x)

for x, y in dict.items(): 
    print(x, "-" , y)

newdict = dict.copy()
print(newdict)

# newdict1 = dict(dict)
# print(newdict1)
# копировать второй способ

