import validate

if __name__ == "__main__":
    chess_board = {"A2": "P_W",
                   "C3": "K_W"}
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
    print("False validate move pawn", validate.validate_move(chess_board, "A2", "D4"))
    print("False validate move king", validate.validate_move(chess_board, "A2", "A7"))
    print("True validate move king", validate.validate_move(chess_board, "A2", "A4"))




