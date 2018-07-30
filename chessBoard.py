from validate import validate_move, ValidationException
import undoMoves
import traceback as tb
import specialMove

#Generates the board and populate it with pieces.
def generate_board():
    global chess_board
    chess_board = {"A1": "C_W", "B1": "H_W"}

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

def process_command(command_input):
    if command_input == "QUIT":
        quit()

    if command_input == "UNDO":
        undoMoves.undo_last_move(chess_board)
        return False
    return True
#taking from coordiantes and moving piece to the to cooridantes
def move_piece(from_coordinates, to_coordinates):
    global chess_board
    piece =  chess_board.get(to_coordinates)
    chess_board[to_coordinates] = chess_board[from_coordinates]
    print(chess_board[from_coordinates])
    del chess_board[from_coordinates]
    undoMoves.store_move(from_coordinates, to_coordinates, piece)
#imports validation at the top and validates
def validate_and_move_piece(from_coordiantes, to_coordinates):
    """imports validation at the top and validates """
    #validate

    if from_coordiantes == None:
        return  False
            #     to_coordinates = None:
            # return False

    if not special_move_manager.check_and_move(from_coordinates, to_coordinates):
        try:
            validate_move(chess_board, from_coordiantes, to_coordinates)
            move_piece(from_coordiantes, to_coordinates)
    # except IndexError("Please enter a coordinate using, once character and one number from the grid")

        except ValidationException as e:
            tb.print_exc()
            print(e)

generate_board()
special_move_manager = specialMove.SpecialMoveManager(chess_board)

print_board()

while True:
    from_coordinates = input("from:  ").strip(" ").upper()
    if process_command(from_coordinates):
        print("You're moving:", chess_board.get(from_coordinates))
        to_coordinates = input("to:  ").strip(" ").upper()

        validate_and_move_piece(from_coordinates, to_coordinates)
        #move_piece_new(from_coordinates, to_coordinates)
    print_board()
