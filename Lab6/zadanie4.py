from time import sleep
import math
root = int(input())
mseconds = int(input())
seconds = mseconds/1000
sleep(seconds)
print("Square root of " , root, " after ",  mseconds, " miliseconds is", math.sqrt(root) )