# classes and objects
# class is like a function definition, except
# a class has data and behavior.
# object -> an instance of a class.
import random
import math


class Ocean:  # class definition (doesn't do anything by itself)
    def __init__(self, num_rows: int, num_cols: int, empty: int) -> None:
        self.cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols

        for row_num in range(self.num_rows):
            row = []
            for col in range(self.num_cols):
                row.append(empty)
            self.cells.append(row)

    def add(self, pos: tuple[int, int], item: int) -> None:
        row_num, col_num = pos
        self.cells[row_num][col_num] = item

    def get(self, pos: tuple[int, int]) -> int:
        row_num, col_num = pos
        return self.cells[row_num][col_num]

    def get_distance(self, start_pos: tuple[int, int], end_pos: tuple[int, int]) -> int:
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        dist = math.sqrt((start_row - end_row) ** 2 + (start_col - end_col) ** 2)
        dist = math.floor(dist)
        return dist


class SonarGame:
    EMPTY = 0
    TREASURE = 1
    BEACON = 2

    def __init__(self) -> None:
        self.num_rows = 15
        self.num_cols = 60
        self.ocean = Ocean(self.num_rows, self.num_cols, SonarGame.EMPTY)

        self.num_treasures = 3
        self.treasures = []
        self.found_treasures = []
        self.hide_treasures()

        self.previous_moves = []

        self.max_beacons = 20
        self.beacons_placed = 0

    def __str__(self) -> str:
        rep = ""

        rep += f"Beacons remaining: {self.max_beacons - self.beacons_placed}\n"
        rep += f"Treasures found: {len(self.found_treasures)}\n\n"
        rep += self.make_ocean_visual()

        return rep

    def get_distance_to_treasure(self, pos: tuple[int, int]) -> int:
        min_distance = 100
        for treasure in self.treasures:
            if treasure not in self.found_treasures:
                dist = self.ocean.get_distance(pos, treasure)
                min_distance = min(min_distance, dist)

        return min_distance

    def get_move(self) -> tuple[int, int]:
        print("Where would you like to place a beacon? (0-14 0-59)")
        input_text = input()

        while not self.is_valid_move(input_text):
            print("Where would you like to place a beacon? (0-14 0-59)")
            input_text = input()

        row_str, col_str = input_text.split(" ")
        row_num = int(row_str)
        col_num = int(col_str)

        return (row_num, col_num)

    def hide_treasures(self) -> None:
        for _ in range(self.num_treasures):
            row_pos = random.randrange(self.num_rows)
            col_pos = random.randrange(self.num_cols)

            while (row_pos, col_pos) in self.treasures:
                row_pos = random.randrange(self.num_rows)
                col_pos = random.randrange(self.num_cols)

            treasure_pos = (row_pos, col_pos)
            self.treasures.append(treasure_pos)
            self.ocean.add(treasure_pos, SonarGame.TREASURE)
            print("treasure added to ocean")
            print(f"{self.ocean.get(treasure_pos)}")

    def is_valid_move(self, move_str: str) -> bool:
        if move_str.count(" ") != 1:
            print("Improperly formatted input")
            return False

        row_str, col_str = move_str.split(" ")

        if not row_str.isdigit():
            print("Input is not numerical")
            return False

        if not col_str.isdigit():
            print("Input is not numerical")
            return False

        row_num = int(row_str)
        col_num = int(col_str)

        if not row_num in range(self.num_rows):
            print("Row value out of bounds")
            return False

        if not col_num in range(self.num_cols):
            print("Column value out of bounds")
            return False

        if (row_num, col_num) in self.previous_moves:
            print("Already used")
            return False

        return True

    def make_move(self, move: tuple[int, int]) -> None:
        self.previous_moves.append(move)

        if self.ocean.get(move) == SonarGame.TREASURE:
            print(f"You found a treasure at {move}!")
            self.found_treasures.append(move)
            return

        self.ocean.add(move, SonarGame.BEACON)
        self.beacons_placed += 1

    def make_ocean_visual(self) -> str:
        rep = ""

        tens_digits_line = "    "  # four spaces
        for tens_digit in range(1, 6):
            tens_digits_line += " " * 9 + str(tens_digit)

        rep += tens_digits_line + "\n"

        ones_digits_line = "   " + "0123456789" * 6
        rep += ones_digits_line + "\n"

        for row_num in range(self.num_rows):
            row_text = ""
            if row_num < 10:
                row_text += " "
            row_text += str(row_num) + " "
            for col_num in range(self.num_cols):
                pos = (row_num, col_num)
                item = self.ocean.get(pos)
                if item == SonarGame.EMPTY:
                    row_text += random.choice(("`", "~"))
                if item == SonarGame.TREASURE:
                    if pos in self.found_treasures:
                        row_text += "T"
                    else:
                        row_text += random.choice(("`", "~"))
                if item == SonarGame.BEACON:
                    dist = self.get_distance_to_treasure(pos)
                    if dist < 10:
                        row_text += str(dist)
                    else:
                        row_text += "X"

            row_text += " " + str(row_num)
            rep += row_text + "\n"

        rep += ones_digits_line + "\n"
        rep += tens_digits_line + "\n"

        return rep

    def play(self) -> None:
        while (
            len(self.found_treasures) < self.num_treasures
            and self.beacons_placed < self.max_beacons
        ):
            print(self)
            move = self.get_move()
            self.make_move(move)

        print(self)
        if len(self.found_treasures) == self.num_treasures:
            print("Congratulations! You found all the treasure!")
        else:
            print("Too bad. Better luck next time.")


game = SonarGame()
game.play()
