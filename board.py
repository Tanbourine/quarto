#!/usr/bin/env python
# encoding: utf-8


import piece


class Board(object):

    # origin (0, 0) is top left

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

    def is_occupied(self, row, col):
        """ anybody home?
        row (int): row value to be placed at
        col (int): col value to be placed at
        returns: bool
        """
        return self.board[row][col] > 0

    def is_available(self, id):
        return id in self.library

    def place(self, id, row, col):
        """ place a piece down onto the board
        id (int): unique id of a piece
        row (int): row to be placed at
        col (int): col to be placed at
        """
        if self.is_occupied(row, col):
            print "INVALID MOVE"

        elif self.is_available(id) is False:
            print "id={} IS NOT IN LIBRARY".format(id)

        else:
            # if it's an valid move, place the piece and remove from library
            self.board[row][col] = id
            self.library.remove(id)

        # show board state
        self.disp_board()

        # check for win conditions
        self.horiz_win()
        self.vert_win()
        self.diag_win_tl_to_br()
        self.diag_win_bl_to_tr()

    def horiz_win(self):
        for i in range(4):
            win_cond, pieces = check_win_cond(self.board[i])
            if win_cond:
                self.game_over(win_cond, pieces, 'horizontal')
                break

    def vert_win(self):
        for i in range(4):
            pieces = [col[i] for col in self.board]
            win_cond, pieces = check_win_cond(pieces)
            if win_cond:
                self.game_over(win_cond, pieces, 'vertical')
                break

    def diag_win_tl_to_br(self):
        pieces = []
        for i in range(4):
            pieces.append(self.board[i][i])

        win_cond, pieces = check_win_cond(pieces)
        if win_cond:
            self.game_over(win_cond, pieces, 'diag_tl_to_br')

    def diag_win_bl_to_tr(self):
        pieces = []
        for i in range(4):
            pieces.append(self.board[3-i][i])

        win_cond, pieces = check_win_cond(pieces)
        if win_cond:
            self.game_over(win_cond, pieces, 'diag_bl_to_tr')

    def game_over(self, win_cond, pieces, direction):
        prop = bin2prop(win_cond)
        print("\n==============================\n")
        print("Game Over!")
        print("Win Direction: {}".format(direction))
        print("Conditions: {}".format(prop))
        print("Pieces: {}".format(pieces))
        print("\nBoard:")
        self.disp_board()


def create_pieces():
    library = []

    for i in range(16):
        library.append(i)
    return library


def check_win_cond(pieces):
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
    # Truth table
    # A | B | Result
    # -------------
    # 0 | 0 | 1
    # 0 | 1 | 0
    # 1 | 0 | 0
    # 1 | 1 | 1
    return 0b1111 - (a ^ b)


def bin2prop(id):
    prop = []
    if id & 0b1000:
        prop.append('SHAPE')

    if id & 0b0100:
        prop.append('COLOR')

    if id & 0b0010:
        prop.append('INDENT')

    if id & 0b0001:
        prop.append('HATCH')

    # print("PROP: {}".format(prop))

    return prop


def main():
    board = Board()

    # print(board.get_matching_pieces(0b0000))

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
