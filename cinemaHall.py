import os
import time
from typing import Counter
from seat import Seat
import logging
maximumSeats = 50


class CinemaHall:

    def __init__(self, filmName, hallNumber):
        
        self.listOfPlaces = self.setPlaces(maximumSeats)
        self.reservedSeat = 0
        self.filmName = filmName
        self.__hallNumber = hallNumber
        # self.__hallNumber += 1
        logging.info("Creating object CinemaHall")
    
    def __str__(self):
        return "Hall number {} with reserved seats {}, playing movie.".format(self.__hallNumber, self.reservedSeat)

    def displayAllPlaces(self):
        for i in self.listOfPlaces:
            print(i)
    
    def displayFreeAndReservedSeat(self):
        numberOfFreeSeats = maximumSeats - self.reservedSeat
        print('\n')
        print("Number of free seats {}".format(numberOfFreeSeats))
        print("Number of reserved seats {}".format(self.reservedSeat))
        time.sleep(5)


    def displayAvailableSeats(self):
        print('\n')
        for i in self.listOfPlaces:
            if not i.isReserved():
                print(i)
        print('\n')

    def displayReservedSeats(self):
        print('\n')
        for i in self.listOfPlaces:
            if i.isReserved():
                print(i)
        
    def selectSeat(self):
        
        selected =  int(input("Select number of seat ")) - 1
        while (selected < 0  or selected > len(self.listOfPlaces)):
            print('Try to choose a seat from 1 to {}'.format(len(self.listOfPlaces)))
            selected =  int(input("Select number of seat "))
    
        return selected

    def checkSeat(self):
        print("Check if seat is reserved.")
        numberOfSeat = self.selectSeat()
        selectedSeat = self.listOfPlaces[numberOfSeat]
        if selectedSeat.isReserved():
            print("Reserved")
            time.sleep(5)
        else:
            print("Not reserved")
            time.sleep(5)
            

    def addReservation(self):
        self.displayAvailableSeats()
        if self.reservedSeat < maximumSeats:
            selectedSeat = self.listOfPlaces[self.selectSeat()]

            if not selectedSeat.isReserved():
                selectedSeat.reserve()
                self.reservedSeat += 1
            else:
                print("This seat is already selected")
                time.sleep(5)
        else:
            print("There is no more place.")
            time.sleep(5)

    def cancelReservation(self):
        self.displayReservedSeats()
        selectedSeat = self.listOfPlaces[self.selectSeat()]
        if selectedSeat.isReserved():
            selectedSeat.cancelReservation()
        else:
            print("This places cannot be cancel becouse is not reserved")
            time.sleep(5)


    def setFilmName(self, film):
        self.filmName = film

    def GetFilmName(self):
        return self.filmName

    def getNumberOfReservedSeats(self):
        return self.reservedSeat

    
    def setPlaces(self, maximiumSeats):
        listOfPlaces = []
        for i in range(1, maximiumSeats + 1):
            listOfPlaces.append(Seat('',' ',i,False))
        return listOfPlaces


    def writeToFile(self, path, number):
        with open(path, 'a+') as f:
            for line in self.listOfPlaces:
                
                if len(self.listOfPlaces) == 0:
                    logging.info("Luck of reservations in hall number {}".format(line))
                    continue


                f.write("Cinema hall nr: {} ".format(str(number)) + str(line) +"\n")
        
#    def readFromFile(self, path, nuber):