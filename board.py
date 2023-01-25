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
        rows = [Element([self.game_board.squares[i][j] for j in range(9)]) for i in range(9)]
        cols = [Element([self.game_board.squares[i][j] for i in range(9)]) for j in range(9)]
        boxes = [Element([self.game_board.squares[i][j]
                 for i in range(n, n+3)
                 for j in range(m, m+3)])
                 for n in range(0, 9, 3)
                 for m in range(0, 9, 3)]

        self.elems = rows + cols + boxes

    def solve(self):
        pass

    def __str__(self):
        return self.game_board.__str__()

class Square:
    def __init__(self, val: int):
        self.value = val

    def __str__(self):
        return str(self.value)

    def __add__(self, o):
        return self.value + o.value

class Element:
    def __init__(self, squares: list[Square]):
        self.squares = squares

    def legality(self):
        used_nums = []
        for square in self.squares:
            if square.value in used_nums:
                return False
            used_nums.append(square.value)
        return True


if __name__ == "__main__":
    # Test code...
    reader = Sudoku_reader("sudoku_10.csv")
    board = SudokuBoard(reader.next_board())
    print(board)