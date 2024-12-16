import time

def display_intro() -> None:

    print("Welcome to Connect 4!!")
    time.sleep(1)
    print("I'm sure that all of you know how to play but for those who don't, connect four is basically tic tac toe but you need to get 4 in a row instead of 3.")
    time.sleep(1)
    print("\nHey you there! You will be player 1 so go ahead and tell me your name")
    player_1_name = input()
    time.sleep(1)
    print("Well well well... another challenger I see. What is your name?")
    player_2_name = input()
    print("Ok great! you will be player 2!")
    time.sleep(1)
    print(f"Ok heres how this is gonna work. {player_1_name} is gonna be X's and {player_2_name} is gonna be O's! ")


def display_board(board: list[str]) -> None:
    #col 7 is in multiples of 7
    #col 1 is 1 less than col 2 
    #col 2 is 1 less than col 3 etc.
    #All the numbers in column 1 are 1 greater than a multiple of 7
    #All of the numbers in column 2 are 2 greater than a multiple of 7 etc.
    print(f"""
    
    | {board[36]} | {board[37]} | {board[38]} | {board[39]} | {board[40]} | {board[41]} | {board[42]} |
    ------------------------------
    | {board[29]} | {board[30]} | {board[31]} | {board[32]} | {board[33]} | {board[34]} | {board[35]} |
    ------------------------------
    | {board[22]} | {board[23]} | {board[24]} | {board[25]} | {board[26]} | {board[27]} | {board[28]} |
    ------------------------------
    | {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} | {board[20]} | {board[21]} |
    ------------------------------
    | {board[8]} | {board[9]} | {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} |
    ------------------------------
    | {board[1]} | {board[2]} | {board[3]} | {board[4]} | {board[5]} | {board[6]} | {board[7]} |
    ------------------------------

             

                    """)


def get_player_move() -> int:
    print("Which column would you like to place your token in? (1-7)")
    player_move = input()
    while not is_valid_input(player_move):
        player_move = input()
    return int(player_move)


def make_player_move(board:list[str], move: int, current_player: str) :

    move_done = False
    index = move
    while index < 43 and move_done == False:
        if board[index] == EMPTY:
            board[index] = current_player
            move_done = True
        else:
            index += 7

    if index >= 43:      
        print("No slots available in this column")


