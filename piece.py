#!/usr/bin/env python
# encoding: utf-8
"""
********************************************
* File Name : piece.py

* Created By : Darren Tan

* Creation Date : 04-21-2019

* Last Modified : 04-21-2019::04:10:09 PDT

* Purpose : Define the attributes of a base piece
********************************************
"""

class Piece(object):

    """This will hold all the properties for a single piece."""

    def __init__(self, id):
        """initialize properties for a piece



        :properties: Dictionary set of bools for each property

            Default values:
                shape == Circle == True
                indent == Yes == True
                color == White == True
                hatch === Yes == True

                _shape_ _color_ _indent_ _hatch_

        """

        self.id = id
        self.shape = is_shape(id)
        self.color = is_color(id)
        self.indent = is_indent(id)
        self.hatch = is_hatch(id)

def is_shape(id):
    return id & 0b1000 > 0

def is_color(id):
    return id & 0b0100 > 0

def is_indent(id):
    return id & 0b0010 > 0

def is_hatch(id):
    return id & 0b0001 > 0



def main():
    id = 15
    # create new instance of the Piece object
    my_piece = Piece(id)

    # testing output to see if it was assigned properly
    print("{0:b}".format(id))
    print(my_piece.shape)
    print(my_piece.color)
    print(my_piece.indent)
    print(my_piece.hatch)



if __name__ == '__main__':
    main()
