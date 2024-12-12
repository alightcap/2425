import time

#8. Add all of the code into a game *cough cough* nOt dOne heheh

#CHECK: 
# - The functions are alphabetized
# - The functions have the write data inside of them
# - The functions are returning ( -> ) the right data


# *COUGH COUGH*

# Before you read my code mr lc
# just IMAGINE that it's A++ worthy
#very professional work 💼
# k? :D
# ur prob like 

# OH THIS WILL BE INTERESTING 
#
#
# ... no
# it's not  😭


#____________________________________________________________________________________________________________________________________________________________________________________________________


class Board():

    #Square
    num_rows = 7 
    num_cols = 7
    empty = " "
    dot = "+"
    hyphen = "-"
    pipe = "|"
    empty_space = 0
    

    def __init__(self, empty: str, num_rows:int, num_cols:int) -> None: 

        self.cells = self.generate_board(num_rows, num_cols, empty)


    def __str__(self) -> str: #TODO 

        rep = ""

        rep += self.generate_board

        return rep


    def generate_board (num_rows: int, num_cols: int, empty: str, dot: str) -> None:



        cells = []
        #for the two spaces before the column numbers
        cells.append(empty)
        cells.append(empty)
        for col in range (num_cols):
            cells.append(col)
        # adding a blank line
        cells.append("\n")


        for r in range (num_rows):
            # For each row i will make a list :D

            row = []
            #we are using r to know what row for the numbers at the beginning of the line
            row.append(r)
            row.append(empty) #the blank space between row number and board
            for col in range (num_cols):
                if col % 2 == 0 and row % 2 == 0:
                    row.append(dot)
                else:
                    row.append(empty)
            cells.append(row)

                

                

        return cells


class DotsAndSquaresGame():

    def cell_position(num_rows: int, num_cols: int, r: int, c: int) -> int:
        # r times num_cols plus two because there are two extra columns at the beginning of each row
        # 5 because there are 5 extra characters before we get to the board (not including the numbers on top)
        return r*(2+num_cols) + c + (5+num_cols)


    def fill_square (board:list [str], square_complete:bool, whose_turn:bool, r:int, c:int, player_one_points: int, player_two_points: int, player_one_symbol: str, player_two_symbol: str ) -> str: 

        #figuring out which character to put where once a square is complete
        if square_complete == True:
            if whose_turn == True:
                board[r, c] = player_one_symbol
                player_one_points +=1 

            else:
                board[r, c] = player_two_symbol
                player_two_points += 1
            

    def get_starting_move (board: list[str], is_valid_move:bool) -> str:
        moves_played = 0
        print (f"Hey! Where would you like to move?")
        move = input()
        moves_played += 1

        while not is_valid_move(board, move):
            print ("Please try again")
            move = input()

        return move


    def go_again (board:list [str], whos_turn:bool, square_complete:None ) -> None: 
        if square_complete == True and whose_turn == True:
            print ("PLAYER ONE congrats you get to go again :D")
        if square_complete == True and whose_turn == False:
            print ("PLAYER TWO congrats you get to go again :D")


    def is_valid_move (board:list [str], player_move:str) -> bool: 

        row_str, col_str = player_move.split (" ")

        row_num = int(row_str)
        col_num = int(col_str)


        if player_move != int:
            print ("Please use only numbers (did you add a comma?)")
            return False
        
        if player_move.count(" ") != 1:
            print ("Improperly formatted input")
            return False
        

        if not input().isdigit():
            print ("Imput is not numerical")
            return False
        
        if col_num % 2 == 0 and row_num % 2 == 0:
            print ("Cannot move on a dot")
            return False
        
        if col_num % 2 == 1 and row_num % 2 == 1:
            print ("Cannot move in a space, only an edge")
            return False
        
        return True
             

    def square_complete (board: list [str], r:int, c:int, cells:str, hyphen:str, pipe: str, cell_position:int) -> bool: 
        #checking if a particular square is complete
        empty_spaces = 4
        if cells [cell_position [r-1, c]] == hyphen and cells [cell_position[r, c-1]] == pipe and cells [cell_position [r, c+1]] == pipe and cells [cell_position [r+1, c]] == hyphen:
            empty_spaces -=1
            return True


    def placing_line (board:list [str], col_str: str, row_str: str, line:str, hyphen: str, pipe: str, cells: str) -> str: 

        if col_str % 2 == 1 and row_str % 2 == 0:
            line = hyphen
        if col_str % 2 == 0 and row_str % 2 == 1:
            line = pipe


        #changing one part of the string, cells, so that it can do what is needed (changing board)
        change = self.cell_position(num_rows = 7, num_cols = 7, r = row_str, c = col_str )

        #getting the specific location in the string, cells
        cells[change] = line
        
        return line


    def play (self, empty: str, empty_spaces: int) -> None:
        while empty == " ":
            print (self)
            move = self.is_valid_move()
            self.placing_line(move)

            print (self)
            if empty_spaces == 0: #if the empty squares are all filled than use the who wins
                self.who_wins         


    def whose_turn (move: int, player_one_moved: bool, moves_played: int) -> bool:


        if moves_played % 2 == 1:
            player_one_moved == True
        else:
            player_one_moved = False


    def who_wins (player_one_points:int, player_two_points:int ) -> int: 
        
        if player_one_points > player_two_points:
            print ("PLAYER ONE WINS WOHOOO!!")
            return 1
        if player_two_points > player_one_points:
            print ("PLAYER TWO WINS WOHOO!!")
            return 2
        if player_one_points == player_two_points:
            print ("Wait, you tied? HOW?!")
            return 0

play_again_input = True

while play_again_input == True:


    player_one_symbol = "🌙"
    player_two_symbol = "☀️"
    player_one_points = 0
    player_two_points = 0
            

    print ("Welcome to Dots and Squares!")
    time.sleep (1)
    print ("\nPlease, tell me player 1's name")
    player_one_name = input()
    print ("\nGreat! Now tell me player 2's name")
    player_two_name = input()  
    #CRINGY NAME ALERT UP AHEAD!!!!! 📣📣📣🗣️🗣️🗣️
    print (f"""\nIn this game, {player_one_name} and {player_two_name},

    you guys will compete to figure out who is the champion 

    of square land! {player_one_name}, you will go first and 

    type in the coordinates of the spot you would like to move 
            
    to place a line there. Make sure that spot isn't already 

    occupied! Then, {player_two_name} will type in the coordinates

    of the location they would like to move. Connecting a whole 

    square gives you a point! {player_one_name}, you will be 🌙 
            
    and {player_two_name} will be ☀️. The tournament starts.... """)

    time.sleep (2) #change this after experimentation

    print ("NOW!!!!")


    game = DotsAndSquaresGame()
    game.play(Board(empty, empty_spaces))


    print(f"\nTell me, {player_one_name} and {player_two_name}, would you like to play again?")

    answer = input()

    if answer.startswith("y") or answer.startswith("Y"):
        print ("\nOMG ACTUALLY!?!?!!")
        play_again_input = True
    else:
        print ("How dare you not wanna play my game (tho i don't really blame you...) >:(")
        play_again_input = False

