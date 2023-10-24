import pytest
from io import StringIO
import sys
from tictactoe2.tictactoe_game import print_board, check_win, is_full

def test_print_board(capsys):
    board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"]
    ]

    expected_output = "X | O | X\n---------\nO | X | O\n---------\nO | X | X\n---------\n"

    print_board(board)
    captured = capsys.readouterr()
    
    assert captured.out == expected_output

def test_check_win():
    board1 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"]
    ]

    board2 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]

    assert check_win(board1, "X") is True
    assert check_win(board1, "O") is True
    assert check_win(board2, "X") is True
    assert check_win(board2, "O") is True

def test_is_full():
    full_board = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"]
    ]

    not_full_board = [
        ["X", "O", "X"],
        ["O", "X", " "],
        ["O", "X", "X"]
    ]

    assert is_full(full_board) is True
    assert is_full(not_full_board) is False

def test_main(monkeypatch, capsys):
    from tictactoe2.tictactoe_game import main

    def simulate_game_input(inputs):
        input_iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda prompt: next(input_iterator))

    # Simulate a game where X wins
    simulate_game_input(["0", "0", "1", "1", "0", "1", "2", "2", "2"])
    main()

    captured = capsys.readouterr()
    assert "Player X wins!" in captured.out

    # Simulate a game that ends in a tie
    simulate_game_input(["0", "0", "0", "1", "1", "0", "1", "1", "2", "0", "2", "1", "2", "2"])
    main()

    captured = capsys.readouterr()
    assert "It's a tie!" in captured.out
