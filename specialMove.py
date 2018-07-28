import undoMoves

en_passant = None

def special_move(chess_board, from_coordinates, to_coordinates):
    global en_passant
    try:
        if chess_board.get(from_coordinates) != None:
            to_row = int(to_coordinates[1])
            from_row = int(from_coordinates[1])
            #print(chess_board.get(from_coordinates)[0], " and ", to_coordinates == en_passant)
            if chess_board.get(from_coordinates)[0] == "P" and to_coordinates == en_passant:
                piece = chess_board.get(to_coordinates)
                chess_board[to_coordinates] = chess_board[from_coordinates]
                del chess_board[from_coordinates]

                en_passant_captured = to_coordinates[0] + from_coordinates[1]

                undoMoves.store_multi_move(from_coordinates, to_coordinates, None, None,
                                           en_passant_captured, chess_board[en_passant_captured])

                del chess_board[en_passant_captured]

                return True


            if chess_board.get(from_coordinates)[0] == "P" and abs(to_row - from_row) == 2:
                en_passant = from_coordinates[0] + str((to_row + from_row)//2)

                return False
            else:
                en_passant = None

    except Exception as a:
        print(a)


    return False
            #undo_move.store_move(from_coordinates, to_coordinates, piece)








