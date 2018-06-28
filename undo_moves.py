undo_moves = []

def store_move(from_coordinates, to_coordinates, undo_piece):
    undo_moves.append((from_coordinates, to_coordinates, undo_piece))

    to_coordinates = from_coordinates

def undo_last_move(chess_board):
    from_coordinates, to_coordinates, undo_piece = undo_moves.pop()
    chess_board[from_coordinates] = chess_board[to_coordinates]
    chess_board[to_coordinates] = undo_piece


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


    store_move("H2", "H3", "P_W")
    print(undo_moves)

    test_chess_board = {"H3": "K_B"}
    print_board()

    undo_last_move(test_chess_board)
    print(test_chess_board)
    print(undo_moves)

    print_board()