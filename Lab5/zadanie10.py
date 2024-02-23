import re

file = open("camel.txt", "r", encoding="utf8")

text = file.read()

text1 = re.findall("[A-Z][^A-Z]*", text)

text2 = ' '.join(text1)

text2 = text2.lower()

text3 = re.sub("\W", "_", text2)

print(text3)

