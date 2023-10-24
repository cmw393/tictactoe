import unittest
from unittest.mock import patch
import io
import sys

def simulate_game(inputs):
    with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
        with patch('builtins.input', side_effect=inputs):
            exec(open('tic_tac_toe.py').read())
        output = mock_stdout.getvalue()
    return output

class TestTicTacToe(unittest.TestCase):

    def test_valid_gameplay(self):
        # Simulate a valid game where 'X' wins.
        inputs = ['0', '0', '0', '1', '1', '1', '2', '2', '2']
        output = simulate_game(inputs)
        self.assertIn("Player X wins!", output)

    def test_invalid_move_then_valid_gameplay(self):
        # Simulate an invalid move followed by valid gameplay where 'O' wins.
        inputs = ['0', '0', '0', '1', '1', '1', '2', '2', '2', '2', '1', '2']
        output = simulate_game(inputs)
        self.assertIn("Player O wins!", output)

    def test_tie_game(self):
        # Simulate a tie game where the board is full.
        inputs = ['0', '0', '0', '0', '2', '2', '2', '1', '1', '1', '1']
        output = simulate_game(inputs)
        self.assertIn("It's a tie!", output)

if __name__ == '__main__':
    unittest.main()
