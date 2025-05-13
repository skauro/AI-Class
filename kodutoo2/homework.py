import random


class NQPosition:
    def __init__(self, N):
        self.N = N
        self.board = [random.randint(0, N - 1) for _ in range(N)]  # Random initial state

    def value(self):
        """Calculate the number of conflicts (attacking queen pairs)."""
        conflicts = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.board[i] == self.board[j]:  # Same row
                    conflicts += 1
                if abs(self.board[i] - self.board[j]) == abs(i - j):  # Same diagonal
                    conflicts += 1
        return conflicts

    def make_move(self, move):
        """ move queen in column move[0] to row move[1]."""
        self.board[move[0]] = move[1]

    def best_move(self):
        """Find the best move that reduces conflicts the most."""
        current_conflicts = self.value()
        best_move = None
        best_value = current_conflicts

        for col in range(self.N): # try each row for that column
            original_row = self.board[col]
            for row in range(self.N):
                if row == original_row:
                    continue  # Skip the current position

                self.board[col] = row
                new_conflicts = self.value()

                if new_conflicts < best_value:
                    best_value = new_conflicts
                    best_move = (col, row)

                self.board[col] = original_row  # Restore original position

        return best_move, best_value


def hill_climbing(pos, max_steps=1000):
    """Hill climbing algorithm with a limit on steps."""
    for _ in range(max_steps):
        move, new_value = pos.best_move()
        if new_value >= pos.value():
            return pos, pos.value()  # No better move found
        pos.make_move(move)
    return pos, pos.value()


def solve_n_queens(N, max_restarts=50):
    """Solve N-Queens using hill climbing with random restarts."""

    best_pos = None
    best_value = float('inf')

    for _ in range(max_restarts):
        pos = NQPosition(N)
        final_pos, final_value = hill_climbing(pos)

        if final_value == 0:  # Found a solution
            print(f"Final value : {final_value}")
            return final_pos.board

        if final_value < best_value:
            best_value = final_value
            best_pos = final_pos

    # best attempt or none
    print(f"Final value : {best_value}")
    return best_pos.board if best_pos else None


def print_board(solution):
    """Prints the N-Queens board in a readable format."""
    N = len(solution)
    for row in range(N):
        line = ""
        for col in range(N):
            if solution[col] == row:
                line += " Q "  # Queen
            else:
                line += " . "  # Empty
        print(line)
    print("\n")  # Extra line for spacing


# Testing
N = 16
solution = solve_n_queens(N)
if solution:
    print(f"Solution for {N}-Queens:", solution)  # lugemine nullist

    print_board(solution)
else:
    print(f"No solution found for {N}-Queens after multiple restarts.")
