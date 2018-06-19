
en_passant = None


def special_move(chess_board, from_coordinates, to_coordinates, undo_move):
    global en_passant

    if chess_board.get(from_coordinates) != None:
        to_row = int(to_coordinates[1])
        from_row = int(from_coordinates[1])

        print(chess_board.get(from_coordinates)[0], " and ", to_coordinates == en_passant)
        if chess_board.get(from_coordinates)[0] == "P" and to_coordinates == en_passant:
            piece = chess_board.get(to_coordinates)
            chess_board[to_coordinates] = chess_board[from_coordinates]
            del chess_board[from_coordinates]

            en_passant_captured = to_coordinates[0] + str(to_row + 1)
            del chess_board[en_passant_captured]

            return True

        # if not ((chess_board.get(from_coordinates)[2] == "P")
        #         and undo_move ==(to_row == from_row + 2)
        #              and (to_row - 1 == None)):
        #     return False
        #
        #
        #     return False
        # el
        if chess_board.get(from_coordinates)[0]== "P" and to_row == from_row + 2:
            en_passant = from_coordinates[0] + str(to_row - 1)
            return False
        else:
            en_passant = None



    return False
            #undo_move.store_move(from_coordinates, to_coordinates, piece)








