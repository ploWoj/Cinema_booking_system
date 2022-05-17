import unittest

import seat 

class SeatTest(unittest.TestCase):

    seat = seat.Seat('Wojciech', 'Janiszyn', 32, True)
   
    def test_setSeat(self):
        self.assertEqual(self.seat.seatID, 32)
        self.assertTrue(self.seat.reserved)
        self.assertEqual(self.seat.surname, 'Janiszyn')
        self.assertEqual(self.seat.name , 'Wojciech')
    
    seat.cancelReservation()

    def test_cancelReservation(self):
        self.assertEqual(self.seat.surname, '')
        self.assertFalse(self.seat.isReserved())
        self.assertEqual(self.seat.name , '')
        
    

if __name__ =='__main__':
    unittest.main()
