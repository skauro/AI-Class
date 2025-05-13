import random

ROWS = 6
COLS = 7
EMPTY = " "
PLAYER = "X"
AI = "O"
N_SIMULATIONS = 200  # Number of simulations per move


# Create an empty board
def create_board():
    return [[EMPTY] * COLS for _ in range(ROWS)]


# Print the board
def print_board(board):
    for row in board:
        print("|" + "".join(row) + "|")
    print(" " + "0123456")


# Get legal moves
def get_legal_moves(board):
    return [c for c in range(COLS) if board[0][c] == EMPTY]


# Make a move
def make_move(board, col, player):
    new_board = [row[:] for row in board]
    for row in reversed(new_board):
        if row[col] == EMPTY:
            row[col] = player
            return new_board
    return None  # Should never happen if called with a valid move


# Check for a win
def check_win(board, player):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True
    return False


# Simulate a random game
def simulate(board, move, player):
    temp_board = make_move(board, move, player)
    current_player = AI if player == PLAYER else PLAYER
    while True:
        legal_moves = get_legal_moves(temp_board)
        if not legal_moves:
            return "DRAW"
        move = random.choice(legal_moves)
        temp_board = make_move(temp_board, move, current_player)
        if check_win(temp_board, current_player):
            return "WIN" if current_player == AI else "LOSS"
        current_player = AI if current_player == PLAYER else PLAYER


# Monte Carlo AI move selection
def monte_carlo_move(board, simulations=N_SIMULATIONS):
    legal_moves = get_legal_moves(board)
    move_scores = {move: 0 for move in legal_moves}

    for move in legal_moves:
        for _ in range(simulations):
            result = simulate(board, move, AI)
            if result == "WIN":
                move_scores[move] += 1
            elif result == "DRAW":
                move_scores[move] += 0.5

    best_move = None


    best_score = -float("inf")

    for move in legal_moves:
        if move_scores[move] > best_score:
            best_score = move_scores[move]
            best_move = move

    return best_move


# Play the game
def play_game():
    board = create_board()
    print_board(board)
    while True:
        user_move = int(input("Your move? "))
        if user_move not in get_legal_moves(board):
            print("Invalid move. Try again.")
            continue
        board = make_move(board, user_move, PLAYER)
        print_board(board)
        if check_win(board, PLAYER):
            print("You win!")
            break
        if not get_legal_moves(board):
            print("It's a draw!")
            break
        ai_move = monte_carlo_move(board)
        print(f"AI plays: {ai_move}")
        board = make_move(board, ai_move, AI)
        print_board(board)
        if check_win(board, AI):
            print("AI wins!")
            break
        if not get_legal_moves(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()