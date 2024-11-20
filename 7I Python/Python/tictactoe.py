import random


def choose_move_from_list(board: list[str], move_list: list[int]) -> int:
    open_moves = []
    for move in move_list:
        if is_space_empty(board, move):
            open_moves.append(move)

    if open_moves:
        return random.choice(open_moves)

    return -1


def copy_board(board: list[str]) -> list[str]:
    board_copy = []
    for space in board:
        board_copy.append(space)

    return board_copy


def display_board(board: list[str]) -> None:
    print(
        f"""
{board[7]} | {board[8]} | {board[9]}
--+---+--
{board[4]} | {board[5]} | {board[6]}
--+---+--
{board[1]} | {board[2]} | {board[3]}
"""
    )


def display_intro() -> None:
    print("Welcome to Tic-Tac-Toe!")


def get_computer_move(board: list[str], own_piece: str, player_piece: str) -> int:
    # where can I win?
    for move in range(1, 10):
        if is_space_empty(board, move):
            board_copy = copy_board(board)
            board_copy = make_move(board_copy, move, own_piece)
            if is_winner(board_copy, own_piece):
                return move

    # where can my opponent win?
    for move in range(1, 10):
        if is_space_empty(board, move):
            board_copy = copy_board(board)
            board_copy = make_move(board_copy, move, player_piece)
            if is_winner(board_copy, player_piece):
                return move

    # can I move in a corner?
    move = choose_move_from_list(board, [1, 3, 7, 9])
    if move != -1:
        return move

    # can I move in the center?
    if is_space_empty(board, 5):
        return 5

    # can I move on an edge?
    move = choose_move_from_list(board, [2, 4, 6, 8])
    if move != -1:
        return move

    return -1

    # move = random.randint(1, 9)
    # while not is_space_empty(board, move):
    #     move = random.randint(1, 9)

    return move


def get_player_move(board: list[str]) -> int:
    print("What is your next move? (1-9)")
    move = input()

    while not is_valid_input(board, move):
        print("What is your next move? (1-9)")
        move = input()

    return int(move)


def get_player_order(x_piece: str, o_piece: str) -> list[str]:
    """
    Return a list of pieces where the first piece is the player piece
    and the second piece is the computer piece.
    """
    if random.random() < 0.5:
        return [x_piece, o_piece]
    return [o_piece, x_piece]


def is_board_full(board: list[str]) -> bool:
    for space in board[1:]:
        if space == EMPTY:
            return False

    return True


def is_space_empty(board: list[str], move: int) -> bool:
    return board[move] == EMPTY


def is_valid_input(board: list[str], player_input: str) -> bool:
    if len(player_input) != 1:
        print("Too many characters")
        return False

    if not player_input in "123456789":
        print("Not a number")
        return False

    move = int(player_input)
    if not is_space_empty(board, move):
        print("That space isn't empty")
        return False

    return True


def is_winner(board: list[str], piece: str) -> bool:
    if board[1] == board[2] == board[3] == piece:
        return True

    if board[4] == board[5] == board[6] == piece:
        return True

    if board[7] == board[8] == board[9] == piece:
        return True

    if board[1] == board[4] == board[7] == piece:
        return True

    if board[2] == board[5] == board[8] == piece:
        return True

    if board[3] == board[6] == board[9] == piece:
        return True

    if board[1] == board[5] == board[9] == piece:
        return True

    if board[7] == board[5] == board[3] == piece:
        return True

    return False


def make_move(board: list[str], move: int, piece: str) -> list[str]:
    board[move] = piece
    return board


EMPTY = " "
X = "X"
O = "O"
play_again = "y"

display_intro()

while play_again.startswith("y"):
    board = [EMPTY] * 10

    player_piece, computer_piece = get_player_order(X, O)

    if player_piece == X:
        current_player = "player"
        current_piece = player_piece
    else:
        current_player = "computer"
        current_piece = computer_piece
    is_game_over = False

    while not is_game_over:
        display_board(board)
        if current_player == "player":
            move = get_player_move(board)
        else:
            move = get_computer_move(board, computer_piece, player_piece)
            print(f"{move = }")

        board = make_move(board, move, current_piece)

        if is_winner(board, current_piece):
            is_game_over = True

        if is_board_full(board):
            is_game_over = True

        if not is_game_over:
            if current_player == "player":
                current_player = "computer"
                current_piece = computer_piece
            else:
                current_player = "player"
                current_piece = player_piece

    display_board(board)

    if is_winner(board, player_piece):
        print("You win! But it won't happen again.")
    elif is_winner(board, computer_piece):
        print("I win. Better luck next time.")
    else:
        print("It's a tie.")

    print("Would you like to play again?")
    play_again = input().lower()
