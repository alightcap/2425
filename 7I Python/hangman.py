import random


def display_game(missed_letters: str, hidden_word: str) -> None:
    print(f"\nYou have guessed incorrectly {len(missed_letters)} times.")
    print(f"Missed letters: {' '.join(missed_letters)}")
    print(f"\n{hidden_word}")


def get_guess(guessed_letters: str) -> str:
    guess = ""

    print("Enter a guess:")
    guess = input()

    while not is_valid(guess, guessed_letters):
        print("Enter a guess:")
        guess = input()

    return guess


def is_valid(guess: str, guessed_letters: str) -> bool:
    if len(guess) != 1:
        print("Guess should be one letter only.")
        return False

    if not guess.isalpha():
        print("Guess should be a letter.")
        return False

    if guess in guessed_letters:
        print("Already guessed.")
        return False

    return True


def make_hidden_word(secret_word: str, correct_letters: str) -> str:
    hidden_word = ""

    for character in secret_word:
        if character in correct_letters:
            hidden_word += character
        elif character.isalpha():
            hidden_word += "*"
        else:
            hidden_word += character

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
    correct_letters = ""
    wrong_letters = ""

    secret_word = random.choice(word_list)
    hidden_word = make_hidden_word(secret_word, correct_letters)
    # print(secret_word)
    # print(hidden_word)
    while secret_word != hidden_word and len(wrong_letters) < max_wrong_guesses:
        display_game(wrong_letters, hidden_word)
        guess = get_guess(correct_letters + wrong_letters)

        if guess in secret_word:
            correct_letters += guess
            hidden_word = make_hidden_word(secret_word, correct_letters)
        else:
            wrong_letters += guess

    print(f"The secret word was {secret_word}.")
    if secret_word == hidden_word:
        print("Congratulations! You win!")
    else:
        print("Too bad. You ran out of guesses.")

    print("\nWould you like to play again?")
    play_again = input().lower().startswith("y")

# print(hidden_word)
# display_game(wrong_letters, hidden_word)
