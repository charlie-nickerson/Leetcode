# Valid Sudoku

# Description: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#    Only the filled cells need to be validated according to the mentioned rules.

from collections import Counter

def isValidSudoku(board: list[list[str]]) -> bool:
        
        # Get the count of each value in the rows
        row_counter = []
        for row in board:
            row_count = Counter(row)
            row_count.pop(".")
            row_counter.append(row_count)
        

        # Convert columns into arrays
        columns = [[] for i in range(9)]
        for row in board:
            for c in range(len(columns)):
                columns[c].append(row[c])

        # Get the count of each element in the columns
        column_counter = []        
        for c in columns:
            col_count = Counter(c)
            col_count.pop(".")
            column_counter.append(col_count)
        
        # Convert sqaures into arrays
        squares = [[] for i in range(9)]
        for i, row in enumerate(board):
                if i % 3 == 0:
                    squares[i].extend(row[0:3])
                    squares[i+1].extend(row[3:6])
                    squares[i+2].extend(row[6:9])
                if i % 3 == 1:
                    squares[i-1].extend(row[0:3])
                    squares[i].extend(row[3:6])
                    squares[i+1].extend(row[6:9])
                if i % 3 == 2:
                    squares[i].extend(row[6:9])
                    squares[i-1].extend(row[3:6])
                    squares[i-2].extend(row[0:3])
        
        # Get the count of each element in the squares
        square_counter = []
        for s in squares:
            square_count = Counter(s)
            square_count.pop(".")
            square_counter.append(square_count)
        
        # Check if each row, column and square contain any duplicates excluding "."
        for r in row_counter:
            if max(r.values(), default=0) > 1: 
                return False
        for c in column_counter:
            if max(c.values(), default=0) > 1: 
                return False
        for s in square_counter:
            if max(s.values(), default=0) > 1:
                return False
        return True

def main():
    sudoku = [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]
    
    isValid = isValidSudoku(sudoku)
    print(isValid)

if __name__ == "__main__":
    main()
