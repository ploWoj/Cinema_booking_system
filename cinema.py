class Cinema:

    def __init__(self, halls, amountOfHalls, films):
        self.halls = halls
        self.amountOfHalls = amountOfHalls
        self.films = films

    
    def displayAllFilms(self):
        for film in self.films:
            print(film)
    
    def getFilm(self, number):
        return self.halls[number]