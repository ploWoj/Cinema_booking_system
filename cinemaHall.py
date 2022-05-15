
from re import S
from socket import SO_BROADCAST

from numpy import dstack
from scipy.fftpack import ss_diff
from yaml import safe_dump_all


class CinemaHall:

    def __init__(self, numberOfSeats, places, numberOfReservedSeats, hallNumber, filmName):
        self.numberOfSeat = numberOfSeats
        self.places = places
        self.numberOfReservedSeats = numberOfReservedSeats
        self.hallNumber = hallNumber
        self.filmName = filmName
    
    def setHallNumber(self, number):
        self.hallNumber = number
    
    def setFilmName(self, film):
        self.filmName = film

    def GetFilmName(self):
        return self.filmName

    def getNumberOfReservedSeats(self):
        return self.numberOfReservedSeats

    def addReservation(self):
        SO_BROADCAST

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
    