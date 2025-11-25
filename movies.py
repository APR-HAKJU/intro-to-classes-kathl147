#Programm, das uns Informationen üher Filme ausgibt

#Jeder Film hat folgende Eigenschaften
#Genre, Titel, Releasejahr, Läge in Minuten

movie_1 =["Horror", "It", 2017, 135]
movie_2 =["Fanatsy", "Harry Potter", 1997, 97]

print(f"Titel des Films: {movie_1[1]}")
print(f"Titel des Films: {movie_2[1]}")
  
class Movie: # Klasse = Bauplan für ein Thema
    def __init__(self,title,genre,duration,release_year ): # Konstruktor -> Wird immer aufgerufen, wenn ein neues Objekt erstellt wird.
        self.title=title
        self.genre=genre
        self.duration=duration
        self.release_year=release_year
        
        print("Neuer Film wurde erstellt!")

# movie_3=Movie() # Erstellt uns ein Objekt nach dem Bauplan "Movie"
# movie_4=Movie()
# movie_5=Movie()

# movie_3.title = "Real Steel"
# print(f"Titel des Filmes: {movie_3.title}")

# movie_3.genre = "Aktion"
# movie_3.duration = 120
# movie_3.release_year = 2015

# movie_4.title="Barbie"
# movie_4.genre="Fantasy"
# movie_4.duration = 125
# movie_4.release_year = 2022

movie_6=Movie(title="Dune: Awakering", genre="Sci-Fi", duration=180, release_year=2020)
print(f"Titel des Filmes: {movie_6.title}")

movie_7=Movie(title="Barbie", genre="Drama", duration=125, release_year=2023)
print(f"{movie_7.title} wurde im Jahr {movie_7.release_year} herausgebracht")

