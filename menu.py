from multiprocessing.sharedctypes import Value
from os import system
from cinemaHall import CinemaHall
from cinema import Cinema

class Menu:

    def __init__(self):
        self.cinema = Cinema()
    
    def printMenu(self):
        print("1. Add reservation.")
        print("2. Delete reservation.")
        print("3. Check the place.")
        print("4. Display all seats.")
        print("5. Display available seats.")
        print("6. Display reserved seats.")
        print("Exit - press 0")
        
    def selectMovie(self):
        system("clear")
        self.cinema.displayAllFilms()
        number = self.validIntiger()
        
        return self.cinema.listOfHalls[number]
            
        
    def runMenu(self):
        while True:
            
            self.printMenu()

            try:
                choice  = self.validIntiger()
                if choice == 1:
                    selectedHall = self.selectMovie()
                    selectedHall.addReservation()

                elif choice == 2:
                    selectedHall = self.selectMovie()
                    selectedHall.cancelReservation()

                elif choice == 3:
                    selectedHall = self.selectMovie()
                    selectedHall.checkSeat()

                elif choice == 4:
                    selectedHall = self.selectMovie()
                    selectedHall.displayAllPlaces()

                elif choice == 5:
                    selectedHall = self.selectMovie()
                    selectedHall.displayAvailableSeats()

                elif choice == 6:
                    selectedHall = self.selectMovie()
                    selectedHall.displayReservedSeats()
                else:
                    exit()
            except ValueError as e:
                print("Wrogng type entered!", e, '\n')


    def validIntiger(self):
        number = int(input("\nEnter a number\n"))
        if type(number) != int :
            raise ValueError("Entered type is not intiger!")
        return number
