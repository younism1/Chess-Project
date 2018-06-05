def validate_move(chess_board, from_coordinate, to_coordinate):
    if not _validate_coordinate(from_coordinate):
        return False

    if not _validate_coordinate(to_coordinate):
        print("failed at 6")
        return False

    from_piece = chess_board.get(from_coordinate)
    if from_piece == None:
        print("Are you blind! there's nothing here")
        return False

    if chess_board.get(to_coordinate) != None:
        if from_piece[2] == chess_board.get(to_coordinate)[2]:
            return False

    from_column_number = coordinate_to_column_number(from_coordinate)
    to_column_number = coordinate_to_column_number(to_coordinate)

    if from_piece[0] == "K":
        return _validate_king_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "P":
        return _validate_pawn_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

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

def coordinate_to_column_number(coordinate):
    column = "ABCDEFGH"
    column_coordinate = column.index(coordinate[0])
    return  column_coordinate

def _validate_king_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    """"validate the from_coordinates is within  one of the to_coordinates"""

    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])

    if not (to_row -1 <= from_row <= to_row +1):
        return False

    if not (to_column_number -1 <= from_column_number <= to_column_number +1):
        return False

    return True


def _validate_pawn_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):

    from_piece_colour = chess_board.get(from_coordinates)[2]
    if from_piece_colour == "B":
        direction = -1
    else:
        direction = +1

    from_row = int(from_coordinates[1])
    to_row =int(to_coordinates[1])

    if chess_board.get(to_coordinates) is None:
        if not from_column_number == to_column_number:
            return False


"""adding things here to validate the last line in test Validate"""
    #     if to_row != from_row + direction:
    #         return False
    #
    # return True

