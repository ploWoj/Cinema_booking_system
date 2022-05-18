from os import system
from cinema import Cinema
import logging

class Menu:

    menuOption = ['Add reservation', 'Cancel reservation', 'Check the seat',
                 'Display all seats', 'Display available seats', 'Display reserved seats',
                 'Write to File', 'Load from File', 'EXIT']
    def __init__(self):
        self.cinema = Cinema()
    
    def printMenu(self):
        
        for i in range (0, len(self.menuOption)):
            print("{}. {}.".format(i + 1, self.menuOption[i]))
        
        
    def selectMovie(self):
        system("clear")
        self.cinema.displayAllFilms()
        number = self.validIntiger() - 1
        
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
                elif choice == 7:
                    self.cinema.writeToFile()
                elif choice == 8:
                    self.cinema.readFromFile()
                else:
                    exit()
            except TypeError as e:
                print("Wrogng type entered!", e, '\n')
                logging.exception("Write wrong type")
          

    def validIntiger(self):
       
        number = int(input("\nEnter a number\n"))
        if type(number) != int :
            raise TypeError("Entered type is not intiger!")

        return number
