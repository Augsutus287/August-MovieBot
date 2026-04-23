genre = input("What genre do you want to watch? ")
mood = input("What mood do you want to be in? ")
age = input("What is your age? ")





Movie =[
    {   "name": "dead poets society", "genre": "drama", "age": "13", "mood": "coziness" },
    {   "name": "cars", "genre": "kidsmovie", "age": "0", "mood": "nostalgi"},
    {   "name": "cars 2", "genre": "kidsmovie", "age": "0", "mood": "nostalgi"},
    {   "name": "cars 3", "genre": "kidsmovie", "age": "0", "mood": "nostalgi" },
    {  "name": "saw", "genre": "horror", "age": "18", "mood": "thrill" } ]

best_score = 0
best_movie = ""

for movie in Movie:
    score = 0
    if movie["genre"] == "genre":
        score += 1

    if movie["age"] == "age":
        score +=1
    if movie["mood"] == "mood":
        score +=1

    if score > best_score:
        best_score = score
        best_movie = movie["name"]    
     
print("Recomendation:", best_movie)