fruits = ["apple", "banana", "cherry", "lemon"]
for x in fruits:
  print(x)
for x in "apple":
  print(x)

for x in fruits:
   print(x)
   if x == "cherry":
    break

for x in fruits:
   if x == "cherry":
    continue
print(x)


for x in range(5):
  print(x+1)
else:
  print("thats all")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


for x in [2, 45, 8]:
  pass