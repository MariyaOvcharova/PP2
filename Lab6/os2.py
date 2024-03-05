file = open("trtrt.txt", "r")

c=0

file1 = file.readlines()

for i in file1:
    c+=1


print (c)
file.close()
