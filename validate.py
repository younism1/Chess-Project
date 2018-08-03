def validate_move(chess_board, from_coordinate, to_coordinate):
    """white piece moves first - can work this out by having """
    if not _validate_coordinate(from_coordinate):
        raise ValidationException("Please enter valid coordinates")

    if not _validate_coordinate(to_coordinate):
        print("failed at line 6", to_coordinate)
        raise ValidationException("Please enter valid coordinates")

    from_piece = chess_board.get(from_coordinate)
    if from_piece == None:
        print("Are you blind! there's nothing here")
        raise ValidationException("Please enter valid coordinates")

    if chess_board.get(to_coordinate) != None:
        if from_piece[2] == chess_board.get(to_coordinate)[2]:
            raise ValidationException("Please enter valid coordinates")

    from_column_number = coordinate_to_column_number(from_coordinate)
    to_column_number = coordinate_to_column_number(to_coordinate)

    if from_piece[0] == "K":
        return _validate_king_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "P":
        return _validate_pawn_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "C":
        return _validate_rook_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "B":
        return _validate_bishop_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "Q":
        return _validate_queen_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    elif from_piece[0] == "H":
        return _validate_knight_move(chess_board, from_coordinate, to_coordinate, from_column_number, to_column_number)

    return True

def _validate_coordinate(coordinate):

    if not len(coordinate) == 2:
        raise ValidationException("make sure you enter a 2 character coordinate")
    if not coordinate[0] in "ABCDEFGH":
        print("not valid column")
        raise ValidationException("Please enter valid coordinates")
    if not coordinate[1] in "12345678":
        print("not valid row")
        raise ValidationException("Please enter valid coordinates")
    if len(coordinate) != 2:
        raise ValidationException("Please enter valid coordinates")
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
        raise ValidationException("Please enter valid coordinates")

    if not (to_column_number -1 <= from_column_number <= to_column_number +1):
        raise ValidationException("Please enter valid coordinates")

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
            raise ValidationException("Please enter valid coordinates")

            """if to_co-ordinate is diagonally forward from from position"""
        # direction = from_column_number
    if ((from_column_number == to_column_number +1 or from_column_number == to_column_number -1) \
                and to_row == from_row + direction) and chess_board.get(to_coordinates) == None:
        raise ValidationException("Please enter valid coordinates")

# """adding things here to validate the last line in test Validate using ands AND ors"""
    if not (to_row == from_row + direction
        or ((from_row == 7 or from_row == 2) and to_row == from_row + (direction * 2))):

        raise ValidationException("Not a standard pawn move")


    return True

def _validate_rook_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    # from_piece_colour = chess_board.get(from_coordinates)[2]
    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])
    if not (from_column_number == to_column_number or from_row == to_row):
        raise ValidationException("Please enter valid coordinates")

    if not from_row == to_row:
        if from_row >= to_row:
            x = range(to_row+1, from_row)
        else:
            x = range(from_row+1, to_row)

        for i in x:
            test_coordiante = from_coordinates[0]+ str(i)
            if chess_board.get(test_coordiante) != None:
                raise ValidationException("Please enter valid coordinates")

    else:
        if from_column_number >= to_column_number:
            y = range(to_column_number + 1, from_column_number)
        else:
            y = range(from_column_number + 1, to_column_number)

        for i in y:
            test_coordiante = "ABCDEFGH"[i] + from_coordinates[1]
            if chess_board.get(test_coordiante) != None:
                raise ValidationException("Please enter valid coordinates")

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

def _validate_bishop_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    # bishop = chess_board.get(from_coordinates)[0] == "B"
    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])

    move = [(to_column_number - from_column_number),(to_row - from_row)]

    if not abs(move[0]) == abs(move[1]):
        raise ValidationException("Please enter valid coordinates")
    return True

def _validate_knight_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    from_row = int(from_coordinates[1])
    to_row = int(to_coordinates[1])

    move = [abs(to_column_number - from_column_number), abs(to_row - from_row)]

    if not (move[0] == 1 and move[1] == 2 or move[0] == 2 and move[1] == 1):
        raise ValidationException("Please enter valid coordinates")
    return True

def _validate_queen_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number):
    # from_coordiantes = chess_board.get(from_coordinates)
    # to_coordiantes = chess_board.get(to_coordinates)

    return _validate_rook_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number)\
        or _validate_bishop_move(chess_board, from_coordinates, to_coordinates, from_column_number, to_column_number)


    # if not _validate_rook_move(che)

class ValidationException(Exception):
    pass