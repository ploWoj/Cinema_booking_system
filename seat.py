import os
import logging



man_file_path = os.getcwd() + '/names/manName.txt'
woman_file_path = os.getcwd() + '/names/womanName.txt'

class Seat:

    PolishMenPopularName = []
    PolishWomenPopularName = []

    def __init__(self, name, surname, seatID, reserved):
        self.name = name
        self.surname = surname
        self.seatID = seatID
        self.reserved = reserved
        try:
            self.PolishMenPopularName = Seat.loadMenNameFromFile(man_file_path)
            self.PolishWomenPopularName = Seat.loadMenNameFromFile(woman_file_path)
        except FileExistsError as e:
            print("You enter wrong file path",e)
            logging.exception("Enter wrong path")
            exit()

    def __str__(self):
        return "Seat number: {} is reserved: {} by {} {}".format(self.seatID, self.reserved, self.name, self.surname)
        
    def isReserved(self):
        return self.reserved

    def reserve(self):
        if self.isReserved():
            print("The place is already booked\n")
        else:
            try:
                name = self.validationName()
                if name.upper() in self.PolishMenPopularName or name.upper() in self.PolishWomenPopularName:
                    self.name = name
                else: 
                    raise UnboundLocalError("That kind of name does not exist!\n")

                self.surname = self.validationName()
                self.reserved = True
                print("\nSeat number {} has been reserved by {} {}".format(self.seatID , self.name, self.surname ))
                
            except ValueError as e:
                print("Entered word was incorect!", e)
                logging.error("Entered word was incorect")
            except UnboundLocalError as e:
                print("Enterd name is not polish",e)
                logging.error("Entered name is not correct")

    def validationName(self):
        name = input("Enter a name")
        if not name.isalpha():
            raise ValueError("Word should consits only letters!\n")
        return name
    
    def cancelReservation(self):
        if not self.isReserved():
            print("Seat is free!!!!")
        else:
            self.name = ''
            self.surname = ''
            self.reserved = False
            print("Seat number {} has become free".format(self.seatID))

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
        









