
from re import S
from socket import SO_BROADCAST

from numpy import dstack
from scipy.fftpack import ss_diff
from yaml import safe_dump_all

from seat import Seat

class CinemaHall:

    def __init__(self, numberOfSeats, places, numberOfReservedSeats, hallNumber, filmName):
        self.numberOfSeat = numberOfSeats
        self.places = places
        self.numberOfReservedSeats = numberOfReservedSeats
        self.hallNumber = hallNumber
        self.filmName = filmName

    def reservedPlaces(self):
        for i in range(i, self.numberOfSeat):
            self.places.append(Seat('','',i,False))
    
    
    def setHallNumber(self, number):
        self.hallNumber = number
    
    def setFilmName(self, film):
        self.filmName = film

    def GetFilmName(self):
        return self.filmName

    def getNumberOfReservedSeats(self):
        return self.numberOfReservedSeats

    def addReservation(self):
        if self.numberOfReservedSeats < self.numberOfSeat:
            selectedSeat = self.selectSeat()
            if selectedSeat and not self.places[self.selectSeat-1].isReserved():
                self.places[selectedSeat - 1].reserved()
                self.numberOfReservedSeats += 1
            else:
                print("This seat is already selected")


    def defleteReservation(self):
        dstack
    
    def selectSeat(self):
        SO_BROADCAST
    
    def checkSeat(self):
        safe_dump_all
    
    def displayAllSeats(self):
        S
    
    def displayAllAvailabeSeats(self):
        ss_diff
    
    def displayReservedSeats(self):
        S
    
    def displayAmountOfFreeAndReservedSeats(self):
        ss_diff
    