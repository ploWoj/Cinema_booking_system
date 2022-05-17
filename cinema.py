from cinemaHall import CinemaHall
import logging
import os

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
        Cinema.listOfHalls = self.creatListOfHalls()
        self.setFilmToHall()
        os.system("clear")

        logging.info("Creat object cinema")

    
    def displayAllFilms(self):
        print(">>>>> Playing movies in our theater <<<<<\n")
        counter = 0
        for halls in self.listOfHalls:
            counter += 1
            print(counter, halls.GetFilmName())
    
    
    
    
    def creatListOfHalls(self):
        lista = []
        for i in range(0, Cinema.maximumAmountOfHalls):
            lista.append(CinemaHall('',[]))
       
        return lista
    
    def setFilmToHall(self):
        counter = 0
        for halls in self.listOfHalls:
            halls.setFilmName(self.listOfFilms[counter])
            counter +=1

    def writeToFile(self):

        path = os.getcwd()
        dirname = '/reservations/'
        path_dir = path + dirname

        if not os.path.exists(path_dir):
            os.mkdir(path_dir)
            logging.info("Creating directory to save file")
        
        filename = 'reservations.txt'
        path_file = os.path.join(path_dir, filename)
        counter = 0
        if os.path.exists(path_file):
            os.remove(path_file)
        
        for hall in self.listOfHalls:
            counter +=1
            hall.writeToFile(path_file,counter)
        

            
