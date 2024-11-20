import random

guesses_taken = 0
max_guesses = 6
guess = 0

print("Hello! Welcome to Guess The Number!")
print("What is your name?")
user_name = input()

print(f"Well, {user_name}, I am thinking of a number between 1 and 10.")

secret_number = random.randint(1, 10)
print(secret_number)

while guess != secret_number and guesses_taken < max_guesses:
    print("\nTake a guess:")
    guess = input()
    # for now we will trust the user to enter a valid input
    guess = int(guess)
    guesses_taken += 1
    # guesses_taken = guesses_taken + 1

    if guess < secret_number:
        print("Your guess is too low.")

    if guess > secret_number:
        print("Your guess is too high.")

if guess == secret_number:
    print(f"Good job {user_name}! You guessed my number in {guesses_taken} guesses!")
else:
    print(f"Nope. THe number I was thinking of was {secret_number}.")
