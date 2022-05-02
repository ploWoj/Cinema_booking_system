class Seat:

    def __init__(self, name, surname, seatID, reserved):
        self.name = name
        self.surname = surname
        self.seatID = seatID
        self.reserved = reserved
    
    def isReserved(self):
        return self.reserved

    def reserve(self):
        if self.isReserved():
            print("The place is already booked\n")
        else:
            self.name = input("Please give me your name: ")
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
    