import os

print(os.listdir()) #печатает все файлы в папке


def exx(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK):
            print("Readable: Yes")
        else:
            print("Readable: No")
        
        if os.access(path, os.W_OK):
            print("Writable: Yes")
        else:
            print("Writable: No")

        if os.access(path, os.X_OK):
            print("Executable: Yes")
        else:
            print("Executable: No")
    else:
        print("Doesn't exist")

ss = input()

exx(ss)
