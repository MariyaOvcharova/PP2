turtle =('solnce', 'luchik')
print(turtle)

turtle =('solnce', 'solnce', 'luchik')
print(turtle)
print(len(turtle))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print(turtle[0])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

y = list(x)
y.append("banana")
x = tuple(y)
print(x)

z = ("wildberry",)
x += z
print(x)

y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

#del x удаляет 

(a, b, c, *d) = x
print (a)
print(d)


tuple = ("apple", "banana", "cherry")
for i in range(len(tuple)):
  print(tuple[i])

i=0

while i<len(tuple):
  print(tuple[i])
  i += 1


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

f = mytuple.count("apple")
print(f)

g = mytuple.index("banana")
print(g+1)
