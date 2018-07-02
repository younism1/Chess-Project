undo_moves = []

def store_move(from_coordinates, to_coordinates, undo_piece):
    undo_moves.append([(from_coordinates, to_coordinates, undo_piece)])
    to_coordinates = from_coordinates

def store_multi_move #new function to store multi moves

def undo_last_move(chess_board):
    sub_moves = undo_moves.pop()
    for sub_move in sub_moves:

        from_coordinates, to_coordinates, undo_piece = sub_move

        if not from_coordinates == None and chess_board.get(to_coordinates) != None:
            chess_board[from_coordinates] = chess_board[to_coordinates]

        if undo_piece != None:
            chess_board[to_coordinates] = undo_piece
        elif chess_board.get(to_coordinates) != None:
            del chess_board[to_coordinates]

if __name__ == "__main__":

    test_chess_board = {"H3": "K_B"}

    def print_board():

        print(" A   B   C   D   E   F   G   H")

        for row in range(1, 9):
            for column in "ABCDEFGH":
                key = column + str(row)
                chess_space = test_chess_board.get(key)
                if chess_space is None:
                    print("   |", end="")
                else:
                    print(chess_space, end=" ")

            print(row)


    store_move("H1", "H2", None)
    store_move("H2", "H3", "P_W")
    print(undo_moves)
    undo_last_move(test_chess_board)
    print(test_chess_board)
    print("="*40)
    #
    # undo_last_move(test_chess_board)
    # print(test_chess_board)
    # print("="*40)

    test_chess_board = {"H3": "K_B"}#,
                        #"H7": "W_P"}

    print_board()

    undo_last_move(test_chess_board)
    print(test_chess_board)
    print(undo_moves)

    print_board()