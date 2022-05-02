import unittest

import seat 

class SeatTest(unittest.TestCase):

    seat = seat.Seat('Wojciech', 'Janiszyn', 32, True)
    def test_checkReservation(self):
        self.assertTrue(self.seat.isReserved())
    
    def test_CheckName(self):
        self.assertEqual(self.seat.name, 'Wojciech')
    
    def test_NumerOfSeat(self):
        self.assertEqual(self.seat.seatID, 32)
        
    

if __name__ =='__main__':
    unittest.main()
