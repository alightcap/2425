import time
import random

# Ideas
# Clue 1 ✔✔✔ - Math (Four equations)
# Clue 2 ✔✔✔ - Sewer dive (Player needs to wait to get clue.)
# Clue 3 - Search for key in pipe
# Clue 4 - Don't die game but find key (chances AND help)
# Clue 5 ✔✔✔- Swim again but better somehow
# Clue 6 - Grand finale


# Board/UI Setup

GradLow = "░"
GradMed = "▒"
GradHigh = "▓"
Check = "✔"
Cross = "X"

playernumber = random.randint(1, 9999)
botnumber = random.randint(1, 9999)

ClueI= f"Clue 1: {Cross}"
ClueII = f"Clue 2: {Cross}"
ClueIII = f"Clue 3: {Cross}"
ClueIV = f"Clue 4: {Cross}"
ClueV = f"Clue 5: {Cross}"
ClueVI = f"Clue 6: {Cross}"
# Tutorial Functions
def tutorial_E():
        print("\nTo interact with an item, enter (E).")
        userinput = input()

        while not userinput == "E":
                print("Try again.")
                userinput = input()
        
        print("Good job. Now let's move on to the next part of the tutorial.")
        time.sleep(2)
def tutorial_task():
        print("Solve the following equation to get the answer.")
        tutorial_num_1 = random.randint(1,30)
        tutorial_num_2 = random.randint(31, 60)
        tutorial_equation = (tutorial_num_1 + tutorial_num_2)

        print(f"{tutorial_num_1} + {tutorial_num_2}")
        answer = input()
        equation_answer = str(tutorial_equation)

        while not answer == equation_answer:
                print("Wrong answer, try again.")
                answer = input()

        print("Good job.")
        time.sleep(2)
def game_choice():
        print("Would you like to try the tutorial?\n\nEnter 'yes' to start tutorial.")
        userinput = input()
        if userinput == "yes" or userinput == "Yes":
                print("Tutorial it is.")
                time.sleep(1)
                tutorial()
        else:
                print(f"{userinput}? Let's start then.")
                time.sleep(2)
                Clue_1()
def tutorial():
       rustybot_speech()
       print("How this will work, is you will need to find clues around the room in order to escape.")
       time.sleep(3)
       print("\nYou will do tasks like fixing pipes, solving math problems and secret codes.")
       time.sleep(3)
       print("\nIf you ever need help, don't bother asking me. I don't really care.")
       time.sleep(3)
       print("\nI have better things to do, like being a rusty pipe and conducting sewer water.")
       time.sleep(3)
       print("\nEnough talking, now that I've told you what you need to do, heres how to do it.")
       time.sleep(3)
       tutorial_E()
       tutorial_task()
       print("\nNow that you've FINALLY completed the tutorial, lets move on to the game itself.")
       time.sleep(3)
       Clue_1()

# Print Functions
def empty_floor():
        print(f"{GradHigh*2}{GradLow*36}{GradHigh*2}")
def rustybot_speech():
        print(f"[RUSTYMETALPIPE-{botnumber}]:")

# UI
def title():   
        print("\n\n")
    
        print("▓▓▓▓▓ ▓▓▓▓▓ ▓ ▓ ▓ ▓▓▓▓▓ ▓▓▓▓    ▓▓▓▓▓▓▓")
          
        print("▓     ▓     ▓ ▓ ▓ ▓     ▓   ▓   ▓▓   ▓▓")
          
        print("▓▓▓▓▓ ▓▓▓▓▓ ▓ ▓ ▓ ▓▓▓▓▓ ▓▓▓▓    ▓ O-+ ▓")

        print("    ▓ ▓      ▓ ▓  ▓     ▓   ▓   ▓▓   ▓▓")

        print("▓▓▓▓▓ ▓▓▓▓▓  ▓ ▓  ▓▓▓▓▓ ▓   ▓   ▓▓▓▓▓▓▓")
        time.sleep(1)
        print("E S C A P E")
        time.sleep(1)
        print("BY ENZO GALL\n\n")
        time.sleep(1)
def board():
        print(f"{GradLow*40}\n{GradMed*40}\n{GradHigh*40}")
        empty_floor()
        print(f"{GradHigh*2}{ClueI}{GradLow*18}{ClueIV}{GradHigh*2}")
        empty_floor()
        print(f"{GradHigh*2}{ClueII}{GradLow*18}{ClueV}{GradHigh*2}")
        empty_floor()
        print(f"{GradHigh*2}{ClueIII}{GradLow*18}{ClueVI}{GradHigh*2}")
        empty_floor()
        print(f"{GradHigh*40}\n{GradMed*40}\n{GradLow*40}")

