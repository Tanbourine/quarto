#!/usr/bin/env python
# encoding: utf-8
"""
********************************************
* File Name : game.py

* Created By : Darren Tan

* Creation Date : 08-26-2019

* Last Modified : 09-10-2019::14:28:04 

* Purpose : Quarto game orchestrator
********************************************
"""

# built-in modules


# downloaded modules


# custom modules
import board as bd


class Game(object):
    """ Orchestrates the game and allows for user interaction """
    # pylint: disable=superfluous-parens, missing-docstring

    def __init__(self):

        self.active_player = 0
        self.next_player = 1
        self.next_piece = -1
        self.p_names = ['Player 1', 'Player 2']

        self.board = bd.Board()
        self.first_turn()

    def new_game(self):
        """ re-initialize to default null values """
        self.active_player = 0
        self.next_player = 1
        self.next_piece = -1
        self.p_names = ['Player 1', 'Player 2']
        self.first_turn()

    def first_turn(self):
        print('Player 1, please select a piece for Player 2 to place')
        self.select_next_piece()

    def next_turn(self):
        self.swap_active_player()
        self.place_next_piece()

    def swap_active_player(self):
        if self.active_player == 0:
            self.active_player = 1
            self.next_player = 0
        else:
            self.active_player = 0
            self.next_player = 1

    def place_next_piece(self):
        row = ''
        col = ''

        row = input(
            self.p_names[self.active_player] + ': Which row would you like the piece to be played? Type "-1" to quit! >>> ')
        if row != -1:
            col = input(
                self.p_names[self.active_player] + ': Which column would you like the piece to be played? Type "-1" to quit! >>> ')

        self.board.place(self.next_piece, row, col)
        if self.board.win:
            self.board.new_game()
            self.new_game()

        else:
            self.select_next_piece()
            self.swap_active_player()

    def select_next_piece(self):
        print('Available pieces: {}'.format(self.board.library))
        piece = input(self.p_names[self.active_player] +
                      ': Which piece would you like your opponent to play? Type "-1" to quit! >>> ')
        assert self.board.is_available(
            piece), "The piece you wanted to play is not available"
        self.next_piece = piece
        self.next_turn()


def main():
    game = Game()


if __name__ == '__main__':
    main()
