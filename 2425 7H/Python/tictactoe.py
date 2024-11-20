import random


def choose_random_move_from_list(board: list[str], move_list: list[int]) -> int:
    possible_moves = []

    for move in move_list:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) > 0:
        # python shortcut if possible_moves:
        return random.choice(possible_moves)

    return 0


def display_board(board: list[str]) -> None:
    print(f"\n{board[7]} | {board[8]} | {board[9]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[1]} | {board[2]} | {board[3]}\n")


def get_board_copy(board: list[str]) -> list[str]:
    board_copy = []
    for piece in board:
        board_copy.append(piece)
    return board_copy


def get_computer_move(board: list[str], comp_piece: str, player_piece: str) -> int:
    # can i win?
    for move in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, move):
            board_copy = make_move(board_copy, move, comp_piece)
            if is_winner(board_copy, comp_piece):
                return move

    # can the player win?
    for move in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, move):
            board_copy = make_move(board_copy, move, player_piece)
            if is_winner(board_copy, player_piece):
                return move

    # can I play in a corner?
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move > 0:
        return move

    # can I play in the center?
    if is_space_free(board, 5):
        return 5

    # can I play an edge?
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def get_player_move(board: list[str]) -> int:
    print("What is your next move? (1-9)")
    move = input()

    while not is_valid_move(board, move):
        print("What is your next move? (1-9)")
        move = input()

    return int(move)


def is_board_full(board: list[str]) -> bool:
    for space in board[1:]:
        if space == EMPTY:
            return False

    return True


def is_space_free(board: list[str], move: int) -> bool:
    return board[move] == EMPTY


def is_valid_move(board: list[str], player_input: str) -> bool:
    if len(player_input) != 1:
        print("Too many characters")
        return False

    if not player_input in "123456789":
        print("Move not in range")
        return False

    move = int(player_input)
    if not is_space_free(board, move):
        print("That space isn't free")
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

    if board[3] == board[5] == board[7] == piece:
        return True

    return False


def make_move(board: list[str], move: int, piece: str) -> list[str]:
    board[move] = piece
    return board


def who_goes_first() -> list[str]:
    if random.random() < 0.5:
        print("You can go first!")
        return [X, O]
    else:
        print("I'll go first.")
        return [O, X]


EMPTY = " "
X = "X"
O = "O"
play_again = "y"

print("Welcome to Tic-Tac-Toe")

while play_again.startswith("y"):
    is_game_over = False
    board = [EMPTY] * 10

    player_piece, computer_piece = who_goes_first()
    if player_piece == X:
        print("You can go first. It won't help you though.")
        current_player = "player"
        current_piece = player_piece
    else:
        print("I will go first. You don't stand a chance.")
        current_player = "computer"
        current_piece = computer_piece

    while not is_game_over:
        display_board(board)

        if current_player == "player":
            move = get_player_move(board)
        else:
            move = get_computer_move(board, computer_piece, player_piece)
            print("I'll play here.")

        board = make_move(board, move, current_piece)

        if is_winner(board, current_piece):
            is_game_over = True

        if is_board_full(board):
            print("Board is full")
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
        print("You didn't win this time. Maybe next time.")
    else:
        print("It's a tie.")

    print("Would you like to play again?")
    play_again = input().lower()
