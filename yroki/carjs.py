import json 
file = open("file.json")
car = file.read()
key = int(input())
print(car[key])