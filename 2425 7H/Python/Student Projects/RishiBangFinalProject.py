import time
import random

play_again = str
play_again = "y"
name = ""
player_guess = ""
computer_guess = random.randint(1,3)
score = 0



def lock_1(score):
    print("Hi what is your name")
    name = input()
    print(f"well hi there {name}")
    time.sleep(2)
    print(" Here is your first challenge")
    time.sleep(1.5)
    print("solve all these math problems and multiply the first number of each of the answers")
    time.sleep(2)
    print("89 * 234")
    time.sleep(2)
    print("the square root of 144")
    time.sleep(2)
    print("674 - 143")
   
   
   
    player_input = input()
    if int(player_input) == 10:
        print("you got it right")

        score += 1
        
    else:
        print("wrong You loose")
        score -= 1
    return name
def lock_2(player_guess, score):
    print("so I see you made it past")
    time.sleep(2)
    print("but im only just getting started")


    print(" there will be 2 parts to this lock")
    print("part 1")
    print("what number on the periodic table is Ytterbium")


    player_guess == input()  
    print("You Got Part 1....")
    if player_guess != "70":
        
        time.sleep(2)
        print("wrong")
        score -= 1
    else: 
        time.sleep(2)
        print("correct")
        score += 1
        
    print("WELCOME to part 2 this is going to be very painful.")
    time.sleep(1)


    print("to figure out the code to this lock you will have to find the year vincent van gogh was born and the year he died in and multiply them together")
    player_guess = input()
    if player_guess != "3502170":
        print("WRONGGGGGG minus 1 point")
        score -= 1
    else:     
        print("Yay You finally got it")
        score += 1
def lock_3(score):
    print("welcome to lock 3")

    time.sleep(1)
    print("in this lock you will be taking a SAT level pop quiz")
    time.sleep(2)

    print(""" A gas station sells regular gasoline for $2.39 per
        
          gallon and premium gasoline for $2.79 per gallon. If the gas station sold

          a total of 550 gallons of both types of gasoline in one day

          for a total of $1,344.50, how many gallons of premium gasoline were sold?
          """)
    time.sleep(1)
    print(" (A)25 (B)75 (C)175 (D)475 ")


    player_guess  == input()
    print("you got it")
    if player_guess != "b":
        
        time.sleep(2)
        print("wrong")
        score -= 1
    
    else:
        score += 1
        print("right")



    time.sleep(1)
    print("Ok next question dont worry its not a math question")
    print("Which english city was named duroliponte?")
    player_guess  == input()
    print("WOW you got it")
    if player_guess.lower() != "Cambridge":
        time.sleep(2)
        print("wrong")
        score -= 1
    else:
        print("correct")
        score += 1
        
def rock_paper_scisors( computer_guess, play_again):
    print("welcome to rock paper scissors")
    time.sleep(1)
    print("do you know how to play?(yes or no)")
    player_guess = input()  


    if player_guess.startswith("Y"):

        print("ok let's get started")

    if player_guess.startswith("N"):
        print("ok here are the rules")
        print("You have to choose 3 objects: rock paper or scissors. Rock beats scissors, paper beats rock and scissors beats paper.")

    print("are you ready to start")
    player_guess = input()

    if player_guess.startswith("y"):
        print("ok lets start")

    else:
        print("too bad")

    print("rock, paper,scisors...")
    time.sleep(1)
    print("pick your item 1 rock 2 paper 3 scisors")
    player_guess = input()

    player_guess = int(player_guess)
    print(computer_guess)
    if computer_guess == player_guess:
        print(f"you both picked {computer_guess}")
        print("Its a tie too bad")
        print("looks like you have to restart")
        
        
        play_again = "n"

    if computer_guess == 2 and player_guess == 1:
        print("HAHAHAHAHAHAHAHAHAHHAAHHAHAHAHAHAHA ur soooooo bad bye  bye bye go restart and suffer")
        play_again == "n"
    
    if computer_guess == 3 and player_guess == 2:
        print("OMGGGGGGGGG u lost IM BETTER GO BACK TO THE START")
        play_again == "n"

    if player_guess == 1 and computer_guess == 3:
        print("U GOT LUCKY")
        play_again == "n"

    if player_guess == 2 and computer_guess == 1:
        print("luck luck luck luck dont talk to me lucky charms mascot")
        play_again == "n"
    if player_guess == 3 and computer_guess == 2:
        print("u are LITTERLY THE  LUCKYEST PERSON ALIVE")
        play_again == "n"

    if player_guess == 3 and computer_guess == 1:
        print("You came all this way just to lose and restart.")
        play_again == "n"
    






    


while play_again == "y":

   
    print("Welcome To My ESCAPE ROOM.")
    time.sleep(2)
    print("Listen Closely")
    time.sleep(2)
    print("You will have to solve 3 challenges to unlock 3 locks.")
    time.sleep(1)
    print("After you do that you will unlock the final lock")
    time.sleep(2)
    print("This may seem easy but trust me its not.")
    time.sleep(1)
    print("Good luck")


    lock_1(score)


    print("are You ready for lock #2")
    input()
   
    lock_2(player_guess, score)


    print("ok you may be better than I thought  but you are now 1 lock from the final lock so expect this to be hard.")


    print(f"are you ready {name}")
    lock_3(score)


    print("Ok you are better than the rest but for the final challenge you have to ....")
    time.sleep(3)
    print("WIN a game of rock paper scissors")


    rock_paper_scisors(computer_guess, play_again)

    time.sleep(2)
    print(f"your final score was {score}.")
    time.sleep(2)
    print("Do you want to play again")
    player_guess = input()
    if player_guess.startswith("y"):
        play_again = "y"

    else: 
        play_again = "n"
    
    