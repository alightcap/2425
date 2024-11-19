import random
import math


class Ocean:
    # constructor gets called automatically when object is created
    def __init__(self, num_rows: int, num_cols: int, empty: int) -> None:
        self.cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols

        # setup the cells
        for row_num in range(self.num_rows):
            row = []
            for col_num in range(self.num_cols):
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

        distance = math.sqrt((start_row - end_row) ** 2 + (start_col - end_col) ** 2)
        distance = math.floor(distance)
        return distance


class SonarGame:
    def __init__(self) -> None:
        self.empty_code = 0
        self.treasure_code = 1
        self.beacon_code = 2

        self.num_rows = 15
        self.num_cols = 60

        self.ocean = Ocean(self.num_rows, self.num_cols, self.empty_code)

        self.num_treasures = 3
        self.treasures = []
        self.hide_treasures()
        self.found_treasures = []

        self.previous_moves = []

        self.max_beacons = 20
        self.num_beacons = 0

    def __str__(self) -> str:
        rep = ""

        # number of beacons remaining
        rep += f"Beacons remaining: {self.max_beacons - self.num_beacons}\n"
        # number of treasures found
        rep += f"Treasures found: {len(self.found_treasures)}\n\n"
        rep += self.make_ocean_visual()

        return rep

    def get_distance_to_treasure(self, pos: tuple[int, int]) -> int:
        min_distance = 100
        for treasure in self.treasures:
            if not treasure in self.found_treasures:
                distance = self.ocean.get_distance(pos, treasure)
                min_distance = min(min_distance, distance)

        return min_distance

    def get_move(self) -> tuple[int, int]:
        print("Where would you like to place a beacon? (0-14 0-59)")
        move = input()

        while not self.is_valid_input(move):
            print("Where would you like to place a beacon? (0-14 0-59)")
            move = input()

        row_text, col_text = move.split(" ")
        row_num = int(row_text)
        col_num = int(col_text)
        # example: move = "ab cd e f" -> move.split(" ") -> ["ab", "cd", "e", "f"]
        return row_num, col_num

    def hide_treasures(self) -> None:
        for _ in range(self.num_treasures):
            row_pos = random.randrange(self.num_rows)
            col_pos = random.randrange(self.num_cols)
            pos = (row_pos, col_pos)

            while pos in self.treasures:
                row_pos = random.randrange(self.num_rows)
                col_pos = random.randrange(self.num_cols)
                pos = (row_pos, col_pos)

            self.treasures.append(pos)
            self.ocean.add(pos, self.treasure_code)

    def is_valid_input(self, input_text: str) -> bool:
        if input_text.count(" ") != 1:
            print("Improperly formatted input.")
            return False

        row_text, col_text = input_text.split(" ")
        if not row_text.isdigit():
            print("Input is not numerical.")
            return False

        if not col_text.isdigit():
            print("Input is not numerical.")
            return False

        row_num = int(row_text)
        col_num = int(col_text)
        if not row_num in range(self.num_rows):
            print("Row value out of bounds.")
            return False

        if not col_num in range(self.num_cols):
            print("Column value out of bounds.")
            return False

        if (row_num, col_num) in self.previous_moves:
            print("Already used.")
            return False

        return True

    def make_move(self, move: tuple[int, int]) -> None:
        self.previous_moves.append(move)

        if move in self.treasures:
            print(f"You found a treasure at {move}!")
            self.found_treasures.append(move)
            return

        self.ocean.add(move, self.beacon_code)
        self.num_beacons += 1

    def make_ocean_visual(self) -> str:
        rep = ""

        tens_digit_line = "    "
        for tens_digit in range(1, 6):
            tens_digit_line += " " * 9 + str(tens_digit)

        rep += tens_digit_line + "\n"

        ones_digit_line = "   " + "0123456789" * 6

        rep += ones_digit_line + "\n"

        for row_num in range(self.num_rows):
            row_text = ""
            if row_num < 10:
                row_text += " "
            row_text += str(row_num) + " "
            for col_num in range(self.num_cols):
                pos = (row_num, col_num)
                item = self.ocean.get(pos)
                if item == self.empty_code:
                    row_text += random.choice(("~", "`"))
                if item == self.treasure_code:
                    if pos in self.found_treasures:
                        row_text += "T"
                    else:
                        row_text += random.choice(("~", "`"))
                if item == self.beacon_code:
                    dist = self.get_distance_to_treasure(pos)
                    if dist < 10:
                        row_text += str(dist)
                    else:
                        row_text += "X"

            row_text += " " + str(row_num)

            rep += row_text + "\n"

        rep += ones_digit_line + "\n"
        rep += tens_digit_line + "\n"

        return rep

    def play(self) -> None:
        # display greeting
        while (
            len(self.found_treasures) < self.num_treasures
            and self.num_beacons < self.max_beacons
        ):
            print(self)
            move = self.get_move()
            self.make_move(move)

        # display all treasures here?
        print(self)
        if len(self.found_treasures) == self.num_treasures:
            print("You found all the treasures! Great job!")
        else:
            print("You ran out of beacons. Better luck next time.")


game = SonarGame()
game.play()
