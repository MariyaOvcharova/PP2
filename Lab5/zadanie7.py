import re

file = open("snake.txt", "r", encoding="utf8")

text = file.read()


text1 = re.sub("_", " ", text)
text2 = re.sub("  ", "\n" , text1)
print(text1)