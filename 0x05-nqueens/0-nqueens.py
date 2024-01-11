#!/usr/bin/python3
import sys


def is_safe(placed_queens, row, col):
    """Checks if placing a queen at (row, col) is safe,
    given previously placed queens."""
    n = len(placed_queens)  # Board size
    for i in range(n):
        # Check for conflicts in row, column, and diagonals
        if placed_queens[i][1] == col or abs(row - i) == abs(col - placed_queens[i][1]):
            return False
    return True


def solve_n_queens(n):
    """Solves the N-Queens problem and returns all valid solutions."""
    solutions = []
    placed_queens = []  # List of (row, col) pairs for placed queens

    def place_queens(row):
        if row == n:  # All queens placed successfully
            solutions.append(placed_queens[:])  # Add a copy of the solution
            return

        for col in range(n):
            if is_safe(placed_queens, row, col):
                placed_queens.append((row, col))
                place_queens(row + 1)  # Recurse to place the next queen
                placed_queens.pop()  # Backtrack if placement leads to conflict

    place_queens(0)  # Start placing queens from row 0
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        exit(1)

    if n < 4:
        exit(1)
    solutions = solve_n_queens(n)
    for solution in solutions:
        print([list(coord) for coord in solution])
