def validate_move(chess_board, from_coordinate, to_coordinate):
    if not _validate_coordinate(from_coordinate):
        return False

    if not _validate_coordinate(to_coordinate):
        return False

    from_piece = chess_board.get(from_coordinate)
    if from_piece == None:
        print("Are you blind! there's nothing here")
        return False
    # x = chess_board.get(to_coordinate)[2]
    # print(x)

    if chess_board.get(to_coordinate) != None:
        if from_piece[2] == chess_board.get(to_coordinate)[2]:
            return False

    if from_piece[0] == "K":
        return _validate_king_move(from_piece,chess_board, from_coordinate, to_coordinate)

    return True

"""add the validation for cooridantes and make sure it runs without a pass, test below"""


def _validate_coordinate(coordinate):
    if not coordinate[0] in "ABCDEFGH":
        print("not valid")
        return False
    if not coordinate[1] in "12345678":
        print("not valid")
        return False
    if len(coordinate) != 2:
        return False
    return True

# def _validate_king_move(from_coordinate, to_coordinate):

def _validate_king_move(from_piece, chess_board, from_coordinates, to_coordinates):
    """"validate the from_coordinates is within  one of the to_coordinates"""

    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])

    if not (to_row -1 <= from_row <= to_row +1):
        return False

    # from_column = int(from_coordinates[0])
    # to_column = int(to_coordinates[0])

#    from_column = "ABCDEFGH"

#     if not from_coordinates[1]
#     nd to_coordinates[1]
#
    return True

if __name__ == "__main__":
    chess_board = {"A2": "P_W"}
    print("A2", validate_move(chess_board, "A2", "A3"))
    print("====" * 30)
    print(validate_move(chess_board, "H9", "cheese"))
    print("====" * 30)
    print(validate_move(chess_board, "E1", "E3"))
    print("====" * 30)

    chess_board["C3"] = "K_W"
    print("True validate king", _validate_king_move("K_W", chess_board, "C3", "D4"))
    print("False validate king", _validate_king_move("K_W", chess_board, "C3", "D7"))
    print("False validate king", _validate_king_move("K_W", chess_board, "C3", "H3"))