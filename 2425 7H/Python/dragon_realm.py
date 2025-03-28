import random
import time


def choose_cave() -> str:
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def display_intro() -> None:
    print(
        """You are in a land full of dragon. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n"""
    )


def enter_cave(chosen_cave: str) -> None:
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...\n")
    time.sleep(2)

    friendly_cave = random.choice(("1", "2"))

    if chosen_cave == friendly_cave:
        print("Gives you their treasure!")
    else:
        print("Gobbles you down in one bite!")


play_again = "yes"
while play_again == "yes" or play_again == "y":
    display_intro()
    cave_number = choose_cave()
    # print(cave_number)
    enter_cave(cave_number)

    print("Do you want to play again? (yes or no)")
    play_again = input()
