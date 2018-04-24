import validate

#CREATING A DICTIONARY FOR CHESS BOARD.
chess_board = {}

#CREATING A FUNCTION TO POPULATE CHESS BOARD.
def populate_board():

    chess_board["A1"] = "C_W"
    chess_board["B1"] = "H_W"
    chess_board["C1"] = "B_W"
    chess_board["D1"] = "Q_W"
    chess_board["E1"] = "K_W"
    chess_board["F1"] = "B_W"
    chess_board["G1"] = "H_W"
    chess_board["H1"] = "C_W"

    chess_board["A2"] = "P_W"
    chess_board["B2"] = "P_W"
    chess_board["C2"] = "P_W"
    chess_board["D2"] = "P_W"
    chess_board["E2"] = "P_W"
    chess_board["F2"] = "P_W"
    chess_board["G2"] = "P_W"
    chess_board["H2"] = "P_W"

    chess_board["A7"] = "P_B"
    chess_board["B7"] = "P_B"
    chess_board["C7"] = "P_B"
    chess_board["D7"] = "P_B"
    chess_board["E7"] = "P_B"
    chess_board["F7"] = "P_B"
    chess_board["G7"] = "P_B"
    chess_board["H7"] = "P_B"

    chess_board["A8"] = "C_B"
    chess_board["B8"] = "H_B"
    chess_board["C8"] = "B_B"
    chess_board["D8"] = "Q_B"
    chess_board["E8"] = "K_B"
    chess_board["F8"] = "B_B"
    chess_board["G8"] = "H_B"
    chess_board["H8"] = "C_B"

populate_board()

#CREATING A FUNCTION TO PRINT THE CHESS BOARD ON CONSOLE,
#SO IT MAKES SENSE TO HUMAN.
def print_board():

    print(" A   B   C   D   E   F   G   H")

    for row in range (1,9):
        for column in "ABCDEFGH":
            key = column + str(row)
            chess_space = chess_board.get(key)
            if chess_space is None:
                print("   |", end = "")
            else:
                print(chess_space, end= " ")

        print(row)

# print_board()

# CREATING A FUNCTION TO MOVE THE CHESS PIECES ON THE BOARD.
# def move_piece_old():
#     global chess_board
#
#     #TAKES "INPUT" FOR FROM COORDINATES.
#     from_coordinates = input("From: ")
#
#     #DEFINED THE VALUE FOR FROM COORDINATES.
#     from_coordinates_value = chess_board[from_coordinates]
#     print("You're moving:",from_coordinates_value)
#
#     #TAKES "INPUT" FOR TO COORDINATES AND REPLACES VALUE WITH FROM COORDINATES VALUE.
#     to_coordinates = input("To: ")
#     chess_board[to_coordinates] = from_coordinates_value
#
#     #DELETE FROM_COORDINATES VALUE.
#     del chess_board[from_coordinates]
#     print_board()
#
#     #CALLING FUNCTION WITHIN FUNCTION AT THE END TO LOOP.
#     #move_piece()

def move_piece_new(from_coordinates, to_coordinates):

    piece =  chess_board[from_coordinates]
    chess_board[to_coordinates] = chess_board[from_coordinates]
    print(chess_board[from_coordinates])
    del chess_board[from_coordinates]


def validate_and_move_piece(from_coordiantes, to_coordinates):
    #validate
    if validate.validate_move(chess_board, from_coordiantes, to_coordinates):
        move_piece_new(from_coordiantes, to_coordinates)
    else:
        print("WHAT ARE YOU DOING?? \n TRY AGAIN! \n FAILED VALIDATION")
    #if it's valid move the piece

# move_piece_new()
# validate_and_move_piece()
print_board()

while True:
    from_coordinates = input("from:  ")
    print("You're moving:", chess_board.get(from_coordinates))
    to_coordinates = input("to:  ")

    validate_and_move_piece(from_coordinates, to_coordinates)
    #move_piece_new(from_coordinates, to_coordinates)
    print_board()

    if from_coordinates == "quit":
        break
