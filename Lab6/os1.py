import os

def exx(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)

        print("Directory portion:", directory)
        print("Filename:", filename)
    else:
        print("Doesn't exist")

ss = input()

exx(ss)
