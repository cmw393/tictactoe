from tictactoe2.tictactoe_game import print_board, check_win, is_full

def test_print_board(capsys):
    board = [["X", "O", "X"], [" ", "O", "X"], ["O", "X", " "]]
    print_board(board)
    captured = capsys.readouterr()
    expected_output = (
        "X | O | X\n"
        "---------\n"
        "  | O | X\n"
        "---------\n"
        "O | X |  \n"
    )
    # Remove leading/trailing white spaces and compare
    assert captured.out.strip() == expected_output.strip()


def test_check_win():
    board_x_wins = [["X", "O", "X"], [" ", "X", "O"], ["O", " ", "X"]]
    board_o_wins = [["X", "O", "X"], [" ", "O", "X"], ["O", "O", "X"]]
    board_no_win = [["X", "O", "X"], [" ", "O", "X"], ["O", "X", " "]]
    
    assert check_win(board_x_wins, "X") == True
    assert check_win(board_o_wins, "O") == True
    assert check_win(board_no_win, "X") == False
    assert check_win(board_no_win, "O") == False

def test_is_full():
    board_full = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    board_not_full = [["X", "O", "X"], ["O", " ", "O"], ["O", "X", "O"]]
    
    assert is_full(board_full) == True
    assert is_full(board_not_full) == False

def test_check_win_horizontal():
    # Test for a horizontal win by player 'X' in the first row.
    board_x_win = [["X", "X", "X"], [" ", "O", "O"], ["O", "X", "O"]]
    assert check_win(board_x_win, "X") == True

    # Test for a horizontal win by player 'O' in the second row.
    board_o_win = [["X", "X", "O"], ["O", "O", "O"], ["X", "X", "O"]]
    assert check_win(board_o_win, "O") == True

    # Test for no horizontal win.
    board_no_win = [["X", "O", "X"], [" ", "O", "X"], ["O", "X", "O"]]
    assert check_win(board_no_win, "X") == False
    assert check_win(board_no_win, "O") == False

def test_check_win_vertical():
    # Test for a vertical win by player 'X' in the first column.
    board_x_win = [["X", "O", "O"], ["X", "O", "O"], ["X", "X", "O"]]
    assert check_win(board_x_win, "X") == True

    # Test for a vertical win by player 'O' in the second column.
    board_o_win = [["X", "O", "O"], ["X", "O", "O"], ["X", "O", "X"]]
    assert check_win(board_o_win, "O") == True

    # Test for no vertical win.
    board_no_win = [["X", "O", "X"], ["O", "X", "X"], ["O", "X", "O"]]
    assert check_win(board_no_win, "X") == False
    assert check_win(board_no_win, "O") == False

def test_check_win_diagonal():
    # Test for a diagonal win by player 'X' from the top-left to bottom-right.
    board_x_win = [["X", "O", "O"], ["O", "X", "O"], ["O", "O", "X"]]
    assert check_win(board_x_win, "X") == True

    # Test for a diagonal win by player 'O' from the bottom-left to top-right.
    board_o_win = [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]]
    assert check_win(board_o_win, "O") == True

    # Test for no diagonal win.
    board_no_win = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
    assert check_win(board_no_win, "X") == False
    assert check_win(board_no_win, "O") == False