# Clues
def Clue_1():
        code1 = random.randint(100000,999999)
        code2 = random.randint(2,9)
        add = (code1*2)
        sub = (code1 - (code1*0.5))
        mult = (code1*code2)
        div = (code1/code2)

        print("\nClue 1 - Pipe fixing.\n\n")
        rustybot_speech()
        print(f"To break open the pipe, enter code ({code1}).")

        userinput = input()
        while not userinput == f"{code1}":
                print("Almost, retry.")
                userinput = input()
        print("Good job.")

        time.sleep(1)
        #Addition
        print("Solve the equations to continue")
        print(add)
        print(f"What is {code1} + {code1}?")
        while not userinput == f"{add}":
                print("Almost, retry.")
                userinput = input()
        #Subtraction
        print(f"What is {code1} - {code1*0.5}")
        print(sub)
        while not userinput == f"{sub}":
                print("Almost, retry.")
                userinput = input()
        #Multiplication
        print(f"What is {code1} x {code2}")
        print(mult)
        while not userinput == f"{mult}":
                print("Almost, retry.")
                userinput = input()
        #Division
        print(f"What is {code1} ÷ {code2}")
        print(div)
        while not userinput == f"{div}":
                print("Almost, retry.")
                userinput = input()

        print(f"Great job, the first key is cleared. Let's do clue 2.")
        global ClueI
        ClueI = (f"Clue 1: {Check}")
        print(ClueI)
        board()
        time.sleep(2)
        Clue_2()
def Clue_2():
        print("\nClue 2 - Sewer Swim I.\n\n")
        time.sleep(2)
        rustybot_speech
        print("That means I get to go for my first swim!")
        time.sleep(2)
        print("In the...")
        time.sleep(2)
        print("Dirty sewer water...")
        time.sleep(2)
        print("Let me go get the key, i'll be back in a few (Ten) seconds.")
        time.sleep(3)
        print("Do some counting while im gone.\n\n")
        time.sleep(2)
        print("One")
        time.sleep(1)
        print("Two")
        time.sleep(1)
        print("Three")
        time.sleep(1)
        print("Four")
        time.sleep(1)
        print("Five")
        time.sleep(2)
        print("Eight")
        time.sleep(2)
        print("Nineteen")
        time.sleep(1)
        print("42²")
        time.sleep(1)
        print("Nine hundred thousand million\nbillion trillion quadrillion\nquintillion-")
        time.sleep(3)
        rustybot_speech()
        print("Ten, here's the key.")
        time.sleep(2)
        print("You ungrateful person.")
        time.sleep(2)
        print("Let's do clue 3.")
        global ClueII
        ClueII = (f"Clue 2: {Check}")
        print(ClueII)
        board()
        time.sleep(2)
        Clue_3()
def Clue_3():
        print("I messed up this clue so it's skipped.")
        time.sleep(1)
        Clue_4()
def Clue_4():
        print("I messed up this on too so also a skip.")
        time.sleep(1)
        Clue_5()
def Clue_5():
        print("\nClue 5 - Sewer Swim II\n\n")
        rustybot_speech()
        print("Onto the fifth task. Im gonna swim... again.")
        time.sleep(2)
        print("But this time, you're coming with me.")
        time.sleep(2)
        print("Get ready to dive in 3... 2... 1...")
        time.sleep(3)
        print("*SPLASH*")
        time.sleep(1)
        rustybot_speech()
        print("You need to catch one of the sewer fish.")
        time.sleep(2)
        print("They are fast, so that means you need to be fast too.")
        time.sleep(2)
        print("You will have some time to enter a code into the sewer fish's number pad.")
        time.sleep(3)
        print("Ready? Go!")
        time.sleep(1)
        randomfish1()
        global ClueV
        ClueV = (f"Clue 5: {Check}")
        print(ClueV)
        board()
        time.sleep(2)
        Clue_6()
