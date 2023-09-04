1
11

# Tic Tac Toe Game

# Initialize the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

# Function to handle a player's turn
def player_turn(player):
    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")
    while not position.isdigit() or int(position) < 1 or int(position) > 9 or board[int(position)-1] != ' ':
        position = input("Invalid input. Choose a position from 1-9: ")
    board[int(position)-1] = player
    display_board()

# Function to check if the game is over
def game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    # Check if board is full
    if ' ' not in board:
        return True
    return False

# Function to check who won
def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X, and Player 2 will be O.")
    display_board()
    player = 'X'
    while not game_over():
        player_turn(player)
        player = 'O' if player == 'X' else 'X'
    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie.")

# Play the game
play_game()
