print(11==6)
print(0>=0,1)

a=6
b=7

if b<a:
    print(b , "smaller")
else:
    print(b, "bigger")

print(bool("blobs"))
print(bool(123))
print(bool(["yabloko", "vishnya", "banan"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


def myclass():
    return 0

m=myclass()
print(m)

def myclass():
    return True

m=myclass()
print(m)

if myclass():
    print("DA")
else:
    print("No(")




