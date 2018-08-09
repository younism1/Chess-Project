import undoMoves

class SpecialMoveManager(object):

    def __init__(self, chess_board):
        self.en_passant = None
        self.chess_board = chess_board


    def check_and_move(self, from_coordinates, to_coordinates):
        try:

            return self._check_move_en_passant(from_coordinates, to_coordinates) \
                   or self._check_and_move_promotion(from_coordinates, to_coordinates)
        except Exception as a:
            print(a)


        return False
            #undo_move.store_move(from_coordinates, to_coordinates, piece)


    def _check_move_en_passant(self, from_coordinates, to_coordinates):

            if self.chess_board.get(from_coordinates) != None:
                to_row = int(to_coordinates[1])
                from_row = int(from_coordinates[1])
                # print(chess_board.get(from_coordinates)[0], " and ", to_coordinates == en_passant)
                if self.chess_board.get(from_coordinates)[0] == "P" and to_coordinates == self.en_passant:
                    piece = self.chess_board.get(to_coordinates)
                    self.chess_board[to_coordinates] = self.chess_board[from_coordinates]
                    del self.chess_board[from_coordinates]

                    en_passant_captured = to_coordinates[0] + from_coordinates[1]

                    undoMoves.store_multi_move(from_coordinates, to_coordinates,
                                               en_passant_captured, self.chess_board[en_passant_captured])

                    del self.chess_board[en_passant_captured]

                    return True

                if self.chess_board.get(from_coordinates)[0] == "P" and abs(to_row - from_row) == 2:
                    en_passant = from_coordinates[0] + str((to_row + from_row) // 2)

                    return False
                else:
                    en_passant = None

    def _check_and_move_promotion(from_coordinates, to_coordinates) :



        return False







