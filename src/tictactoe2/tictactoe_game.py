def print_board(board):
    """
    Print the Tic-Tac-Toe board with the current state.

    Parameters:
        board (list of lists): The 3x3 Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))  # Display each row with vertical bars to separate cells.
        print("-" * 9)  # Display horizontal lines to separate rows.

def check_win(board, player):
    # Check for horizontal and vertical wins.
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check for diagonal wins from top-left to bottom-right.
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check for diagonal wins from bottom-left to top-right.
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """
    Check if the Tic-Tac-Toe board is full (no empty spaces left).

    Parameters:
        board (list of lists): The 3x3 Tic-Tac-Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)

def main():
    """
    Main function to play a game of Tic-Tac-Toe.

    This function initializes the game board, handles player turns, checks for wins or ties,
    and prints the game state.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize the empty game board.
    current_player = "X"  # Start the game with 'X' as the current player.

    while True:
        print_board(board)  # Display the current state of the board.
        print(f"Player {current_player}'s turn.")  # Show the current player's turn.

        row = int(input("Enter the row (0, 1, 2): "))  # Get the player's chosen row.
        col = int(input("Enter the column (0, 1, 2): "))  # Get the player's chosen column.

        # Check if the player's move is valid (within the board and the cell is empty).
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")  # Display a message for an invalid move.
            continue

        board[row][col] = current_player  # Apply the player's move to the board.

        # Check if the current player has won the game.
        if check_win(board, current_player):
            print_board(board)  # Display the final board state.
            print(f"Player {current_player} wins!")  # Announce the winner.
            break

        # Check if the game has ended in a tie (board is full).
        if is_full(board):
            print_board(board)  # Display the final board state.
            print("It's a tie!")  # Announce a tie game.
            break

        current_player = "O" if current_player == "X" else "X"  # Switch to the other player for the next turn.

if __name__ == "__main__":
    main()
