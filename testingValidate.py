import validate
import specialMove
import undo_moves

if __name__ == "__main__":
    chess_board = {"A2": "P_W",
                   "B4": "P_B",
                   "H7": "P_B",
                   "G5": "P_W",
                   "C3": "K_W",
                   "F8":"K_B",
                   "C7": "P_B",
                   "A8": "C_B",
                   "A6": "C_B",
                   "B6": "C_W",
                   "A7": "P_W",
                   "D1": "Q_W"}

    # print("====" * 30+"Special move")
    # print("Validate en_passant A2 to A4 is False", specialMove.special_move(chess_board,"A2","A4"))
    # print(specialMove.en_passant)
    # chess_board["A4"] = chess_board["A2"]
    # del chess_board["A2"]
    # print("Validate en_passant B4 to A3 is True", specialMove.special_move(chess_board,"B4","A3"))
    # print(chess_board)

    print()
    print("Validate en_passant BLACK! H7 to H5 is False", specialMove.special_move(chess_board,"H7","H5"))
    print(specialMove.en_passant)
    chess_board["H5"] = chess_board["H7"]
    del chess_board["H7"]
    print("Validate en_passant BLACK! G5 to H6 is True", specialMove.special_move(chess_board,"G5","H6"))
    print(chess_board)
    print("====" * 30)
    print(undo_moves.undo_moves)
    undo_moves.undo_last_move(chess_board)
    print(chess_board)
    print(undo_moves.undo_moves)

    print("====" * 30)

    print("====" * 30+"validate")
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

    chess_board = {"A2": "P_W",
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

    print("True validate move pawn A2 to A3", validate.validate_move(chess_board, "A2", "A3"))
    print("False validate move pawn A2 to A7", validate.validate_move(chess_board, "A2", "A7"))
    print("True validate move pawn A2 to A4", validate.validate_move(chess_board, "A2", "A4"))
    #print("True validate move king A7 to A6", validate.validate_move(chess_board, "A7", "A6"))
    print("False validate move pawn A2 to A1", validate.validate_move(chess_board, "A2", "A1"))
    print("True validate move pawn C7 to C5", validate.validate_move(chess_board, "C7", "C5"))
    print("True validate move king C7 to C5", validate.validate_move(chess_board, "C7", "C5"))

    print("_validate_rock_move A8 to B3 False", validate._validate_rook_move(chess_board, "A8", "B3", 0, 1))
    print("_validate_rock_move A8 to A3 True", validate._validate_rook_move(chess_board, "A8", "A3", 0, 0))
    print("_validate_rock_move A8 to C8 True", validate._validate_rook_move(chess_board, "A8", "C8", 0, 2))
    print("====" * 30)
    print("_validate_rock_move A8 to A5 False", validate._validate_rook_move(chess_board, "A8", "A5", 0, 0))
    print("====" * 30)
    print("_validate_rock_move A6 to E6 False", validate._validate_rook_move(chess_board, "A6", "E6", 0, 4))

    print("==== HOME WORK " * 30)
    del chess_board["A7"]
    print("_validate_rock_move A6 to B6 True", validate._validate_rook_move(chess_board, "A6", "B6", 0, 1))
    print("_validate_rock_move A8 to A6 False", validate._validate_rook_move(chess_board, "A8", "A6", 0, 0))
    print("==== " * 30)

    print("validate move with rook validation False", validate.validate_move(chess_board, "A8", "A6"))

    print("_validate_rock_move A8 to C8 True", validate.validate_move(chess_board, "A8", "C8"))
    print("_validate_rock_move A8 to A5 False", validate.validate_move(chess_board, "A8", "A5"))
    print("_validate_rock_move A6 to E6 False", validate.validate_move(chess_board, "A6", "E6"))
    # print("Validate A8 to B5 is False", validate._validate_rock_move(chess_board, "A8", "B5"))
    print("==== " * 30)
    print("Validate SPECAIL MOVE BLACK! G5 to H6 is True", specialMove.special_move(chess_board, "G5", "H6"))
    print("==== " * 30)
    print("_validate_bishop_move C1 to A3", validate.validate_move(chess_board, "C1", "A3"))

    # print("==== " * 30)
    # print("_validate_queen_move D1 to D3", validate.validate_move(chess_board, "D1", "D3"))
    # print("_validate_queen_move D3 to F6", validate.validate_move(chess_board, "D3", "F6", 3, 5))