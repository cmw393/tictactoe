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
    assert captured.out == expected_output

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
