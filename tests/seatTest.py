import unittest
from projectFile.seat import Seat




class TestSeat(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("settng up class ...")
        cls.seat = Seat('Adam', 'Trauka',32, True)

    @classmethod
    def tearDownClass(cls):
        print('tearing down')
        del cls.seat

    def test_is_seat_reserve(self):
        self.assertTrue(self.seat.isReserved)

    def test_is_number_set(self):
        self.assertEqual(self.seat.getSeatId(), 32)
    
    def test_name_is_set_correctly(self):
        self.assertEqual(self.seat.getName(), 'Adam')
    
    def test_surname_is_set_correctly(self):
        self.assertEqual(self.seat.getSurname(), 'Trauka')



class TestSeatCancelReservation(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("settng up class ...")
        cls.seat = Seat('Adam', 'Trauka',32, True)

    @classmethod
    def tearDownClass(cls):
        print('tearing down')
        del cls.seat

    def test_is_seat_reserved(self):
        self.assertFalse(self.seat.cancelReservation(), self.seat.isReserved)
    
