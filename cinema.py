from re import L
import time
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
    maximumAmountOfHalls = 6

    def __init__(self):
        self.listOfHalls = self.creatListOfHalls()
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
        for i in range(1, Cinema.maximumAmountOfHalls):
            lista.append(CinemaHall('', i))
       
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
        
        counter = 1
        for hall in self.listOfHalls:
            hall.writeToFile(path_file, counter)
            counter += 1


    def readFromFile(self):
       
        path = os.getcwd()
        dirname = '/reservations/'
        path_dir = path + dirname
        filename = 'reservations.txt'
        path_file = os.path.join(path_dir, filename)

        if not os.path.exists(path_file):
            raise FileExistsError("File does not exists")
        

        with open(path_file, 'r') as f:
            for hall in self.listOfHalls:
                sth  = []
                counter = 0
                for line in f:
                    sth= line.split(' ')
                    seat = hall.listOfPlaces[counter]
                    for i in range(0, len(sth)):
                        if i == 6:
                            seat.setID(sth[i])
                        elif i == 9:
                            seat.setReserved(sth[i])
                        elif i == 11:
                            seat.setName(sth[i])
                        elif i == 12:
                            seat.setSurname(sth[i])
                         
                    counter += 1
                    
                    if counter == 50:
                        counter = 0
                        break
            time.sleep(1)
