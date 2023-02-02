from sudoku_reader import SudokuReader
import numpy as np

class Board:
    def __init__(self, nums: list[list]):
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self._set_up_squares(nums)

    def _set_up_squares(self, nums):
        # Creates an empty board with the dimensions of `nums`
        self.squares = np.array([
            [None for _ in range(self.n_rows)]
            for _ in range(self.n_cols)
        ])

    def __str__(self):
        board_str = f"Board with {self.n_rows} rows and {self.n_cols} columns:\n"
        board_str += "[["
        for row in self.squares:
            for square in row:
                board_str += square.__str__() + ", "
            board_str = board_str[:-2] + "]\n ["
        board_str = board_str[:-3] + "]"
        return board_str

class SudokuBoard(Board):
    def _set_up_squares(self, nums):
        self.squares = np.array([
            [
                Square(num, False if num == 0 else True)
                for num in row
            ]
            for row in nums
        ])

        self._set_up_elems()

    def _set_up_elems(self):
        row_elems = np.array([Element(row) for row in self.squares])
        col_elems = np.array([
            Element([row[j] for row in self.squares])
            for j in range(self.n_cols)
        ])
        box_elems = np.array([
            [
                Element([
                    self.squares[i][j]
                    for i in range(n, n+3)
                    for j in range(m, m+3)
                ])
                for m in range(0, 9, 3)
            ]
            for n in range(0, 9, 3)
        ]) # Boxes are ordered in a 3x3 list as they appear on the board

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                assoc_elems = np.array([
                    row_elems[i],
                    col_elems[j],
                    box_elems[int(i/3)][int(j/3)]
                ])
                self.squares[i][j].elems = assoc_elems

    def print_elems(self, i, j):
        for elem in self.squares[i][j].elems:
            print(elem)

    def solve(self):
        # Brute force algorithm
        mutable_squares = np.array([
            square
            for square in self.squares.flatten()
            if not square.fixed
        ])

        i = 0
        while i < len(mutable_squares):
            #print(f"Index {i}")

            square = mutable_squares[i]
            #print(f"Seen {square.value}")

            trial_val = square.min_legal_val(square.value + 1)
            #print(f"Trying {trial_val}")

            if trial_val > 0:
                #print("Setting")
                square.set_val(trial_val)
                i += 1
            else:
                #print("Stepping back")
                square.set_val(0)
                i -= 1

class Square:
    def __init__(self, value: int, fixed: bool):
        self.value = value
        self.fixed = fixed
        self.elems = []

    def _consider(self, pot_val):
        for elem in self.elems:
            if pot_val in elem.contents():
                return False
        return True

    def min_legal_val(self, min=1):
        for k in range(min, 10):
            if self._consider(k):
                return k
        return 0

    def set_val(self, new_val):
        if self.fixed:
            raise AttributeError("Square is fixed; value cannot be reassigned")
        else:
            self.value = new_val

    def __str__(self):
        if self.fixed:
            return "(" + str(self.value) + ")"
        else:
            return " " + str(self.value) + " "

class Element:
    def __init__(self, squares: list[Square]):
        self.elem_squares = np.array(squares)

    def contents(self):
        elem_contents = set([square.value for square in self.elem_squares])
        return elem_contents

    def __str__(self):
        elem_str = f"Element with {len(self.elem_squares)} squares:\n"
        elem_str += "["
        for square in self.elem_squares:
            elem_str += square.__str__() + ", "
        elem_str = elem_str[:-2] + "]"
        return elem_str

if __name__ == "__main__":
    # Test code
    reader = SudokuReader("sudoku_10.csv")
    board = SudokuBoard(reader.next_board())
    board.print_elems(4, 6)
    print(board)

    board.solve()
    print(board)