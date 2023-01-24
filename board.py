from sudoku_reader import Sudoku_reader
import numpy as np

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.squares = [[Square(x) for x in row] for row in nums]

    def _set_up_nums(self):
        # Set up the squares on the board (ints into Square objects)
        pass

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for row in self.squares:
            for square in row:
                r += square.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

class SudokuBoard:
    def __init__(self, nums):
        self.game_board = Board(nums)

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)
        pass

    def solve(self):
        pass

class Square:
    def __init__(self, val: int):
        self.value = val

    def __str__(self):
        return str(self.value)

class Element:
    def __init__(self, squares: Square):
        self.squares = squares

if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv")
    board = Board(reader.next_board())
    print(board)