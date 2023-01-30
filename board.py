from sudoku_reader import SudokuReader
import numpy as np

class Board:
    def __init__(self, nums):
        # nums parameter is a 2D list
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.squares = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]
        print("Initialized board")

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        board_str = f"Board with {self.n_rows} rows and {self.n_cols} columns:\n"
        board_str += "[["
        for row in self.squares:
            for square in row:
                board_str += square.__str__() + ", "
            board_str = board_str[:-2] + "]\n ["
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
        self._set_up_squares(nums)
        self._set_up_elems()

    def _set_up_squares(self, nums):
        self.squares = [
            [
                Square(num, False if num == 0 else True)
                for num in row
            ]
            for row in nums
        ]

    def _set_up_elems(self):
        row_elems = [Element(row) for row in self.squares]
        col_elems = [Element([row[j] for row in self.squares]) for j in range(self.n_cols)]
        box_elems = [
            [
                Element([
                    self.squares[i][j]
                    for i in range(n, n+3)
                    for j in range(m, m+3)
                ])
                for m in range(0, 9, 3)
            ]
            for n in range(0, 9, 3)
        ] # Boxes are ordered in a 3x3 list as they appear on the board

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                assoc_elems = [row_elems[i], col_elems[j], box_elems[int(i/3)][int(j/3)]]
                self.squares[i][j].elems = assoc_elems

    def solve(self):
        # Your solving algorithm goes here!
        pass

class Element:
    def __init__(self, squares):
        self.squares = squares

    def contents(self):
        elem_contents = set([[square.value for square in row] for row in self.squares])
        return elem_contents

    def __str__(self):
        elem_str = f"Element with {len(self.squares)} squares:\n"
        elem_str += "["
        for square in self.squares:
            elem_str += square.__str__() + ", "
        elem_str = elem_str[:-2] + "]"
        return elem_str

if __name__ == "__main__":
    # Test code
    reader = SudokuReader("sudoku_10.csv")
    board = SudokuBoard(reader.next_board())
    print(board)