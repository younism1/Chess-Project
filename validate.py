

def validate_move(chess_board, from_coordinate, to_coordinate):
    if not _validate_coordinate(from_coordinate):
        return False

    if not _validate_coordinate(to_coordinate):
        print("failed at line 6", to_coordinate)
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

    elif from_piece[0] == "C":
        return _validate_rook_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    return True
"""add the validation for cooridantes and make sure it runs without a pass, test below"""
def _validate_coordinate(coordinate):
    if not coordinate[0] in "ABCDEFGH":
        print("not valid column")
        return False
    if not coordinate[1] in "12345678":
        print("not valid row")
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
    to_row = int(to_coordinates[1])

    if chess_board.get(to_coordinates) is None:
        if not from_column_number == to_column_number:

            """if to_co-ordinate is diagonally forward from from position"""
        # direction = from_column_number
        if ((from_column_number == to_column_number +1 or from_column_number == to_column_number -1) \
                and to_row == from_row + direction) and chess_board.get(to_coordinates) != None:
            return True

            """if its not black make """
            return False

# """adding things here to validate the last line in test Validate using ands AND ors"""
        if not (to_row == from_row + direction
                or ((from_row == 7 or from_row == 2) and to_row == from_row + (direction * 2))):
            return False
    return True

def _validate_rook_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    from_piece_colour = chess_board.get(from_coordinates)[2]
    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])
    # if chess_board.get(to_coordinates) is None:
    if not (from_column_number == to_column_number or from_row == to_row):
        #        and chess_board.get(to_coordinates) != None or :
        return False

    if not from_row == to_row:
        if from_row >= to_row:
            x = range(to_row+1, from_row)
        else:
            x = range(from_row+1, to_row)

        for i in x:
            test_coordiante = from_coordinates[0]+ str(i)
            if chess_board.get(test_coordiante) != None:
                return False

    else:
        if from_column_number >= to_column_number:
            y = range(to_column_number + 1, from_column_number)
        else:
            y = range(from_column_number + 1, to_column_number)

        for i in y:
            test_coordiante = "ABCDEFGH"[i] + from_coordinates[1]
            if chess_board.get(test_coordiante) != None:
                return False

    # print("x",x)
    # y = range(from_column_number, to_column_number)
    # print("y",y)
    # from_coordinates = from_column_number and from_row
    # print("from coord",from_coordinates)
    # to_coordinates = to_column_number and to_row
    # print("to coord",to_coordinates)
    #
    # if from_column_number == to_column_number:
    #     x +
    #     return False
    return True

    # if not from_row == to_row:
    #
    #
    # if not to_column_number == from_column_number:
    #     return False

    # from_column_number = chess_board.get(from_coordinates[0] == int(from_coordinates[0]))
    # to_column_number = chess_board.get(to_coordinates[0] == int(to_coordinates[0]))
    #
    # if not to_coordinates == None \
    #         and from_column_number == to_column_number or from_coordinates[1] == to_coordinates[1]:
    #         return False

    # from_piece_colour = chess_board.get(from_coordinates)[2]
    # if from_piece_colour == "B":
    #     direction = range(1,8)
    # else:
    #     direction = range(1,8)
    #
    # from_row = int(from_coordinates[1])
    # to_row = int(to_coordinates[1])
    #
    # if chess_board.get(to_coordinates)is None:
    #     if not from_column_number == to_column_number:
    #         return False
    #
    #     if not to_row == from_row + direction:
    #         return False

