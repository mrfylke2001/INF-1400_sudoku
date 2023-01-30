from sudoku_reader import SudokuReader
import numpy as np

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self._set_up_squares(nums)
        print("Initialized board")

    def _set_up_squares(self, nums):
        self.squares = [[Square(num, False if num == 0 else True)
                        for num in row]
                        for row in nums]

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        board_str = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        board_str += "[["
        for row in self.squares:
            for square in row:
                board_str += square.__str__() + ", "
            board_str = board_str[:-2] + "]" + "\n ["
        board_str = board_str[:-3] + "]"
        return board_str

class Square:
    def __init__(self, value, fixed: bool):
        self.value = value
        self.fixed = fixed

    def __str__(self):
        if self.fixed:
            return "(" + str(self.value) + ")"
        else:
            return " " + str(self.value) + " "

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

class Element:
    def __init__(self, squares):
        self.squares = squares

    def contents(self):
        elem_contents = set([[square.value for square in row] for row in self.squares])
        return elem_contents

if __name__ == "__main__":
    # Test code...
    reader = SudokuReader("sudoku_10.csv")
    board = SudokuBoard(reader.next_board())
    print(board)