import pandas as pd

# Initialize the game board
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
players = ['X', 'O']
current_player = 0

def gameBoard():
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def checkWinner():
    winning_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in winning_conditions:
        if all(board[row][col] == players[current_player] for row, col in condition):
            return True
    return False

def playGame():
    global current_player
    for turn in range(9):
        gameBoard()
        move = int(input(f'Player {players[current_player]}, enter your move (1-9): ')) - 1
        row, col = divmod(move, 3)

        if board[row][col] == '_':
            board[row][col] = players[current_player]
            if checkWinner():
                gameBoard()
                print(f'Player {players[current_player]} wins!')
                return
            current_player = 1 - current_player  # Switch player
        else:
            print("The box has already been taken! Try again.")

    gameBoard()
    print("The game is a draw!")

playGame()
