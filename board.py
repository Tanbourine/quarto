#!/usr/bin/env python
# encoding: utf-8
"""
********************************************
* File Name : board.py

* Created By : Darren Tan

* Creation Date : 08-26-2019

* Last Modified : 09-10-2019::19:46:56 

* Purpose : Manage board state and determine win conditions
********************************************
"""


class Board(object):
    """ Manages the board state
        Creates new games, place pieces, determintes win conditions
    """
    # pylint: disable=superfluous-parens

    # origin (0, 0) is top left

    def __init__(self):
        # create board
        self.win = False
        self.library = []
        self.board = []
        self.new_game()

    def new_game(self):
        """ create a new game by resetting the board and library of pieces """
        self.create_board()
        self.create_pieces()
        self.win = False
        print("\n==============================\n")
        print("Welcome to Quarto!")
        print("Available Pieces: {}".format(self.library))
        print("Board:")
        self.disp_board()
        print("==============================\n")

    def create_board(self):
        """ populate a 4x4 matrix of -1s """
        self.board = [[-1 for _ in range(4)] for _ in range(4)]

    def create_pieces(self):
        """ create an array of 16 pieces to refer as ID """
        self.library = []
        for i in range(16):
            self.library.append(i)

    def disp_board(self):
        """ prints board state for visualization """
        for row in self.board:
            print row
        print "\n"

    def is_occupied(self, row, col):
        """ anybody home?
        since the board is initialized with -1s, as long as the value at a location
        is > 0, a piece has been placed there
        row (int): row value to be placed at
        col (int): col value to be placed at
        returns: bool
        """
        return self.board[row][col] > 0

    def is_available(self, piece):
        """ checks to see if the piece is in the library """
        return piece in self.library

    def place(self, piece, row, col):
        """
        place a piece down onto the board
        args:
        piece (int): unique id of a piece
        row (int): row to be placed at
        col (int): col to be placed at
        """

        success = False

        if self.is_occupied(row, col):
            print "INVALID MOVE"

        elif self.is_available(piece) is False:
            print "id={} IS NOT IN LIBRARY".format(piece)

        else:
            # if it's an valid move, place the piece and remove from library
            self.board[row][col] = piece
            self.library.remove(piece)
            success = True
            print("Placed {} on {}".format(piece, (row, col)))

        # show board state
        self.disp_board()

        # check for win conditions
        self.horiz_win()
        self.vert_win()
        self.diag_win_tl_to_br()
        self.diag_win_bl_to_tr()

        return success

    def horiz_win(self):
        """ check each row of the board for win conditions"""
        for i in range(4):
            win_cond, pieces = check_win_cond(self.board[i])
            if win_cond:
                self.game_over(win_cond, pieces, 'horizontal')
                break

    def vert_win(self):
        """ check each column for win conditions """
        for i in range(4):
            # row[i] will return a column
            pieces = [row[i] for row in self.board]
            win_cond, pieces = check_win_cond(pieces)
            if win_cond:
                self.game_over(win_cond, pieces, 'vertical')
                break

    def diag_win_tl_to_br(self):
        """ check diagonals from top left to bottom right for win conditions """
        pieces = []
        for i in range(4):
            pieces.append(self.board[i][i])

        win_cond, pieces = check_win_cond(pieces)
        if win_cond:
            self.game_over(win_cond, pieces, 'diag_tl_to_br')

    def diag_win_bl_to_tr(self):
        """ check diagonals from bottom left to top right for win conditions """
        pieces = []
        for i in range(4):
            # start from bottom left
            pieces.append(self.board[3-i][i])

        win_cond, pieces = check_win_cond(pieces)
        if win_cond:
            self.game_over(win_cond, pieces, 'diag_bl_to_tr')

    def game_over(self, win_cond, pieces, direction):
        """ print win condition and show board """
        self.win = True
        prop = bin2prop(win_cond)
        print("\n==============================\n")
        print("Game Over!")
        print("Win Direction: {}".format(direction))
        print("Conditions: {}".format(prop))
        print("Pieces: {}".format(pieces))
        print("\nBoard:")
        self.disp_board()


def check_win_cond(pieces):
    """ receives four pieces as arg and checks to see if they have matching features """
    # make sure we're getting 4 pieces to check
    assert len(pieces) == 4, "DID NOT PASS 4 PIECES TO CHECK"

    # filter out -1's
    for piece in pieces:
        if piece < 0:
            return 0, pieces

    # xnor each piece with its neighbor
    xnor_01 = xnor(pieces[0], pieces[1])
    xnor_12 = xnor(pieces[1], pieces[2])
    xnor_23 = xnor(pieces[2], pieces[3])

    # bitwise and all the xnors together to see which match
    win_cond = (xnor_01 & xnor_12 & xnor_23)

    # print debug statements
    # print("Pieces: {}".format(pieces))
    # print("XNOR_01: {0:4b}".format(xnor_01))
    # print("XNOR_12: {0:4b}".format(xnor_12))
    # print("XNOR_23: {0:4b}".format(xnor_23))
    # print("win_cond: {0:4b}".format(win_cond))

    return win_cond, pieces


def xnor(a, b):
    # pylint: disable=invalid-name
    """ standard xnor logic gate, tuned for python's weirdness """
    # Truth table
    # A | B | Result
    # -------------
    # 0 | 0 | 1
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1
    return 0b1111 - (a ^ b)


def bin2prop(piece):
    """ prints win condition back in ASCII """
    prop = []
    if piece & 0b1000:
        prop.append('SHAPE')

    if piece & 0b0100:
        prop.append('COLOR')

    if piece & 0b0010:
        prop.append('INDENT')

    if piece & 0b0001:
        prop.append('HATCH')

    # print("PROP: {}".format(prop))

    return prop


def main():
    """ main runtime execution """
    board = Board()

    # horizontal win with zeros
    # board.place(4, 0, 0)
    # board.place(1, 0, 1)
    # board.place(2, 0, 2)
    # board.place(3, 0, 3)

    #####################

    # horizontal win with ones
    # board.place(15, 1, 1)
    # board.place(14, 1, 2)
    # board.place(13, 1, 3)
    # board.place(12, 1, 0)

    #####################

    # vertical win
    # board.place(15, 0, 3)
    # board.place(14, 1, 3)
    # board.place(13, 2, 3)
    # board.place(12, 3, 3)

    # diag tl to br win
    # board.place(2, 0, 0)
    # board.place(3, 1, 1)
    # board.place(6, 2, 2)
    # board.place(7, 3, 3)

    # diag bl to tr win
    board.place(1, 3, 0)
    board.place(3, 2, 1)
    board.place(5, 1, 2)
    board.place(7, 0, 3)


if __name__ == '__main__':
    main()
