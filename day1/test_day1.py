import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263"
        self.assertEqual(solve_puzzle(test_input),7)
