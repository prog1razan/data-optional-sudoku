# pylint: disable=missing-docstring

def sudoku_validator(grid):
    # The set of numbers that must appear in every row, column, and subgrid
    nums = set(range(1, 10))  # {1,2,3,4,5,6,7,8,9}

    # 1. Check rows

    for row in grid:
        # Convert the row to a set and compare with {1..9}
        if set(row) != nums:
            return False  # Invalid if a row doesn't contain all numbers 1–9


    # 2. Check columns

    for col in range(9):
        # Build a set of all elements in the current column
        column_values = {grid[row][col] for row in range(9)}
        if column_values != nums:
            return False  # Invalid if a column doesn't contain all numbers 1–9

    # The top-left corners of each 3x3 box are at (0,0), (0,3), (0,6), ..., (6,6)
    for box_row in range(0, 9, 3):      # step by 3 rows
        for box_col in range(0, 9, 3):  # step by 3 columns
            block = []
            # Collect all 9 numbers in this 3x3 block
            for i in range(3):
                for j in range(3):
                    block.append(grid[box_row + i][box_col + j])
            if set(block) != nums:
                return False  # Invalid if a 3x3 block doesn't contain all numbers 1–9

    # If all checks passed, the Sudoku is valid
    return True
