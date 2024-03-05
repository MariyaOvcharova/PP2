import os

pathh = './files/'

for i in list(map(chr, range(97, 123))):
    with open(pathh + f"{i}.txt", "w") as file:
        file.write(f"{i}")