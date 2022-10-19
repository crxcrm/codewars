# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

def valid_solution(board):
    for i in range(len(board)):
        hoz = 0
        ver = 0
        for j in range(len(board)):
            ver += board[j][i]
            hoz += board[i][j]
            if board[i][j] < 1 or board[i][j] > 9:
                return False
        if ver != 45 or hoz != 45:
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i*3+k][j*3+l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        return False
            if gadd != 45:
                return False
    return True 
