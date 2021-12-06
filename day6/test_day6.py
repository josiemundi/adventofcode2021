import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = "3,4,3,1,2"
        self.assertEqual(solve_puzzle(test_input),5934)
