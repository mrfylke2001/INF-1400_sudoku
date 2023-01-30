from sudoku_reader import SudokuReader
import numpy as np

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self._set_up_nums(nums)
        print("Initialized board")

    def _set_up_nums(self, nums):
        self.nums = [[Square(nums[i][j], i, j) for j in range(self.n_cols)] for i in range(self.n_rows)]

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

class Square:
    def __init__(self, value, row: int, col: int):
        self.value = value
        self.position = (row, col)

    def __str__(self):
        return str(self.value)

class SudokuBoard(Board):
    def __init__(self, nums):
        Board.__init__(self, nums)
        self._set_up_elems()

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)
        print("Setting up elems")

    def solve(self):
        # Your solving algorithm goes here!
        pass

if __name__ == "__main__":
    # Test code...
    reader = SudokuReader("sudoku_10.csv")
    board = SudokuBoard(reader.next_board())
    print(board)