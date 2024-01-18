import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, n, solutions):
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens_util(board, row + 1, n, solutions)


def solve_nqueens(n):
    board = [-1] * n
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Convert the argument to an integer
        N = int(sys.argv[1])

        # Check if N is greater than or equal to 4
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Solve N Queens problem
        solutions = solve_nqueens(N)

        # Print the solutions
        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
