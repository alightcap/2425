import random
import time


def choose_cave() -> str:
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def choose_weapon() -> tuple[int, str]:
    r_weapon_description = "boulder"
    p_weapon_description = "cloth"
    s_weapon_description = "spear"

    weapon_descriptions = (
        r_weapon_description,
        p_weapon_description,
        s_weapon_description,
    )
    chosen_weapon = 0
    while chosen_weapon not in ("1", "2", "3"):
        print(
            "You quickly look around the cave and spot a boulder, a large canvas, and a spear."
        )
        print("1 - boulder")
        print("2 - canvas")
        print("3 - spear")
        print("What will you pick up?")
        chosen_weapon = input()

    chosen_weapon = int(chosen_weapon)
    return (chosen_weapon, weapon_descriptions[chosen_weapon - 1])


def display_intro() -> None:
    print(
        """You are in a land full of dragon. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.\n"""
    )


def enter_cave(chosen_cave: str) -> None:

    r_dragon_description = "thick and scaly skin"
    p_dragon_description = "thin and flaky skin"
    s_dragon_description = "sharp and horned skin"

    chosen_dragon = random.randint(1, 3)
    dragon_description = (
        r_dragon_description,
        p_dragon_description,
        s_dragon_description,
    )[chosen_dragon - 1]

    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print(
        f"A dragon with {dragon_description}, jumps out in front of you! He opens his jaws and...\n"
    )
    time.sleep(2)

    chosen_weapon, weapon_description = choose_weapon()
    winner = resove_battle(chosen_dragon, chosen_weapon)

    if winner == "draw":
        print(
            "Your weapon cannot slay the dragon, but does deter it. It runs away and you leave the cave."
        )
        return
    if winner == "dragon":
        print(
            "Your weapon is ineffective against the dragon. It gobble you down in one bite!"
        )
    if winner == "player":
        print(
            "Your weapon intimidates the dragon. It offers to share it's treasure with you."
        )

    # friendly_cave = random.choice(("1", "2"))

    # if chosen_cave == friendly_cave:
    #     print("Gives you their treasure!")
    # else:
    #     print("Gobbles you down in one bite!")


def resove_battle(dragon: int, weapon: int) -> str:
    result = (dragon - weapon) % 3

    match result:
        case 0:
            return "draw"
        case 1:
            return "dragon"
        case 2:
            return "player"
        case _:
            return ""


play_again = "yes"
while play_again == "yes" or play_again == "y":
    display_intro()
    cave_number = choose_cave()
    # print(cave_number)
    enter_cave(cave_number)

    print("Do you want to play again? (yes or no)")
    play_again = input()
