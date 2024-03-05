import os

def exx(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Doesn't exist")

ss = "t.txt"

exx(ss)