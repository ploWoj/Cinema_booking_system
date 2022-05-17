from cinemaHall import CinemaHall
import logging

class Cinema:

    listOfHalls = []
    listOfFilms = [
        "Blade Runner, 1982",
        "2001: A Space Odyssey, 1968",
        "One Flew Over the Cuckoo's Nest, 1975",
        "The Godfather, 1972",
        "The Good, the Bad and the Ugly, 1966"]
    maximumAmountOfHalls = 5

    def __init__(self):
        Cinema.listOfHalls = Cinema.creatListOfHalls()
        self.setFilmToHall()

    
    def displayAllFilms(self):
        print(">>>>> Playing movies in our theater <<<<<\n")
        counter = 0
        for halls in self.listOfHalls:
            counter += 1
            print(counter, halls.GetFilmName())
    
    
    
    @staticmethod
    def creatListOfHalls():
        list = []
        for i in range(0, Cinema.maximumAmountOfHalls):
            list.append(CinemaHall(''))
       
        return list
    
    def setFilmToHall(self):
        counter = 0
        for halls in self.listOfHalls:
            halls.setFilmName(self.listOfFilms[counter])
            counter +=1
            
