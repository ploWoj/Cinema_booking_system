
from re import S
from socket import SO_BROADCAST

from numpy import dstack
from scipy.fftpack import ss_diff
from yaml import safe_dump_all

from seat import Seat

maximumSeats = 50


class CinemaHall:

    hallNumber = 0
    reservedSeat = 0
    filmName = ''
    listOfPlaces = []

    def __init__(self, filmName):
        
        CinemaHall.listOfPlaces = CinemaHall.setPlaces(maximumSeats)
        CinemaHall.hallNumber += 1
        CinemaHall.reservedSeat = 0
        self.filmName = filmName
    
    
    def displayAllPlaces(self):
        for i in self.listOfPlaces:
            print(i)
    
    def displayFreeAndReservedSeat(self):
        numberOfFreeSeats = maximumSeats - self.reservedSeat

        print("Number of free seats {}".format(numberOfFreeSeats))
        print("Number of reserved seats {}".format(self.reservedSeat))


    @classmethod
    def displayAvailableSeats(cls):
        for i in cls.listOfPlaces:
            if not i.isReserved():
                print(i)

    @classmethod
    def displayReservedSeats(cls):
        for i in cls.listOfPlaces:
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
        else:
            print("Not reserved")

    def addReservation(self):
        self.displayAvailableSeats()
        if self.reservedSeat < maximumSeats:
            selectedSeat = self.listOfPlaces[self.selectSeat()]

            if not selectedSeat.isReserved():
                selectedSeat.reserve()
                self.reservedSeat += 1
            else:
                print("This seat is already selected")
        else:
            print("There is no more place.")

    def cancelReservation(self):
        self.displayReservedSeats()
        selectedSeat = self.listOfPlaces[self.selectSeat()]
        if selectedSeat.isReserved():
            selectedSeat.cancelReservation()
        else:
            print("This places cannot be canceld becouse is not reserved")


    def setFilmName(self, film):
        self.filmName = film

    def GetFilmName(self):
        return self.filmName

    def getNumberOfReservedSeats(self):
        return self.reservedSeat

    @staticmethod
    def setPlaces(maximiumSeats):
        listOfPlaces = []
        for i in range(1, maximiumSeats + 1):
            listOfPlaces.append(Seat('','',i,False))
        return listOfPlaces


