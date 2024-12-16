import random


#hey josh. its gideon and reshi. GET OFF THE GAME. also you forgot el primo

def display_game(missed_letters: str, hidden_word: str):
    print(f"\n You have guessed incorrectly {len(missed_letters)} times")
    print(f"Missed_letters: {' '.join(missed_letters)}")
    print(f"\n{hidden_word}")



def get_guess(guessed_letters) -> str:
    guess = ""



                        
    print(f"Welcome to Hangman")  
    guess = input()

    while not is_valid(guess, guessed_letters):
        print(f"Enter Your Guess at a chance to win big time bucks. Also your guess should be a letter")
        guess = input()

    return guess
    

def is_valid(guess: str, guessed_letters: str) -> bool:
    if len(guess) != 1:
        print("Incorrect tu es poopy")
        
        return False


    if not guess.isalpha():
        print("Guess should be a letter")
        return False
    

    if guess in guessed_letters:
        print("You should be a real estate agent, BECAUSE YOUR SELLING. Also, you already guessed that.")
        return False
    
    


    
    
    return True



def make_hidden_word(secret_word:str, correct_letters: str) -> str:
    hidden_word = ""

    for letter in secret_word:
        if letter in correct_letters:
            hidden_word += letter
        
        elif letter.isalpha():
            hidden_word += "$"
        else:
            hidden_word += letter 
    
    
    return hidden_word

word_list_1 = [
    "kenji",
    "clancy",
    "gale",
    "frank",
    "meg",
    "lily",
    "darryl",
    "mortis",
    "surge",
    "kit",
    "chester",
    "byron",
    "amber",
    "nita",
    "poco",
    "cordelius",
    "crow",
    "rosa",
    "buzz",
    "dynamike",
    "colonel ruff",
    "larry and lawrie",

]

word_list_2 = [
    "american football",
    "basketball",
    "cricket",
    "diving",
    "equestrian",
    "formula one",
    "gymnastics",
    "horse racing",
    "ice hockey",
    "judo",
    "karate",
    "mixed martial arts",
    "netball",
    "rowing",
    "soccer"
    "tennis",
    "volleyball",
    "wrestling",
]

word_list_3 = [
    "sushi",
    "pecking duck",
    "fried dumplings",
    "steamed dumplings",
    "fried rice",
    "noodles",
    "mexican shrimp",
    "calamari",
    "hotdogs",
    "burger",
    "salmon",
    "chicken",
    "lamb",
    "fries",
    "chicken nuggets",
    "chicken tenders",
    "chicken fries",
    "spicy chicken sandwich with some bacon",
    "chips",
    "ramen",
]

word_list_4 = [
    "sword",
    "knife",
    "axe",
    "mace",
    "spear",
    "bow",
    "lance",
    "arrow",
    "bow",
    "boomerang",
    "numchucks",
    "rod",
    "deer horn knives",
    "yasss queen"
    "kris",
    "flanged mace",
    "spiked mace",
    "shuriken",
    "pata",
    "three sectioned staff",
    "quarter staff",
]

word_list_5 = [
    "the",
    "at",
    "win",
    "after",
    "loesr",
    "lose",
    "lol",
    "winner",
    "fried",
    "dinner",
    "know",
    "knew",
    "no",
    "yes",
    "Wassup",
    "Wazzap",
    "cool",
    "migl",
    "gideon is slay"
    "es",
    "stupid",
    "y",
    "skibid",
    "chicken",
    "chick",
    "boy",
    "girl",
    "man",
    "women",
    "gramps",
    "pops",
    "grams",
    "pounds",
    "dollar",
    "ghana",
    "cedi",
]

play_again = [

]


max_wrong_guesses = 6
play_again = True


print("H A N G M A N")

while play_again:

    correct_letters = ""
    wrong_letters = ""


    secret_word = random.choice(word_list_1, word_list_2, word_list_3, word_list_4, word_list_5)
    hidden_word = make_hidden_word(secret_word, correct_letters)
    #print(hidden_word)
    #print(secret_word)

    while secret_word != hidden_word and len(wrong_letters) < max_wrong_guesses:
        display_game(wrong_letters, hidden_word)

        guess = get_guess(correct_letters + wrong_letters)

        if guess in secret_word:
            correct_letters += guess
            hidden_word = make_hidden_word(secret_word, correct_letters)
        else:
            wrong_letters += guess

    print(f"The Word Was {secret_word}")
    if secret_word == hidden_word:
        print("""Congraulation. YOu dont have a skill issue
        
            ⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
            ⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
            ⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
            ⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
            ⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
            ⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
            ⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠀⠀⠀⠀⠀⠀
            This is your 1st trophy. The more levels you beat the more you gain. 
            Each trophy is different and special in its own way 
            Beat five levels to be the trophy champion!""")
        print("Would you like to advance to the next level, sports?")
        play_again = input().lower().startswith("y")
        if input().startswith("y"):
            play_again
        else: 
            print("🎶Whomp Whomp, you quit your so skibid🎶")


    else:
        print("Too bad, So sad")



    

    




# print(hidden_word)
#display_game(wrong_letters, hidden_word)

