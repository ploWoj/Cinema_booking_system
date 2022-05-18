import time
import os
import logging



man_file_path = os.getcwd() + '/names/manName.txt'
woman_file_path = os.getcwd() + '/names/womanName.txt'

class Seat:

    PolishMenPopularName = []
    PolishWomenPopularName = []

    def __init__(self, name, surname, seatID, reserved):
        self.__name = name
        self.surname = surname
        self.__seatID = seatID
        self.__reserved = reserved
        try:
            self.PolishMenPopularName = Seat.loadMenNameFromFile(man_file_path)
            self.PolishWomenPopularName = Seat.loadMenNameFromFile(woman_file_path)
        except FileExistsError as e:
            print("You enter wrong file path",e)
            logging.exception("Enter wrong path")
            exit()
        
        logging.info("Creat object seat")

    def __str__(self):
        return "Seat number: {} is reserved: {} by {} {}".format(self.__seatID, self.__reserved, self.__name, self.surname)
        
    def isReserved(self):
        return self.__reserved

    def reserve(self):
        if self.isReserved():
            print("The place is already booked\n")
            time.sleep(2)
        else:
            try:
                name = self.validationName()
                if name.upper() in self.PolishMenPopularName or name.upper() in self.PolishWomenPopularName:
                    self.__name = name
                else: 
                    raise UnboundLocalError("That kind of name does not exist!\n")

                self.surname = self.validationName()
                self.__reserved = True
                print("\nSeat number {} has been reserved by {}  {}".format(self.__seatID , self.__name, self.surname))
                time.sleep(2)
            except ValueError as e:
                print("Entered word was incorect!", e)
                logging.exception("Entered word was incorect")
            except UnboundLocalError as e:
                print("Enterd name is not polish",e)
                logging.exception("Entered name is not correct")

    def validationName(self):
        name = input("Enter a name")
        if not name.isalpha():
            raise ValueError("Word should consits only letters!\n")
        return name
    
    def cancelReservation(self):
        if not self.isReserved():
            print("Seat is free!!!!")
            time.sleep(2)
        else:
            self.__name = ''
            self.surname = ''
            self.__reserved = False
            print("Seat number {} has become free".format(self.__seatID))
            time.sleep(2)

    @staticmethod
    def loadMenNameFromFile(path):
        if os.path.exists(path):
            lista = []
            with open(path, 'r') as f:
                for line in f:
                    first = line.find(' ')
                    line = line[first+ 1:]
                    second = line.find(' ')
                    line = line[:second]
                    lista.append(line)
        else:
            raise FileExistsError("File does not exists")
        return lista
        
    def setName(self, newName):
        self.__name = newName

    def setSurname(self, newSurname):
        self.surname = newSurname

    def setID(self, newID):
        self.__seatID = newID
    
    def setReserved(self, newReserved):
        self.__reserved = newReserved

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.surname


    def getSeatId(self):
        return self.__seatID







