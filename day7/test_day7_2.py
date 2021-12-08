import unittest

from .part2 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = "16,1,2,0,4,2,7,1,2,14"
        self.assertEqual(solve_puzzle(test_input),168)
