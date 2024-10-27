# Initialize a 3x3 board filled with empty spaces
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def display_board():
    """Display the current state of the game board."""
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))  # Join cells with '|' for separation
        if row < 2:
            print("--+---+--")  # Add a horizontal divider between rows
    print("\n")

def check_winner(player):
    """Check if the given player has won."""
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):  # Top-left to bottom-right
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Top-right to bottom-left
        return True
    return False

def is_board_full():
    """Check if the board is full (i.e., a draw)."""
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

def play_game():
    """Main function to control the game flow."""
    global current_player

    # Loop until the game is won or the board is full
    while True:
        display_board()

        # Get player's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue

            # Convert the move to row and column indices
            row, col = divmod(move - 1, 3)

            # Check if the cell is already occupied
            if board[row][col] != ' ':
                print("This spot is already taken! Choose another one.")
                continue

            # Place the player's symbol on the board
            board[row][col] = current_player

            # Check for a win
            if check_winner(current_player):
                display_board()
                print(f"Congratulations! Player {current_player} wins!")
                break

            # Check for a draw
            if is_board_full():
                display_board()
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Start the game
play_game()
