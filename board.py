#!/usr/bin/env python
# encoding: utf-8
"""
********************************************
* File Name : board.py

* Created By : Darren Tan

* Creation Date : 04-21-2019

* Last Modified : 04-21-2019::04:09:23 PDT

* Purpose : Keeping track of all the pieces in play
********************************************
"""


# custom modules
import piece

class Board(object):

    #origin (0, 0) is top left

    def __init__(self):
        self.board = [[0 for col in range(4)] for row in range(4)]
        self.library = create_pieces()

    def disp_board(self):
        for row in self.board:
            print row
        print "\n"


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
            print "PIECE IS NOT IN LIBRARY"

        else:
            self.board[x][y] = self.library.pop(id)

        # print(self.board)
        self.disp_board()
        self.game_over(self.win_cond())



    def win_cond(self):
        for i in range(4):
            horiz_win = self.board[i][0] & self.board[i][1] & self.board[i][2] & self.board[i][3]
            vert_win = self.board[0][i] & self.board[1][i] & self.board[2][i] & self.board[3][i]
            diag_down_win = self.board[0][0] & self.board[1][1] & self.board[2][2] & self.board[3][3]
            diag_up_win = self.board[3][3] & self.board[2][2] & self.board[1][1] & self.board[0][0]

            if horiz_win:
                return horiz_win
            if vert_win:
                return vert_win
            if diag_down_win:
                return diag_down_win
            if diag_up_win:
                return diag_up_win
        return 0

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






def main():
    board = Board()

    # horizontal win
    board.place(15, 1, 1)

    board.place(14, 1, 2)

    board.place(13, 1, 3)

    board.place(12, 1, 0)
    #####################


if __name__ == '__main__':
    main()
