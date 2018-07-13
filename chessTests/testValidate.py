import unittest
import validate

class TestValidation(unittest.TestCase):

    def testPawnMove(self):
        self.assertEqual(True, True)
        #self.assertEqual(True, False)



    def testKingMove(self):
        self.assertEqual(True, False)
        #self.assertEqual(True, False)

if __name__ == "__main__":
    unittest.main()