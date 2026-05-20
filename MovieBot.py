
# olika fragor som stalls till anvandaren 




# Lagras olika filmer 
Movie =[
       # Drama
    {"name": "Dead Poets Society", "genre": "drama", "age": "13", "mood": "coziness"},
    {"name": "Forrest Gump", "genre": "drama", "age": "13", "mood": "nostalgic"},
    {"name": "Good Will Hunting", "genre": "drama", "age": "13", "mood": "coziness"},

    # Kidsmovie
    {"name": "Cars", "genre": "kidsmovie", "age": "0", "mood": "nostalgic"},
    {"name": "Toy Story", "genre": "kidsmovie", "age": "0", "mood": "nostalgic"},
    {"name": "The Lion King", "genre": "kidsmovie", "age": "0", "mood": "nostalgic"},

    # Horror
    {"name": "Saw", "genre": "horror", "age": "18", "mood": "thrill"},
    {"name": "It", "genre": "horror", "age": "18", "mood": "thrill"},
    {"name": "The Conjuring", "genre": "horror", "age": "18", "mood": "thrill"},

    # Action
    {"name": "Iron Man", "genre": "action", "age": "13", "mood": "excited"},
    {"name": "John Wick", "genre": "action", "age": "18", "mood": "excited"},
    {"name": "Top Gun: Maverick", "genre": "action", "age": "13", "mood": "excited"},

    # Animation
    {"name": "Super Mario Bros Movie", "genre": "animation", "age": "7", "mood": "adventurous"},
    {"name": "Kung Fu Panda", "genre": "animation", "age": "7", "mood": "adventurous"},
    {"name": "How to Train Your Dragon", "genre": "animation", "age": "7", "mood": "adventurous"},

    # Comedy
    {"name": "The Hangover", "genre": "comedy", "age": "18", "mood": "excited"},
    {"name": "Elf", "genre": "comedy", "age": "7", "mood": "coziness"},
    {"name": "Home Alone", "genre": "comedy", "age": "7", "mood": "nostalgic"},

    # Thriller
    {"name": "Gone Girl", "genre": "thriller", "age": "18", "mood": "thrill"},
    {"name": "Shutter Island", "genre": "thriller", "age": "13", "mood": "thrill"},
    {"name": "Se7en", "genre": "thriller", "age": "18", "mood": "thrill"},

    # Sci-Fi
    {"name": "Interstellar", "genre": "scifi", "age": "13", "mood": "adventurous"},
    {"name": "Inception", "genre": "scifi", "age": "13", "mood": "adventurous"},
    {"name": "The Matrix", "genre": "scifi", "age": "13", "mood": "excited"},
]
# En loop som kors tills anvandaren ar nojd med rekommendationen
while True:
    genre = input("What genre do you want to watch? ")
    mood = input("What mood do you want to be in? ")
    age = input("What age rating? 0, 7, 13, 18 ")
    
    best_score = 0
    best_movies = []  # ← lista istallet for en film
    
    for movie in Movie:
        score = 0
        if movie["genre"] == genre:
            score += 1
        if movie["age"] == age:
            score += 1
        if movie["mood"] == mood:
            score += 1
        if score > best_score:
            best_score = score
            best_movies = [movie["name"]] 
        elif score == best_score and score > 0:
            best_movies.append(movie["name"])  

    print("Recommendations:", ", ".join(best_movies[:3]))
    print("Are you satisfied with the recommendation? yes or no")
    
    answer = input()
    if answer == "yes":
        break

    
