a = 333
b = 555

if a == b:
    print("cool")
elif a > b:
    print("great")
else:
    print("ne cool")

print("cool") if a < b else print ("ne cool")

c = 222

if a<b and c<a:
    print("cool")

if a<b or b<a:
    print("klass")

if not b<a:
    print("boom")
    a+=222
    if a == b:
        print("cooler")
    

if a == b:
    pass

# error


i = 1
while i <= 7:
    print(i)
    i+=1

while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

while i < 6:
  i += 1
  if i == 2:
    continue
  print(i)

while i <= 5:
  print(i)
  i += 1
else:
  print("i is no longer less than 5")