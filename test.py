#!/usr/bin/env python
# encoding: utf-8
# Author: Darren Tan


import unittest
import board as bd

props = [0b0001, 0b0010, 0b0100, 0b1000]


class TestGame(unittest.TestCase):

    def test_horiz_win(self):
        for prop in props:
            print("TESTING PROPERTY: 0b{0:04b}".format(prop))
            self.place_horiz_win(prop)

    def place_horiz_win(self, property):
        board_1 = bd.Board()
        board_2 = bd.Board()
        for i in range(4):
            # get the 8 pieces that match the property
            matching_pieces = board_1.get_matching_pieces(property)

            # split into two games with different pieces
            piece_1 = matching_pieces[:4]
            piece_2 = matching_pieces[4:]

            print("GAME 1 USING: {}".format(piece_1))
            print("GAME 2 USING: {}".format(piece_2))

            for j in range(4):
                board_1.place(piece_1[j], i, j)
                board_2.place(piece_2[j], i, j)

            self.assertTrue(board_1.win)
            self.assertTrue(board_2.win)

            if i < 3:
                board_1.new_game()
                board_2.new_game()


# def main():
#     place_horiz_win(0b0001)


if __name__ == '__main__':
    # main()
    unittest.main()
