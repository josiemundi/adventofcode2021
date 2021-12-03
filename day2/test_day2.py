import unittest

from .part1 import solve_puzzle

class TestPuzzle(unittest.TestCase):
    def test_example_input(self):
        test_input = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"
        self.assertEqual(solve_puzzle(test_input),150)