def Clue_6():
        print("\nClue 6 - C̴̖͕̾l̵̹̓i̵̗̩͝m̴b̸͈̊ P̴̳̋͛i̷̻̓p̶̦̣͘ȩ̴͔̔͑")
        time.sleep(2)
        rustybot_speech()
        print("Wait, whats h̷̩̽͝a̵͎̱͛p̸̟̍p̴̱̓é̸̗͂n̵̬͋i̴̥͠n̶̳͓̈͒g̵̢̜̕ to M̸̡̛̤̖͍̱͚̳̠͋̿̊̐E̷̗̓̏͑̑!?")
        time.sleep(2)
        print("Q̷͇̜̆́Ǔ̶͉Ȋ̸̹Č̵Ḳ̷̨͂̆!̴̯̱͘\n CLIMB TO THE TOP OF THE P̴̝̖͙͆Ị̴̐̑̍̿͆P̴̛͇̫̱͑̿́͘E̸̟̬̝̙͙̋́͐̈́ BEFORE I D̷̲͙̳̫͈̺̏͛Ȩ̸̧̝̳̟͚͔̞̲̾̔̀̊͆̿S̵̨̧̢̠̻͓̝̲͕̠͉̥̘̯̋̋͒Ţ̷̲͕̯̳̤̭̺̱͕͕̤̏̐̓͋̇̌̽̾͑͑R̸̛͉͓̠̫̔̏̉̋̅̉͐̆̍̊̌̉̈͐͝͝Ờ̸̛̩̼͕̱̲͚̭̩͓̱̙̘̼̿̏̂̿̑͒̽͘͜ͅỶ̸̠͚͉̪̮̪̭͇͇̗͒̐ YOU!")
        time.sleep(2)
        print("YOU HAVE 60 SECONDS BEFORE-")
        time.sleep(2)
        print("G̵͍̭͋O̵̱̎͠")
        time.sleep(1)
        Climb_1()

# Game
def introduction():
        print(f"[RUSTYMETALPIPE-{botnumber}]:")
        print(f"Welcome to the sewers, prisoner {playernumber}! My name is rustymetalpipe-{botnumber}...")
        time.sleep(3)
        print("\nBut you can call me robot.")
        time.sleep(2)
        print("\nNow that I think of it, whats your REAL name?")
        time.sleep(2)
        print("\nHello, my name is:")
        name = input()
        time.sleep(1)
        print("\nWow! I absolutely hate that name.")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print(f"\nIl just call you {name}{playernumber}. How does that sound?")
        time.sleep(3)
        print("\nNot that your opinion matters to me, lets continue.\n\n\n")
        time.sleep(3)
        return name
def play():
        title()
        introduction()
        game_choice()
def playagain():
        print("Would you like to play again?")
        userinput = input()
        if userinput == "yes" or userinput == "Yes":
                        Clue_1()       
        time.sleep(1)
        print("Goodbye")
        time.sleep(2)
def randomfish1():
        fishnumber = random.randint(100, 9999)
        print(f"Enter code: {fishnumber}")
        userinput = input()
        inputint = int(userinput)
        if inputint == fishnumber:
                print("You did it!")
                time.sleep(1)
                print("Nevermind it got away.")
                time.sleep(2)
                randomfish2()
        else:
                print("Incorrect, try again.")
                time.sleep(1)
                randomfish1()
def randomfish2():
        fishnumber = random.randint(100, 9999)
        print(f"Enter code: {fishnumber}")
        userinput = input()
        inputint = int(userinput)
        if inputint == fishnumber:
                print("This time, you actually caught it, good job.")
                time.sleep(2)
                Clue_6()
        else:
                print("Incorrect, try again.")
                time.sleep(1)
                randomfish2()
def Climb_1():
        code = random.randint(1000000,9999999)
        print("\nENTER THE FOLLOWING CODE TO PROCEED.")
        time.sleep(1)
        print(code)
        userinput = input()
        inputint = int(userinput)

        while not inputint == code:
                print("INVALID CODE")
                userinput = input()
                inputint = int(userinput)
        
        print("YOU CAN NOW PROCEED")
        time.sleep(1)
        print("-=40 SECONDS LEFT=-")
        time.sleep(1)
        Climb_2()
def Climb_2():
        code1 = random.randint(10,30)
        code2 = random.randint(10,30)
        code3 = random.randint(10,30)
        answer = (code1+code2+code3)

        print(f"What is {code1} + {code2} + {code3}?")
        print(answer)
        userinput = input()
        inputint = int(userinput)

        while not inputint == answer:
                print("INVALID ANSWER")
                userinput = input()
                inputint = int(userinput)
        
        print("YOU CAN NOW PROCEED")
        time.sleep(1)
        print("-=20 SECONDS LEFT=-")
        time.sleep(1)
        Climb_3()
def Climb_3():
        print("\nending here i guess")
        time.sleep(1)
        playagain()
play()