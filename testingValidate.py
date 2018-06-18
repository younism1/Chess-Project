import validate
import specialMove



if __name__ == "__main__":
    chess_board = {"A2": "P_W",
                   "C3": "K_W",
                   "F8":"K_B",
                   "C7": "P_B",
                   "A8": "C_B"}

    print("A2", validate.validate_move(chess_board, "A2", "A3"))
    print("====" * 30)
    print(validate.validate_move(chess_board, "H9", "cheese"))
    print("====" * 30)
    print(validate.validate_move(chess_board, "E1", "E3"))
    print("====" * 30)

    print("True validate move king", validate.validate_move(chess_board, "C3", "D4"))
    print("False validate move king", validate.validate_move(chess_board, "C3", "D7"))
    print("False validate move king", validate.validate_move(chess_board, "C3", "H3"))

    print("====" * 30)
    print("Validate C is 3", validate.coordinate_to_column_number("C3"))
    print("Validate H is 7", validate.coordinate_to_column_number("H3"))
    print("Validate B is 1", validate.coordinate_to_column_number("B3"))
    print("Validate D is 3", validate.coordinate_to_column_number("D3"))


    print("====" * 30)
    print("True validate move pawn A2 to A3", validate.validate_move(chess_board, "A2", "A3"))
    print("False validate move pawn A2 to A7", validate.validate_move(chess_board, "A2", "A7"))
    print("True validate move king A2 to A4", validate.validate_move(chess_board, "A2", "A4"))
    #print("True validate move king A7 to A6", validate.validate_move(chess_board, "A7", "A6"))
    print("False validate move king A2 to A1", validate.validate_move(chess_board, "A2", "A1"))
    print("True validate move king C7 to C5", validate.validate_move(chess_board, "C7", "C5"))
    print("True validate move king C7 to C5", validate.validate_move(chess_board, "C7", "C5"))

    # print("====" * 30)
    print("Validate en_passant A2 to A4 is True", specialMove.en_passant(chess_board,"A8","A5"))
    # print("Validate A8 to B5 is False", validate._validate_rock_move(chess_board, "A8", "B5",))
