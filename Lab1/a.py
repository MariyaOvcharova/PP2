print("Hello World")

if 5 > 2:
  print("Five is greater than two!")


#следующее
"""лол кек"""

x = 5
y = "Hello, World!"
print (x,y)

z = "lol"
print(type(z))

a, b, c = "sosisochka", "sordelechka", "kolbasochka"
print(a, b, c)

stolovie_pribori = ["lozka", "vilka", "noz"]
l, v, n = stolovie_pribori
print(l)
print(v)
print(n)

p = "pyn'kat'"
nn = "nosik"
print (p+nn)


t = "cherepashka"

def New():
  print (t+ " polzet po polu")

New()

t1 = "cherepaha"
def New1():
  t1 = "cherepashonok"
  print (t1+ " polzet po polu")
New1()
print (t1+ " polzet po polu")

complex = 1j
print(type(complex))

complex = 5
complex1 = str(complex)
print(type(complex1))

import random 

print(random.randrange(0, 100))

w = int(6.5)
print(w)

print('by')

k = """ya lublu sobachek
i coshechek"""
print(k)

k = """ya lublu sobachek
i coshechek"""
print(k[0])

for x in "banana":
  print(x)

k = """ya lublu sobachek
i coshechek"""
print(len(k))

print("ya" in k)

print("mem" not in k)

print (k[3:26])

print(k.upper())

print(k.split(","))

l = 18
let = 'mne {} let'
print(let.format(l))

k = """ya lublu \'sobachek
i coshechek"""
print(k.title())
