listt = ["DJ", "make", "list", "of", "songs"] 
with open("ttt.txt", "w") as file:
    for i in listt:
        file.write(str(i))
        file.write(str(" "))
    