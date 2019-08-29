#!/usr/bin/env python
# encoding: utf-8
"""
********************************************
* File Name : game.py

* Created By : Darren Tan

* Creation Date : 08-26-2019

* Last Modified : 08-29-2019::10:30:22 

* Purpose : Quarto game orchestrator
********************************************
"""

# built-in modules


# downloaded modules


# custom modules
import board as bd


class Game(object):

    def __init__(self):

        self.board = bd.Board()
        self.new_game()

    def new_game(self):
        """ re-initialize to default null values """
        self.active_player = 0
        self.next_player = 1
        self.next_piece = [-1, -1]
        self.p_names = ['Player 1', 'Player 2']
        self.first_turn()

    def first_turn(self):
        print('Player 1, please select a piece for Player 2 to place')
        self.select_next_piece()

    def next_turn(self):
        self.swap_active_player()

        if self.active_player == 0:
            print('Player 1:\n')
        else:
            self.active_player == 1
            print('Player 2:\n')

        self.place_next_piece()

    def swap_active_player(self):
        if self.active_player == 0:
            self.active_player = 1
            self.next_player = 0
        else:
            self.active_player = 0
            self.next_player = 1

    def select_next_piece(self):
        print('Available pieces: {}'.format(self.board.library))
        piece = input(self.p_names[self.active_player] +
                      ': Which piece would you like your opponent to play? Type "-1" to quit! >>> ')
        assert self.board.is_available(
            piece), "The piece you wanted to play is not available"
        self.next_piece[self.next_player] = piece
        self.next_turn()

    def place_next_piece(self):
        row = ''
        col = ''
        piece = self.next_piece[self.active_player]

        row = input(
            self.p_names[self.active_player] + ': Which row would you like the piece to be played? Type "-1" to quit! >>> ')
        if row != -1:
            col = input(
                self.p_names[self.active_player] + ': Which column would you like the piece to be played? Type "-1" to quit! >>> ')

        self.board.place(piece, row, col)
        if self.board.win:
            self.board.new_game()
            self.new_game()

        else:
            self.select_next_piece()
            self.swap_active_player()


def main():
    game = Game()


if __name__ == '__main__':
    main()
