#!/usr/bin/env python
# encoding: utf-8
# Author: Darren Tan


def xor(*args):
    val = args[0]
    for i in range(1, len(args)):
        val = (val ^ args[i])
        # print(bin(val))
    return val

def xnor(*args):
    val = args[0]
    for i in range(1, len(args)):
        # val = ~(val ^ args[i])
        val = 0b1111 - (val ^ args[i])
        # print(bin(val))
    return val

def wrong_xnor(*args):
    val = args[0]
    for i in range(1, len(args)):
        val = ~(val ^ args[i])
        # print(bin(val))
    return val

def bit_and(*args):
    val = args[0]
    for i in range(1, len(args)):
        val = val & args[i]
    # print(bin(val))
    return val

def main():
    # test = [8, 9, 10, 11]
    # test = [1, 2]
    test = [-1, 0]
    # test = [0b0001, 0b0011]
    # print("BITWISE XOR: {0:04b}".format(xor(*test)))
    print("BITWISE XNOR: {0:04b}".format(xnor(*test)))
    print("BITWISE WRONG_XNOR: {0:04b}".format(wrong_xnor(*test)))

    # print("BITWISE AND: {0:04b}".format(bit_and(*test)))



if __name__ == '__main__':
    main()
