from movement import Movement
import unittest

class TestMovement(unittest.TestCase):
    
    def test_movement(self):
        move = Movement(0, 1) 
        self.assertEqual(move.apply(3)['eastwards'], 0)
        self.assertEqual(move.apply(3)['northwards'], 3)
        
    def test_specify_direction(self):
        move = Movement.specify('E')
        self.assertEqual(move.apply(2)['eastwards'], 2)
        self.assertEqual(move.apply(2)['northwards'], 0)
    
    def test_rotate_left(self):
        move = Movement(0, 1)
        move.rotate('L', 90)
        self.assertEqual(move.apply(4)['eastwards'], -4)        
        self.assertEqual(move.apply(4)['northwards'], 0)
           
    def test_rotate_right(self):
        move = Movement(0, 1)
        move.rotate('R', 90)
        self.assertEqual(move.apply(4)['eastwards'], 4)
        self.assertEqual(move.apply(4)['northwards'], 0)
    
    def test_rotate_left_270(self):
        move = Movement(0, 1)
        move.rotate('L', 270)
        self.assertEqual(move.apply(4)['eastwards'], 4)
        self.assertEqual(move.apply(4)['northwards'], 0)
                
    def test_rotate_right_270(self):
        move = Movement(0, 1)
        move.rotate('R', 270)
        self.assertEqual(move.apply(4)['eastwards'], -4)
        self.assertEqual(move.apply(4)['northwards'], 0)
        
    def test_rotate_180(self):
        move = Movement(0, 1)
        move.rotate('R', 180)
        self.assertEqual(move.apply(3)['eastwards'], 0)
        self.assertEqual(move.apply(3)['northwards'], -3)
            
if __name__ == '__main__':
    unittest.main()
