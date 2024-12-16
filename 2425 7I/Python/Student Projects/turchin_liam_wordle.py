#imports#
import random
import time
#classes#
class WordleGame:
    def __init__(self) -> None:
        self.max_guesses = 6
        self.guesses = 0
        self.points = 0
        self.player_guesses = []

        self.letters_guessed = ""
        self.letters_found = ""
        self.letters_not_in_word = ""
        self.powerup = ""

    def generate_word(self) -> str:

        word_list = [
"About",
"Alert",
"Argue",
"Beach",
"Above",
"Alike",
"Arise",
"Began",
"Abuse",
"Alive",
"Array",
"Begin",
"Actor",
"Allow",
"Aside",
"Begun",
"Acute",	
"Alone",	
"Asset",	
"Being",
"Admit",	
"Along",	
"Audio",
"Below",
"Adopt",
"Alter",
"Audit",
"Bench",
"Adult",
"Among",
"Avoid",	
"Billy",
"After",
"Anger",
"Award",	
"Birth",
"Again",
"Angle",
"Aware",	
"Black",
"Agent",	
"Angry",	
"Badly",
"Blame",
"Agree",	
"Apart",	
"Baker",	
"Blind",
"Ahead",	
"Apple",	
"Bases",	
"Block",
"Alarm",	
"Apply",	
"Basic",	
"Blood",
"Album",	
"Arena",	
"Basis",	
"Board",
"Boost",	
"Buyer",	
"China",	
"Cover",
"Booth",	
"Cable",	
"Chose",	
"Craft",
"Bound",	
"Calif",
"Civil",
"Crash",
"Brain",	
"Carry",	
"Claim",	
"Cream",
"Brand",	
"Catch",	
"Class",	
"Crime",
"Bread",	
"Cause",	
"Clean",	
"Cross",
"Break",	
"Chain",	
"Clear",	
"Crowd",
"Breed",	
"Chair",	
"Click",	
"Crown",
"Brief",	
"Chart",	
"Clock",	
"Curve",
"Bring",
"Chase",	
"Close",	
"Cycle",
"Broad",	
"Cheap",	
"Coach",	
"Daily",
"Broke",	
"Check",	
"Coast",	
"Dance",
"Brown",	
"Chest",	
"Could",	
"Dated",
"Build",	
"Chief",	
"Count",	
"Dealt",
"Built",	
"Child",	
"Court",	
"Death",
"Debut",	
"Entry",	
"Forth",	
"Group",
"Delay",	
"Equal",	
"Forty",	
"Grown",
"Depth",	
"Error",	
"Forum",	
"Guard",
"Doing",	
"Event",	
"Found",	
"Guess",
"Doubt",	
"Every",	
"Frame",	
"Guest",
"Dozen",	
"Exact",	
"Frank",	
"Guide",
"Draft",	
"Exist",	
"Fraud",	
"Happy",
"Drama",	
"Extra",	
"Fresh",	
"Harry",
"Drawn",	
"Faith",	
"Front",	
"Heart",
"Dream",	
"False",	
"Fruit",	
"Heavy",
"Dress",	
"Fault",	
"Fully",	
"Hence",
"Drill",	
"Fibre",	
"Funny",
"Night",
"Drink",	
"Field",	
"Giant",	
"Horse",
"Drive",	
"Fifth",	
"Given",	
"Hotel",
"Drove",	
"Fifty",	
"Glass",	
"House",
"Dying",	
"Fight",	
"Globe",
"Human",
"Eager",	
"Final",	
"Going",	
"Ideal",
"Early",	
"First",	
"Grace",	
"Image",
"Earth",	
"Fixed",	
"Grade",	
"Index",
"Eight",	
"Flash",	
"Grand",	
"Inner",
"Elite",	
"Fleet",	
"Grant",	
"Input",
"Empty",	
"Floor",	
"Grass",	
"Issue",
"Enemy",	
"Fluid",	
"Great",	
"Irony",
"Enjoy",	
"Focus",	
"Green",	
"Juice",
"Enter",	
"Force",	
"Gross",	
"Joint",
"Judge",	
"Metal",	
"Media",	
"Newly",
"Known",	
"Local",	
"Might",	
"Noise",
"Label",	
"Logic",	
"Minor",	
"North",
"Large",	
"Loose",	
"Minus",	
"Noted",
"Laser",	
"Lower",	
"Mixed",	
"Novel",
"Later",	
"Lucky",	
"Model",	
"Nurse",
"Laugh",	
"Lunch",	
"Money",	
"Occur",
"Layer",	
"Lying",	
"Month",	
"Ocean",
"Learn",	
"Magic",	
"Moral",	
"Offer",
"Lease",	
"Major",	
"Motor",	
"Often",
"Least",	
"Maker",	
"Mount",	
"Order",
"Leave",	
"March",	
"Mouse",	
"Other",
"Legal",	
"Music",	
"Mouth",	
"Ought",
"Level",	
"Match",	
"Movie",	
"Paint",
"Light",	
"Mayor",	
"Needs",	
"Paper",
"Limit",	
"Meant",	
"Never",	
"Party",
"Peace",	
"Power",	
"Radio",	
"Round",
"Panel",	
"Press",	
"Raise",	
"Route",
"Phase",	
"Price",	
"Range",	
"Royal",
"Phone",	
"Pride",	
"Rapid",	
"Rural",
"Photo",	
"Prime",	
"Ratio",	
"Scale",
"Piece",	
"Print",	
"Reach",	
"Scene",
"Pilot",	
"Prior",	
"Ready",	
"Scope",
"Pitch",	
"Prize",	
"Refer",	
"Score",
"Place",	
"Proof",	
"Right",	
"Sense",
"Plain",	
"Proud",	
"Rival",	
"Serve",
"Prove",	
"River",	
"Seven",
"Plant",	
"Queen",	
"Quick",	
"Shall",
"Plate",	
"Sixth",	
"Stand",	
"Shape",

    ]
        word = random.choice((word_list))
        word = word.lower()

        return word

    def get_player_guess(self) -> str:
        guess = input("Enter a guess: ")

        while not self.is_valid_guess(guess):
            guess = input("Enter a guess: ")

        self.player_guesses.append(guess) 

        return guess
    
    def give_player_hint(self, word: str) -> None:
        if self.powerup == "jumble":
            for letter in range(len(self.letters_found)):
                word_index = word.index(self.letters_found[letter])
                print(f"The letter {self.letters_found[letter]} is in place {word_index}")
                return
            for letter in range(5):
                if not word[letter] in self.letters_guessed:
                    print(f"Letter {word[letter]} is in the word")
        else:
            give_hint = input("Would you like a hint for 10 points (y or n)?\n") 
            if give_hint.startswith("y") and self.points > 10:
                self.points -= 10
                for letter in range(len(self.letters_found)):
                    word_index = word.index(self.letters_found[letter])
                    print(f"The letter {self.letters_found[letter]} is in place {word_index}")
                    return
                for letter in range(5):
                    if not word[letter] in self.letters_guessed:
                        print(f"Letter {word[letter]} is in the word")

    def guess_review(self, guess: str, word: str, name: str) -> None:
        self.letters_guessed = ""
        self.letters_found = ""
        if guess == word:
            print(f"Great job {name} for guessing the word! The word was {word}")
            self.points += 5
            print(f"Total points: {self.points}")
            return

        for letter_no in range(5):
            if guess[letter_no] == word[letter_no]:
                print("This letter is in the correct place.")
                self.letters_guessed += guess[letter_no]
                self.points += 1
                continue
            if guess[letter_no] in word:
                print("This letter is in the word, but not here.")
                self.letters_found += guess[letter_no]
                self.points += 0.5
            else:
                print("This letter isn't in the word.")
                if not guess[letter_no] in self.letters_not_in_word:
                    self.letters_not_in_word += guess[letter_no]
        print()

    def is_valid_guess(self, guess: str) -> bool:
        if len(guess) != 5:
            print("Improperly formatted input")
            return False
        
        if not guess.isalpha():
            print("Guess should only contain letters")
            return False
        
        if guess in self.player_guesses:
            print("Already guessed")
            return False
        
        return True

    def make_wordle_display(self) -> str:
        display = "\n"
        for guess in self.player_guesses:
            display += f"{guess}\n"
        
        for _ in range(self.max_guesses - len(self.player_guesses)):
            display += "-----\n"
        
        return display

    def play(self):
        print("Welcome to Wordle!\n")
        name = input("What is your name? ")
        print(f"""Okay {name}, wordle is a simple game where you guess
5 letter words to guess the correct word. Along the way,
you can get hints to help you if you need. Lets get started!""")
        time.sleep(5)
        play_again = "y"
        while play_again.startswith("y"):
            self.guesses = 0
            self.max_guesses = 6
            self.player_guesses = []
            self.letters_not_in_word = ""
            guess = ""
            word = self.generate_word()
            self.powerup = ""
            self.use_powerup()
            while guess != word and self.max_guesses != self.guesses:
                print(f"\nGuesses Remaining: {self.max_guesses - self.guesses}\nPoints: {self.points}\nLetters Not In The Word: {self.letters_not_in_word}")
                display = self.make_wordle_display() #creates display
                print(display) #prints display
                guess = self.get_player_guess() #get guess
                self.guess_review(guess, word, name) #tells user what there guess did #win text too#
                self.give_player_hint(word)
                self.guesses += 1
            
            if self.max_guesses == self.guesses:
                print(f"Sorry {name}, sorry. The word was {word}")
                print(f"Total points: {self.points}")
             
            play_again = input("\nWould you like to play again (y or n)? ")
                 
    def use_powerup(self) -> None:
        powerup = input("\nWould you like a random powerup this round (y or n)?\n")
        if powerup.startswith('y'):
            self.powerup = random.choice(("jumble", "guesses gone", "snorlax visit", "Anya visit"))
            if self.powerup == "guesses gone":
                print("Uh oh, you have been cursed! You now have 2 guesses to get the word!")
                self.max_guesses = 2
            if self.powerup == "jumble":
                print("A leprechaun came,  now you get a hint every guess!")
            if self.powerup == "snorlax visit":
                print("Snorlax visited and gave you more guesses!")
                self.max_guesses = 10
            if self.powerup == "anya visit":
                print("Anya came by and smashed your keyboard!")
                self.player_guesses.append("hoalt")
#game code#
game = WordleGame()
game.play()