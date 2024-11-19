import random
from enum import Enum, auto


class DotsItems(Enum):
    EMPTY = auto()
    PLAYER_ONE_ITEM = auto()
    PLAYER_TWO_ITEM = auto()
    LINE = auto()


class Board:
    def __init__(self, cell_rows, cell_cols, empty):
        self.num_cell_rows = cell_rows
        self.num_cell_cols = cell_cols

        self.cells = []
        self.edges = []

        for row in range(self.num_cell_rows):
            row = []
            for col in range(self.num_cell_cols):
                row.append(empty)
            self.cells.append(row)

        for line_row in range(2 * self.num_cell_rows + 1):
            row = []
            for line_col in range(2 * self.num_cell_cols + 1):
                row.append(empty)
            self.edges.append(row)

    def is_board_full(self) -> bool:
        for line_row in range(2 * self.num_cell_rows + 1):
            for line_col in range(2 * self.num_cell_cols + 1):
                if line_row % 2 != line_col % 2:
                    if self.edges[line_row][line_col] == DotsItems.EMPTY:
                        return False

        return True

    def place(self, row: int, col: int, item: DotsItems) -> None:
        if item == DotsItems.LINE:
            self.edges[row][col] = item
        if item == DotsItems.PLAYER_ONE_ITEM or item == DotsItems.PLAYER_TWO_ITEM:
            self.cells[row][col] = item


