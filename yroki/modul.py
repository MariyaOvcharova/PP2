x = 300
def myFunk():
    global x
    x = 500
    print(x)
print(x)
myFunk()