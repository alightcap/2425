import random


def display_game(missed_letters: str, hidden_word: str) -> None:
    print(f"\nYou have guessed incorrectly {len(missed_letters)} times.")
    print(f"Missed letters: {" ".join(missed_letters)}")
    print()
    print(hidden_word)


def get_guess(already_guessed: str) -> str:
    guess = ""
    print("\nEnter a guess: ")
    guess = input()

    while not is_valid(guess, already_guessed):
        print("Please guess again: ")
        guess = input()

    return guess


def is_valid(guess: str, already_guessed: str) -> bool:
    if len(guess) != 1:
        print("Your guess should contain only 1 character")
        return False

    if guess in already_guessed:
        print("You have already guessed that letter")
        return False

    if not guess.isalpha():
        print("You must enter a letter")
        return False

    return True


def make_hidden_word(secret_word: str, correct_letters: str) -> str:
    hidden_word = ""

    for letter in secret_word:
        if letter in correct_letters:
            hidden_word += letter

        elif not letter.isalpha():
            hidden_word += letter

        else:
            hidden_word += "*"

    return hidden_word


word_list = [
    "star wars",
    "luke skywalker",
    "han solo",
    "leia organa",
    "chewbacca",
    "obi-wan kenobi",
    "darth vader",
    "ahsoka tano",
]

max_wrong_guesses = 6
play_again = True

print("H A N G M A N")
while play_again:
    missed_letters = ""
    correct_letters = ""
    secret_word = random.choice(word_list)
    hidden_word = make_hidden_word(secret_word, correct_letters)

    # print(secret_word)
    # print(hidden_word)
    while hidden_word != secret_word and len(missed_letters) < max_wrong_guesses:
        display_game(missed_letters, hidden_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess
            hidden_word = make_hidden_word(secret_word, correct_letters)
        else:
            missed_letters += guess

    # display_game(missed_letters, hidden_word)
    print(f"The secret word was {secret_word}.")
    if hidden_word == secret_word:
        print("Congratulations! You win!")
    else:
        print("Too bad! You ran out of guesses.")

    print("\nWould you like to play again?")
    play_again = input().lower().startswith("y")
