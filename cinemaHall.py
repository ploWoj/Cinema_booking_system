
from re import S
from socket import SO_BROADCAST

from numpy import dstack
from scipy.fftpack import ss_diff
from yaml import safe_dump_all

from seat import Seat

maximumSeats = 50


class CinemaHall:

    hallNumber = 0
    listOfReservedSeats = []
    nameOfFilm = ''
    listOfPlaces = []

    def __init__(self):
        
        CinemaHall.listOfPlaces = CinemaHall.setPlaces(maximumSeats)
        CinemaHall.hallNumber += 1
        

    
    def displayAllPlaces(self):
        for i in self.listOfPlaces:
            print(i)
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
    
    def addReservation(self):
        
        chosenSeat = input("Enter a seat you want to choose.")
        
        while chosenSeat > len(self.listOfPlaces) and chosenSeat < 1:
            print("Try to choose a seat from 1 to {}".foramt(maximumSeats))

        
        if self.numberOfReservedSeats < self.numberOfSeat:
            selectedSeat = self.selectSeat()
            if selectedSeat and not self.places[self.selectSeat-1].isReserved():
                self.places[selectedSeat - 1].reserved()
                self.numberOfReservedSeats += 1
            else:
                print("This seat is already selected")
    

    def selectSeat(self):
        
        selected =  int(input("Select number of seat "))
        while (selected < 1 or selected > len(self.listOfPlaces)):
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



#     void CinemaHall::checkSeat() {
#     std::cout << "Check the reservation: \n";
#     size_t selectedSeat = selectSeat();
#     if (selectedSeat) {
#         places_[selectedSeat - 1].display();
#     }
# }


    def setFilmName(self, film):
        self.filmName = film

    def GetFilmName(self):
        return self.filmName

    def getNumberOfReservedSeats(self):
        return self.numberOfReservedSeats

    @staticmethod
    def setPlaces(maximiumSeats):
        listOfPlaces = []
        for i in range(1, maximiumSeats + 1):
            listOfPlaces.append(Seat('','',i,False))
        return listOfPlaces



    # def defleteReservation(self):
    #     dstack
    
    # def selectSeat(self):
    #     SO_BROADCAST
    
    # def checkSeat(self):
    #     safe_dump_all
    
    # def displayAllSeats(self):
    #     S
    
    # def displayAllAvailabeSeats(self):
    #     ss_diff
    
    # def displayReservedSeats(self):
    #     S
    
    # def displayAmountOfFreeAndReservedSeats(self):
    #     ss_diff
    

kino1 = CinemaHall()

# line = kino1.selectSeat()

kino1.checkSeat()