def is_winner(board: list[str], piece:str) -> bool:
    #All vertical wins
    if board[1] != EMPTY and board[1] == board[2] == board[3] == board[4] == piece:
        print("You win!")
        return True
    if board[2] != EMPTY and board[1] == board[3] == board[4] == board[5] == piece:
        print("You win!")
        return True
    if board[3] !=  EMPTY and  board[3] == board[4] == board[5] == board[6] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[5] == board[6] == board[7] == piece:
        print("You win!")
        return True
    if board[1] != EMPTY and board[1] == board[8] == board[15] == board[22] == piece:
        print("You win!")
        return True
    if board[8] != EMPTY and board[8] == board[15] == board[22] == board[29] == piece:
        print("You win!")
        return True
    if board[15] != EMPTY and board[15] == board[22] == board[29] == board[36] == piece:
        print("You win!")
        return True
    if board[2] != EMPTY and board[2] == board[9] == board[16] == board[23] == piece:
        print("You win!")
        return True
    if board[9] != EMPTY and board[9] == board[16] == board[23] == board[30] == piece:
        print("You win!")
        return True
    if board[16] != EMPTY and board[16] == board[23] == board[30] == board[37] == piece:
        print("You win!")
        return True
    if board[17] != EMPTY and board[17] == board[24] == board[31] == board[38] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[11] == board[18] == board[25] == piece:
        print("You win!")
        return True
    if board[11] != EMPTY and board[11] == board[18] == board[25] == board[32] == piece:
        print("You win!")
        return True
    if board[18] != EMPTY and board[18] == board[25] == board[32] == board[36] == piece:
        print("You win!")
        return True
    if board[5] != EMPTY and board[5] == board[12] == board[19] == board[26] == piece:
        print("You win!")
        return True
    if board[12] != EMPTY and board[12] == board[19] == board[26] == board[33] == piece:
        print("You win!")
        return True
    if board[19] != EMPTY and board[19] == board[26] == board[33] == board[40] == piece:
        print("You win!")
        return True
    if board[6] != EMPTY and board[6] == board[13] == board[20] == board[27] == piece:
        print("You win!")
        return True
    if board[13] != EMPTY and board[13] == board[20] == board[27] == board[34] == piece:
        print("You win!")
        return True
    if board[20] != EMPTY and board[20] == board[27] == board[34] == board[41] == piece:
        print("You win!")
        return True
    if board[7] != EMPTY and board[7] == board[14] == board[21] == board[28] == piece:
        print("You win!")
        return True
    if board[14] != EMPTY and board[14] == board[21] == board[28] == board[35] == piece:
        print("You win!")
        return True
    if board[21] != EMPTY and board[21] == board[28] == board[35] == board[42] == piece:
        print("You win!")
        return True
    #All Horizontal Wins
    #Row 1
    if board[1] != EMPTY and board[1] == board[2] == board[3] == board[4] == piece:
        print("You win!")
        return True
    if board[2] != EMPTY and board[2] == board[3] == board[4] == board[5] == piece:
        print("You win!")
        return True
    if board[3] != EMPTY and board[3] == board[4] == board[5] == board[6] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[5] == board[6] == board[7] == piece:
        print("You win!")
        return True
    #Row 2
    if board[8] != EMPTY and board[8] == board[9] == board[10] == board[11] == piece:
        print("You win!")
        return True
    if board[9] != EMPTY and board[9] == board[10] == board[11] == board[12] == piece:
        print("You win!")
        return True
    if board[10] != EMPTY and board[10] == board[11] == board[12] == board[13] == piece:
        print("You win!")
        return True
    if board[11] != EMPTY and board[11] == board[12] == board[13] == board[14] == piece:
        print("You win!")
        return True
    #Row 3
    if board[15] != EMPTY and board[15] == board[16] == board[17] == board[18] == piece:
        print("You win!")
        return True
    if board[16] != EMPTY and board[16] == board[17] == board[18] == board[19] == piece:
        print("You win!")
        return True
    if board[17] != EMPTY and board[17] == board[18] == board[19] == board[20] == piece:
        print("You win!")
        return True
    if board[18] != EMPTY and board[18] == board[19] == board[20] == board[21] == piece:
        print("You win!")
        return True
    #Row 4
    if board[22] != EMPTY and board[22] == board[23] == board[24] == board[25] == piece:
        print("You win!")
        return True
    if board[23] != EMPTY and board[23] == board[24] == board[25] == board[26] == piece:
        print("You win!")
        return True
    if board[24] != EMPTY and board[24] == board[25] == board[26] == board[27] == piece:
        print("You win!")
        return True
    if board[25] != EMPTY and board[25] == board[26] == board[27] == board[28] == piece:
        print("You win!")
        return True
    #Row 5
    if board[29] != EMPTY and board[29] == board[30] == board[31] == board[32] == piece:
        print("You win!")
        return True
    if board[30] != EMPTY and board[30] == board[32] == board[33] == board[7] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[5] == board[6] == board[7] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[5] == board[6] == board[7] == piece:
        print("You win!")
        return True
    #Row 6
    if board[36] != EMPTY and board[36] == board[37] == board[38] == board[39] == piece:
        print("You win!")
        return True
    if board[37] != EMPTY and board[37] == board[38] == board[39] == board[40] == piece:
        print("You win!")
        return True
    if board[38] != EMPTY and board[38] == board[39] == board[40] == board[41] == piece:
        print("You win!")
        return True
    if board[39] != EMPTY and board[39] == board[40] == board[41] == board[42] == piece:
        print("You win!")
        return True
    
    #All Diagonal Wins facing right
    if board[1] != EMPTY and board[1] == board[9] == board[17] == board[25] == piece:
        print("You win!")
        return True
    if board[8] != EMPTY and board[8] == board[16] == board[24] == board[32] == piece:
        print("You win!")
        return True
    if board[15] != EMPTY and board[15] == board[23] == board[31] == board[39] == piece:
        print("You win!")
        return True
    if board[9] != EMPTY and board[9] == board[17] == board[25] == board[33] == piece:
        print("You win!")
        return True
    if board[17] != EMPTY and board[17] == board[25] == board[33] == board[41] == piece:
        print("You win!")
        return True
    if board[16] != EMPTY and board[16] == board[24] == board[32] == board[40] == piece:
        print("You win!")
        return True
    if board[2] != EMPTY and board[2] == board[10] == board[18] == board[26] == piece:
        print("You win!")
        return True
    if board[10] != EMPTY and board[10] == board[18] == board[26] == board[34] == piece:
        print("You win!")
        return True
    if board[18] != EMPTY and board[18] == board[26] == board[34] == board[42] == piece:
        print("You win!")
        return True
    if board[3] != EMPTY and board[3] == board[11] == board[19] == board[27] == piece:
        print("You win!")
        return True
    if board[11] != EMPTY and board[11] == board[19] == board[27] == board[35] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[12] == board[20] == board[28] == piece:
        print("You win!")
        return True
    #All diagonal wins facing left
    if board[7] != EMPTY and board[7] == board[13] == board[19] == board[25] == piece:
        print("You win!")
        return True
    if board[13] != EMPTY and board[13] == board[19] == board[25] == board[31] == piece:
        print("You win!")
        return True
    if board[19] != EMPTY and board[19] == board[25] == board[31] == board[37] == piece:
        print("You win!")
        return True
    if board[14] != EMPTY and board[14] == board[20] == board[26] == board[32] == piece:
        print("You win!")
        return True
    if board[20] != EMPTY and board[20] == board[26] == board[32] == board[38] == piece:
        print("You win!")
        return True
    if board[21] != EMPTY and board[21] == board[27] == board[33] == board[39] == piece:
        print("You win!")
        return True
    if board[6] != EMPTY and board[6] == board[12] == board[18] == board[24] == piece:
        print("You win!")
        return True
    if board[12] != EMPTY and board[12] == board[18] == board[24] == board[30] == piece:
        print("You win!")
        return True
    if board[18] != EMPTY and board[18] == board[24] == board[30] == board[36] == piece:
        print("You win!")
        return True
    if board[5] != EMPTY and board[5] == board[11] == board[17] == board[23] == piece:
        print("You win!")
        return True
    if board[11] != EMPTY and board[11] == board[17] == board[23] == board[29] == piece:
        print("You win!")
        return True
    if board[4] != EMPTY and board[4] == board[10] == board[16] == board[22] == piece:
        print("You win!")
        return True
    return False


def is_valid_input(player_move: str) -> bool:
    
    if (len(player_move) != 1):
        print("Not a valid input. Try again")
        return False

    if player_move not in "1234567":
        print("Not a valid input. Try again")
        return False
    
    
    
    index = int(player_move)
    while index < 43:
        if board[index] != EMPTY:
            index += 7
        else:
            return True

    print("No slots avalabile in this column.")        
    

    return False


EMPTY = " "
X = "X"
O = "O"

current_player = X

board = [EMPTY] * 43
display_intro()

moves_made = 0 

retry = "y"

result_of_winner = False

while retry.startswith("y"):

    board = [EMPTY] * 43
    result_of_winner = False


    while result_of_winner == False and moves_made < 43:

        display_board(board)

        move = get_player_move()

        make_player_move(board, move, current_player)

        moves_made += 1


        result_of_winner = is_winner(board, current_player)

        if current_player == X:
            current_player = O
        else:
            current_player = X

    print("Would you like to play again?")
    retry = input().lower()
    print("Ok cya next time!")









