import os
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
        self.PolishMenPopularName = Seat.loadMenNameFromFile(man_file_path)
        self.PolishWomenPopularName = Seat.loadMenNameFromFile(woman_file_path)
    

    def __str__(self):
        return "Seat number: {} is reserved: {} by {} {}".format(self.seatID, self.reserved, self.name, self.surname)
        
    def isReserved(self):
        return self.reserved

    def reserve(self):
        if self.isReserved():
            print("The place is already booked\n")
        else:
            name = input("Please give me your name: ")
            if name.upper() in self.PolishMenPopularName or name.upper() in self.PolishWomenPopularName:
                self.name = name
            else: 
                print("This is not Polish name.")

            self.surname = input("Please give me your surname: ")
            self.reserved = True
            print("Seat number {} has been reserved by {} {}".format(self.seatID , self.name, self.surname ))
    
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
        
        lista = []
        with open(path, 'r') as f:
            for line in f:
                first = line.find(' ')
                line = line[first+ 1:]
                second = line.find(' ')
                line = line[:second]
                lista.append(line)
        return lista
        









