
en_passant = None


def special_move(chess_board, from_coordinates, to_coordinates, undo_move):
    if chess_board.get(from_coordinates) != None:
        to_row = int(to_coordinates[1])
        from_row = int(from_coordinates[1])

        if not ((chess_board.get(from_coordinates)[2] == "P")
                and undo_move ==(to_row == from_row + 2)
                     and (to_row - 1 == None)):
            return False


            return False
        elif chess_board.get(from_coordinates)[2] == "P" and to_row == from_row + 2:
            return True




