fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
    """лист со соловами с буквой а"""

print(newlist)

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)

newlist2 = [x for x in fruits if x != "banana"]

print(newlist2)

newlist3 = [x for x in range(5)]

print(newlist3)

kaps = ["solnce", "lyna", "zvezda"]

kaps2 = [x.upper() for x in kaps]

print(kaps2)

kaps3 = ["skazka" for x in kaps2]

print(kaps3)

kaps4 = [x if x != "solnce" else "meteor" for x in kaps]

print(kaps4)