from tictactoe import check_win, is_full

def test_check_win():
    # Test winning horizontally
    board = [["X", "X", "X"],
             [" ", "O", " "],
             ["O", " ", " "]]
    assert check_win(board, "X") is True

    # Test winning vertically
    board = [["X", "O", "O"],
             ["X", "O", " "],
             ["X", " ", "X"]]
    assert check_win(board, "X") is True

    # Test winning diagonally
    board = [["X", "O", "O"],
             [" ", "X", " "],
             ["O", " ", "X"]]
    assert check_win(board, "X") is True

    # Test no win
    board = [["X", "O", "X"],
             ["X", "O", "O"],
             ["O", "X", "X"]]
    assert check_win(board, "X") is False

def test_is_full():
    # Test when the board is full
    board = [["X", "O", "X"],
             ["X", "O", "O"],
             ["O", "X", "X"]]
    assert is_full(board) is True

    # Test when the board is not full
    board = [["X", "O", "X"],
             ["X", " ", "O"],
             ["O", "X", "X"]]
    assert is_full(board) is False