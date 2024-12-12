import random
import time
print(" Welcome to Kitty Doom! Whats your name?")
user_name = input()

def choose_food() -> str:
    cat = ""
    print("Which food type would you like to try?")
    cat = input()

    return cat

def display_intro() -> None:
    print(
    f"""Okay {user_name}, well this game is kind of like a guessing game.
    You have to guess what the cat, Snickers will want to eat, you can choose from
    the fish,meat or milk. 
    AND IF YOU MESS UP THE CAT WILL EAT YOU, AND YOU WOULD DESERVE IT!!!! >:(""")
    print(
    f"Ok, so are you ready to choose? Remember, you can choose drink - milk or food - fish. "
)

def cat_attack(chosen_food: str) -> None: 
            print (" You aproach the hangry cat.....")
            time.sleep(1)
            print(" The bright light that you were previously playing in now seems gloomy and dreadfull")
            time.sleep(2)
            print(" A large cat jumps out in front of u and you jump back in supprise! You give the cat your meal.... the cat.....")
            time.sleep(4)

display_intro()
chosen_food = choose_food()
cat_attack(chosen_food)
choice_food = random.choice (("milk","meat"))
print(chosen_food, choice_food)
if  chosen_food == choice_food :
    print("-She gives you an adorable nudge! YOU CHOOSE CORRECTLY!! Now... how about dessert?")
else:
    print(" SHE ATTACKS!!! OOF.. i guess you tasted better than what you choose...")

if choose_food != (("milk","meat")):
    print("please choose milk or meat, all lower case")
    print("Try again -_-")

play_again = "yes"
while play_again == "yes" or play_again == "y":

    print ("Do YOU wana play this AMAZING,FANTASTIC,WIERD, GAME?! Where you could posibly die?? :D (yes or no)")
    play_again = input()
    display_intro() 