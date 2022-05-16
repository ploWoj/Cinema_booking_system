class Cinema:

    def __init__(self, listOfHalls, amountOfHalls, listOfFilms):
        self.listOfHalls = listOfHalls
        self.amountOfHalls = amountOfHalls
        self.listOfFilms = listOfFilms

    
    def displayAllFilms(self):
        for film in self.listOfFilms:
            print(film)
    
    def getFilm(self, number):
        return self.halls[number]