class DotsGame:
    def __init__(self):
        self.EMPTY = " "
        self.PLAYER_ONE_ITEM = "X"
        self.PLAYER_TWO_ITEM = "O"
        self.DOT = "+"
        self.HORIZONTAL_LINE = "-"
        self.VERTICAL_LINE = "|"

        self.num_cell_rows = 2
        self.num_cell_cols = 2
        self.board = Board(self.num_cell_rows, self.num_cell_cols, DotsItems.EMPTY)

        self.player_one = DotsPlayer("a", DotsItems.PLAYER_ONE_ITEM)
        self.player_two = DotsPlayer("b", DotsItems.PLAYER_TWO_ITEM)
        self.current_player = self.player_one

        self.take_another_turn = False

    def __str__(self) -> str:
        rep = ""

        rep += self.board_string()

        return rep

    def board_string(self) -> str:
        rep = "\n"

        tens_digit_line = "\n" + " " * 4
        for col in range((self.num_cell_cols * 2 + 1) // 10):
            tens_digit_line += " " * 9 + f"{col + 1}"
        rep += tens_digit_line

        ones_digit_line = "\n" + " " * 3
        for col in range(self.num_cell_cols * 2 + 1):
            ones_digit_line += f"{col % 10}"
        rep += ones_digit_line

        for line_row in range(self.num_cell_rows * 2 + 1):
            row = "\n"
            if line_row < 10:
                row += " "
            row += f"{line_row} "
            for line_col in range(self.num_cell_cols * 2 + 1):
                if line_row % 2 == line_col % 2 == 0:
                    row += self.DOT

                if line_row % 2 == line_col % 2 == 1:
                    cell_row = (line_row - 1) // 2
                    cell_col = (line_col - 1) // 2
                    cell_item = self.board.cells[cell_row][cell_col]

                    if cell_item == DotsItems.EMPTY:
                        row += self.EMPTY

                    if cell_item == DotsItems.PLAYER_ONE_ITEM:
                        row += self.PLAYER_ONE_ITEM

                    if cell_item == DotsItems.PLAYER_TWO_ITEM:
                        row += self.PLAYER_TWO_ITEM

                if line_row % 2 != line_col % 2:
                    if self.board.edges[line_row][line_col] == DotsItems.LINE:
                        if line_row % 2 == 0:
                            row += "-"
                        else:
                            row += "|"
                    else:
                        row += " "
            row += f" {line_row}"
            rep += row
        rep += ones_digit_line
        rep += tens_digit_line

        return rep

    def display_result(self) -> None:
        player_one_score = 0
        player_two_score = 0

        for row in self.board.cells:
            for cell in row:
                if cell == DotsItems.PLAYER_ONE_ITEM:
                    player_one_score += 1
                if cell == DotsItems.PLAYER_TWO_ITEM:
                    player_two_score += 1

        if player_one_score > player_two_score:
            print(f"{self.player_one.name} wins!")
        elif player_one_score < player_two_score:
            print(f"{self.player_two.name} wins!")
        else:
            print("It's a tie!")

    def find_boxes(self, row: int, col: int) -> list:
        boxes = []
        if row % 2 == 0:  # horizontal line, look up and down
            cell_row = row // 2 - 1
            cell_col = (col - 1) // 2
            if cell_row in range(self.board.num_cell_rows) and cell_col in range(
                self.board.num_cell_cols
            ):
                if self.board.cells[cell_row][cell_col] == DotsItems.EMPTY:
                    if (
                        self.board.edges[row - 1][col - 1]
                        == self.board.edges[row - 2][col]
                        == self.board.edges[row - 1][col + 1]
                        == DotsItems.LINE
                    ):
                        boxes.append((cell_row, cell_col))
            if cell_row + 1 in range(self.board.num_cell_rows) and cell_col in range(
                self.board.num_cell_cols
            ):
                if self.board.cells[cell_row + 1][cell_col] == DotsItems.EMPTY:
                    if (
                        self.board.edges[row + 1][col - 1]
                        == self.board.edges[row + 2][col]
                        == self.board.edges[row + 1][col + 1]
                        == DotsItems.LINE
                    ):
                        boxes.append((cell_row + 1, cell_col))
        else:  # vertical line, look left and right
            cell_row = (row - 1) // 2
            cell_col = col // 2 - 1
            if cell_row in range(self.board.num_cell_rows) and cell_col in range(
                self.board.num_cell_cols
            ):
                if self.board.cells[cell_row][cell_col] == DotsItems.EMPTY:
                    if (
                        self.board.edges[row + 1][col - 1]
                        == self.board.edges[row][col - 2]
                        == self.board.edges[row - 1][col - 1]
                        == DotsItems.LINE
                    ):
                        boxes.append((cell_row, cell_col))
            if cell_row in range(self.board.num_cell_rows) and cell_col + 1 in range(
                self.board.num_cell_cols
            ):
                if self.board.cells[cell_row][cell_col + 1] == DotsItems.EMPTY:
                    if (
                        self.board.edges[row + 1][col + 1]
                        == self.board.edges[row][col + 2]
                        == self.board.edges[row - 1][col + 1]
                        == DotsItems.LINE
                    ):
                        boxes.append((cell_row, cell_col + 1))
        return boxes

    def is_board_full(self) -> bool:
        return self.board.is_board_full()

    def is_valid_move(self, move: str) -> bool:
        if move.count(" ") != 1:
            print("Improperly formatted input.")
            return False

        left_side, right_side = move.split(" ")
        if not left_side.isdigit():
            print("Row is not numeric.")
            return False

        if not right_side.isdigit():
            print("Column is not numeric.")
            return False

        row_num = int(left_side)
        col_num = int(right_side)

        if row_num not in range(self.board.num_cell_rows * 2 + 1):
            print("Row value out of range.")
            return False

        if col_num not in range(self.board.num_cell_cols * 2 + 1):
            print("Column value out of range.")
            return False

        if row_num % 2 == col_num % 2 == 0:
            print("That is a dot, not an edge.")
            return False

        if row_num % 2 == col_num % 2 == 1:
            print("That is a space, not an edge.")
            return False

        return True

    def make_move(self, row: int, col: int) -> None:
        # place edge
        self.board.place(row, col, DotsItems.LINE)
        # look for boxes
        boxes = self.find_boxes(row, col)
        # if found, enter current player piece in box
        if boxes:
            self.take_another_turn = True
            for box in boxes:
                row, col = box
                self.board.place(row, col, self.current_player.piece)
        #   current player gets to play again

    def next_turn(self) -> None:
        if self.take_another_turn:
            self.take_another_turn = False
            print(f"{self.current_player.name}, take another turn")
            return

        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one
        print(f"{self.current_player.name}, it's your turn!")

    def play(self) -> None:
        while not self.is_board_full():
            self.next_turn()
            print(self)
            move = self.current_player.get_move(self.board)
            while not self.is_valid_move(move):
                move = self.current_player.get_move(self.board)

            left_side, right_side = move.split(" ")
            row_num = int(left_side)
            col_num = int(right_side)

            self.make_move(row_num, col_num)

        print(self)
        self.display_result()
        # end game stuff


class DotsPlayer:
    def __init__(self, name: str, piece: DotsItems):
        self.name = name
        self.piece = piece

    def get_move(self, board: Board) -> str:
        print(
            f"Enter an edge: (0-{board.num_cell_rows * 2}) (0-{board.num_cell_cols * 2})"
        )
        move_str = input()

        return move_str


game = DotsGame()
game.play()
