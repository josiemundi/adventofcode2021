import unittest

from .part1 import bingo, solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
        self.assertEqual(solve_puzzle(test_input),4512)

class TestBingo(unittest.TestCase):
    def test_no_bingo(self):
        test_input = [[22, 13, 17, 11,  0],
[8,  2, 23,  4, 24],
[21,  9, 14, 16,  7],
 [6, 10,  3, 18,  5],
 [1, 12, 20, 15, 1]]
        self.assertFalse(bingo(test_input))


    def test_row_bingo(self):
        test_input = [[22, 13, 17, 11,  0],
[-1,-1,-1,-1,-1],
[21,  9, 14, 16,  7],
 [6, 10,  3, 18,  5],
 [1, 12, 20, 15, 1]]
        self.assertTrue(bingo(test_input))

    def test_column_bingo(self):
        test_input = [[-1, 13, 17, 11,  0],
[-1,5,-1,-1,-1],
[-1,  9, 14, 16,  7],
 [-1, 10,  3, 18,  5],
 [-1, 12, 20, 15, 1]]
        self.assertTrue(bingo(test_input))