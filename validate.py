

def validate_move(chess_board, from_coordinate, to_coordinate):
    """"Validates a chess move in the given board.
    Returns true if everything is valid. Otherwise returns false"""

    #validate that from and to coordinates are on the board
    #if not _validate_coordinate(from_coordinate):
     #   return False

    #_validate_coordinate(from_coordinate)
    # if not from_coordinate in chess_board[from_coordinate]:
    #     print(from_coordinate)
    #     return False
    # if not to_coordinate in chess_board:
    #     print(to_coordinate)
    #     return False

    #validate that from coordinates are a chess piece
    from_piece = chess_board.get(from_coordinate)
    if from_piece == None:
        print("Are you blind! there's nothing here")
        return False

#    if from_piece == chess_board[from_coordinate]:
    return True


def _validate_coordinate(co_ordinate):
    pass