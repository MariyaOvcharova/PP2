import re

file = open("row1.txt", "r", encoding="utf8")

text = file.read()

print(re.findall("ab*", text))

print(re.findall("ab{2,3}", text))

print(re.findall("\\D\\w+_\\w+\\D", text))

print(re.findall("[A-Z][a-z]+", text))

listik = []
words = text.split()
for word in words:
    listik.extend(re.findall("^a.*b$", word))
print(listik)


text1 = re.sub("\W", ":", text)

print(text1)