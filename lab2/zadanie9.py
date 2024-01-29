thisdict = {
  "brand": "Porshe",
  "model": "spyder",
  "year": 2023
}

print(thisdict)
print(thisdict["model"])
print(len(thisdict))


thisdict1 = {
  "brand": "Porshe",
  "model": ["spyder", 911],
  "year": 2023
}

print(thisdict1)

thisdict2 = dict(model = 911)
print(thisdict2) #создает новый дикт

x = thisdict.get("year") #значение под этим ключем
print(x)

y = thisdict.keys() #только ключи
print(y)

thisdict["model"] = 911
print(thisdict)

z = thisdict.values() #только значения
print(z)

i = thisdict.items() #все части дикта
print(i)

if "model" in thisdict:
    print("I'm in love")

thisdict.update({"year":2024})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.update({"model":"spyder"})
print(thisdict)

# thisdict.popitem()
# print(thisdict)
# -последний элемент

# del thisdict["model"]
# print(thisdict)
# удаляет элемент под ключем

# thisdict.clear()
# print(thisdict)
# очищает
