
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

for x in movies:
    if x["imdb"]>5.5:
        print(x["name"], x["imdb"])


movies1 = {}

for x in movies:
    name = x["name"]
    movies1[name] = {
        "imdb": x["imdb"]
    }

# print(movies1)

# y = input()
# for x in movies:
#     if x["category"]==y:
#         print(x["name"])

def aav(movies):
    num = len(movies)
    imbdd = 0
   
    for x in movies:
        imbdd += x["imdb"]
    
    if num > 0:
        avg = imbdd / num
        return avg
    else:
        return 0

avr = aav(movies)
print(avr)

 
def aav1(movies, category):
    num = len(movies)
    imdd = 0
    numM = 0
    for x in movies:
        if x["category"] == category:
            imdd += x["imdb"]
            numM += 1
    
    if numM > 0:
        avg = imdd / numM
        return avg
    else:
        return 0
    
category = input()
avr1 = aav1(movies, category)
print(avr1)