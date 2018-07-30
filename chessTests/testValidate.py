import unittest
import validate

"""complete unite test for Friday and make sure I understand it"""
""" show phil a good understanding of how i've converted the TestValidate to Unite test and got everything working"""

class TestValidation(unittest.TestCase):

    def setUp(self):
        self.chess_board = {"A2": "P_W",
                       "B4": "P_B",
                       "H7": "P_B",
                       "G5": "P_W",
                       "C3": "K_W",
                       "F8": "K_B",
                       "C7": "P_B",
                       "A8": "C_B",
                       "A6": "C_B",
                       "B6": "C_W",
                       "A7": "P_W",
                       "D1": "Q_W"}

    # def tearDown(self):
    #     print("Fin a test")

    def testValidate_move(self):

        with self.assertRaises(validate.ValidationException):

            validate.validate_move(self.chess_board, "A2", "A3")
            validate.validate_move(self.chess_board, "H9", "cheese")
            validate.validate_move(self.chess_board, "E1", "E3")
            validate.validate_move(self.chess_board, "C3", "D4")
            validate.validate_move(self.chess_board, "C3", "D7")
            validate.validate_move(self.chess_board, "C3", "H3")

    def testCoordinate_to_column_number(self):
        self.assertEqual(2, validate.coordinate_to_column_number("C3"), msg="C3 should give us column number 2")

        validate.coordinate_to_column_number("H3")
        validate.coordinate_to_column_number("B3")
        validate.coordinate_to_column_number("D3")

    def testPawnMove(self):
        #self.assertEqual(True, validate.validate_move(self.chess_board, "A2", "A3"))

        with self.assertRaises(validate.ValidationException):
            validate.validate_move(self.chess_board, "A2", "A4")
            validate.validate_move(self.chess_board, "A2", "A3")
            validate.validate_move(self.chess_board, "A2", "A7")
            validate.validate_move(self.chess_board, "A2", "A4")
            validate.validate_move(self.chess_board, "A2", "A1")
            validate.validate_move(self.chess_board, "C7", "C5")

        #self.assertRaises
        # try:
        #     self.fail("Didn't getexpected exception")
        # except validate.ValidationException:
        #     pass

        # print("True validate move pawn A2 to A4", validate.validate_move(self.chess_board, "A2", "A4"))
        # # print("True validate move king A7 to A6", validate.validate_move(self.chess_board, "A7", "A6"))
        # print("False validate move pawn A2 to A1", validate.validate_move(self.chess_board, "A2", "A1"))
        # print("True validate move pawn C7 to C5", validate.validate_move(self.chess_board, "C7", "C5"))
        #self.assertEqual(True, True)
        #self.assertEqual(True, False)

    def testQueenMove(self):

        # self.assertEqual(True, validate.validate_move(self.chess_board, "D1", "D2"))
        # self.assertEqual(True,True)
        # with self.assertRaises(validate.ValidationException):
        validate.validate_move(self.chess_board, "D1", "D2")
        with self.assertRaises(validate.ValidationException):
            validate.validate_move(self.chess_board, "D1", "D3")

    def testKingMove(self):

        # pass
        #self.assertEqual(True, False)
        #self.assertEqual(True, False)

        with self.assertRaises(validate.ValidationException):
            validate.validate_move(self.chess_board, "D1", "D3")

    def testRookMove(self):

        with self.assertRaises(validate.ValidationException):
            validate._validate_rook_move(self.chess_board, "A8", "B3", 0, 1)
            validate._validate_rook_move(self.chess_board, "A8", "A3", 0, 0)
            validate._validate_rook_move(self.chess_board, "A8", "C8", 0, 2)
            validate._validate_rook_move(self.chess_board, "A8", "A5", 0, 0)
            validate._validate_rook_move(self.chess_board, "A6", "E6", 0, 4)
            validate._validate_rook_move(self.chess_board, "A6", "B6", 0, 1)
            validate._validate_rook_move(self.chess_board, "A8", "A6", 0, 0)
            validate.validate_move(self.chess_board, "A8", "A6")
            validate.validate_move(self.chess_board, "A8", "C8")
            validate.validate_move(self.chess_board, "A8", "A5")
            validate.validate_move(self.chess_board, "A6", "E6")

    def testKnightMove(self):

        #with self.assertRaises(validate.ValidationException):
            pass

    def testBishopMove(self):

        with self.assertRaises(validate.ValidationException):
            validate.validate_move(self.chess_board, "C1", "A3")

if __name__ == "__main__":
    unittest.main()