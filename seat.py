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
        self.PolishMenPopularName = self.loadMenNameFromFile(man_file_path)
        self.PolishWomenPopularName = self.loadMenNameFromFile(woman_file_path)
    
    def isReserved(self):
        return self.reserved

    def reserve(self):
        if self.isReserved():
            print("The place is already booked\n")
        else:
            name = input("Please give me your name: ")
            # if not name.isalpha:
            #     raise ValueError("Given name has to include only letters")

            self.surname = input("Please give me your name: ")
            self.seatID = input("Please give a seat number")
            self.isReserved = True
            print("Seat number {} has been reserved by {} {}".format(self.seatID, self.name, self.surname ))
    
    def cancelReservation(self):
        if not self.isReserved():
            print("Seat is free!!!!")
        else:
            self.name = ''
            self.surname = ''
            self.reserved = False
            print("Seat number {} has become free".format(self.seatID))

    def display(self):
        if self.reserved:
            print("Seat number {} is reserved by {} {}".format(self.seatID, self.name, self.surname))
        else:
            print("Seat number {} has been free.".format(self.seatID))
    

#  napisz funkcje ktora zszczytuje z pluku imiona i inicjalizuje zmienna imiona meskie
    
    def loadMenNameFromFile(self, path):
        
        lista = []
        with open(path, 'r') as f:
            for line in f:
                first = line.find(' ')
                line = line[first+ 1:]
                second = line.find(' ')
                line = line[:second]
                lista.append(line)
        return lista
        


seat = Seat('Wojciech', 'Plociennik', 32, True)


lista = Seat.PolishMenPopularName

print(lista)