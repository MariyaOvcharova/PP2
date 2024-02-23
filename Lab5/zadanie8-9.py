import re

file = open("Upper.txt", "r", encoding="utf8")

text = file.read()

text1 = re.findall("[A-Z][^A-Z]*", text)

print(text1)


text2 = ' '.join(text1)

print(text2)