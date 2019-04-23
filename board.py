#!/usr/bin/env python
# encoding: utf-8


import piece

class Board(object):

    #origin (0, 0) is top left

    def __init__(self):
        # create board
        self.board = [[-1 for col in range(4)] for row in range(4)]
        self.library = create_pieces()

    def disp_board(self):
        for row in self.board:
            print row
        print "\n"

    def get_matching_pieces(self, property):
        # this fails if you try to match with 0b0000
        matching_pieces = []
        for piece in self.library:
            if piece & property:
                matching_pieces.append(piece)
        return matching_pieces

    def is_occupied(self, x, y):
        """ anybody home?

        x (int): x value to be placed at
        y (int): y value to be placed at

        returns: bool
        """
        return self.board[x][y] > 0

    def is_available(self, id):
        return id in self.library


    def place(self, id, x, y):
        """ place a piece down onto the board
        id (int): unique id of a piece
        x (int): x value to be placed at
        y (int): y value to be placed at

        """
        if self.is_occupied(x, y):
            print "INVALID MOVE"

        elif self.is_available(id) is False:
            print "id={} IS NOT IN LIBRARY".format(id)

        else:
            self.board[x][y] = id
            self.library.remove(id)

        # print(self.board)
        self.disp_board()
        win_cond, win_pieces = self.horiz_win()
        if win_cond:
            print "you win!"
            print win_cond, win_pieces

        # self.game_over(self.is_win_cond())
        # if self.is_win_cond():
        #     self.game_over(0b0100)


    def horiz_win(self):
        for i in range(4):
            # xnor entire row
            win_cond = xnor(self.board[i])
            if win_cond:
                return win_cond, self.board[i]




    def is_win_cond(self):
        winning_pieces = []
        for i in range(4):
            if not(self.board[i][0] ^ self.board[i][1] ^ self.board[i][2] ^ self.board[i][3]):
                win_dir = 'horizontal'
                winning_pieces.append(self.board[i])
                print winning_pieces
                win_cond = self.which_win_cond(winning_pieces)
                return win_cond

            if not(self.board[0][i] ^ self.board[1][i] ^ self.board[2][i] ^ self.board[3][i]):
                win_dir = 'vertical'
                return True

            if not (self.board[0][0] ^ self.board[1][1] ^ self.board[2][2] ^ self.board[3][3]):
                win_dir = 'diag_down'
                return True

            if not (self.board[3][3] ^ self.board[2][2] ^ self.board[1][1] ^ self.board[0][0]):
                win_dir = 'diag_up'
                return True

            # horiz_win = self.board[i][0] & self.board[i][1] & self.board[i][2] & self.board[i][3]
            # vert_win = self.board[0][i] & self.board[1][i] & self.board[2][i] & self.board[3][i]
            # diag_down_win = self.board[0][0] & self.board[1][1] & self.board[2][2] & self.board[3][3]
            # diag_up_win = self.board[3][3] & self.board[2][2] & self.board[1][1] & self.board[0][0]

        return False


    def which_win_cond(self, win_pieces):
        assert len(win_pieces) == 4, "DOES NOT HAVE 4 PIECES"

        return win_pieces[0] & win_pieces[1] & win_pieces[2] & win_pieces[3]

    def game_over(self, win_cond):
        if win_cond & 0b1000:
            print "GAME OVER!!\nWIN CONDITION: SHAPE"

        elif win_cond & 0b0100:
            print "GAME OVER!!\nWIN CONDITION: COLOR"

        elif win_cond & 0b0010:
            print "GAME OVER!!\nWIN CONDITION: INDENT"

        elif win_cond & 0b0001:
            print "GAME OVER!!\nWIN CONDITION: HATCH"

def create_pieces():
    library = []

    for i in range(16):
        library.append(i)
    return library


def xnor(*args):
    # Truth table
    # A | B | Result
    # -------------
    # 0 | 0 | 1
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1
    for piece in args:
        if piece < 0:
            return 0
    val = args[0]
    for i in range(1, len(args)):
        val = 0b1111 -(val ^ args[i])
    return val

def bit_and(*args):
    val = args[0]
    for i in range(1, len(args)):
        val = val & args[i]
    # print(bin(val))
    return val






def main():
    board = Board()

    # print(board.get_matching_pieces(0b0000))
    # horizontal win with zeros
    print("Place 1")
    board.place(4, 0, 0)
    print("Place 2")
    board.place(1, 0, 1)
    print("Place 3")
    board.place(2, 0, 2)
    print("Place 4")
    board.place(3, 0, 3)
    # horizontal win
    # board.place(15, 1, 1)

    # board.place(14, 1, 2)

    # board.place(13, 1, 3)

    # board.place(12, 1, 0)
    #####################


if __name__ == '__main__':
    main()
