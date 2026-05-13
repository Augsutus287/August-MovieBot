# olika frågor som ställs till användaren
genre = input("What genre do you want to watch? ")
mood = input("What mood do you want to be in? ")
age = input("What age rating? 0, 7, 13, 18 ")



# Lagras olika filmer 
Movie =[
    {   "name": "dead poets society", "genre": "drama", "age": "13", "mood": "coziness" },
    {   "name": "cars", "genre": "kidsmovie", "age": "0", "mood": "nostalgic"},
    {   "name": "cars 2", "genre": "kidsmovie", "age": "0", "mood": "nostalgic"},
    {   "name": "cars 3", "genre": "kidsmovie", "age": "0", "mood": "nostalgic" },
    {  "name": "saw", "genre": "horror", "age": "18", "mood": "thrill" },
    {   "name": "Ironman", "genre": "action", "age": "13", "mood": "excited" },
    {   "name": "arthur and the invisibles", "genre": "animation", "age": "7", "mood": "adventurous" },
    {   "name": "Super Mario Bros Movie", "genre": "animation", "age": "7", "mood": "adventurous"}
    ]
# En loop som körs tills användaren är nöjd med rekommendationen
while True:

    #hur boten väljer den bästa filmen baserat på användarens svar
    best_score = 0
    best_movie = ""
    for movie in Movie:
        score = 0
    if movie["genre"] == genre:
        score += 1

    if movie["age"] == age:
        score +=1
    if movie["mood"] == mood:
        score +=1

    if score > best_score:
        best_score = score
        best_movie = movie["name"]    
     #rekommenderar filmen baserat på resultatet 
    print("Recomendation:", best_movie)
    print("are you satisfied with the recomendation? yes or no")
   
   #om svaret är yes så avslutas loppen.
    answer = input()
    if answer == "yes": 
        break

    print("KING BOB!")
