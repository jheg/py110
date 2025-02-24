import random 
import threading # to wait 3 seconds for play again response from user
import os # for clearing terminal each time board is displayed
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
PLAYER_ONE = "Player"
PLAYER_TWO = "Computer"
TARGET_SCORE = 1
ROUND_PAUSE = 1
PLAY_AGAIN_WAIT = 5
FIRST_MOVE = 'prompt'
WINNING_ROWS = [
        [1,2,3], [4,5,6], [7,8,9],  # Rows
        [1,4,7], [2,5,8], [3,6,9],  # Columns
        [1,5,9], [3,5,7]            # Diagonals
    ]

def prompt(msg):
    print(f'==> {msg}')

def display_board(board):
    os.system('clear')
    prompt(f'First to {TARGET_SCORE}!')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |')
    print('')

def initialise_board():
    return {square: INITIAL_MARKER for square in range(1,10) }

def empty_squares(board):
    return [ key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(empty_squares, delimiter=",", word="or"):
    if not empty_squares:
        return []
    elif len(empty_squares) < 2:
        return empty_squares[0]
    else:
        return f"{(delimiter + " ").join(empty_squares[0:-2])}{delimiter} {empty_squares[-2]} {word} {empty_squares[-1]}"

def player_chooses_square(board):
    prompt('Players go:')
    while True:
        valid_squares = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square: {join_or(valid_squares)}')
        square = input().strip()
        if square in valid_squares:
            break

        prompt("Sorry that's not a valid choice, try again:")
    
    board[int(square)] = HUMAN_MARKER
    display_board(board)

def computers_turn(board):
    prompt('Computers go:')
    time.sleep(ROUND_PAUSE)
    attack_or_defend = False
    winning_square = []
    defend_square = []
    for winning_line in WINNING_ROWS:
        player1 = []
        player2 = []
        empty = []
        for square in winning_line:
            if board[square] == HUMAN_MARKER:
                player1.append(square)
            elif board[square] == COMPUTER_MARKER:
                player2.append(square)
            else:
                empty.append(square)
        if len(player2) == 2 and len(empty) == 1:
            winning_square.append(int(empty[0]))
        if len(player1) == 2 and len(empty) == 1:
            defend_square.append(int(empty[0]))

    if winning_square:
        board[winning_square[0]] = COMPUTER_MARKER
        attack_or_defend = True
    elif defend_square:
        board[defend_square[0]] = COMPUTER_MARKER
        attack_or_defend = True

    if attack_or_defend == False:
        board[random.choice(empty_squares(board))] = COMPUTER_MARKER

    display_board(board)
    time.sleep(ROUND_PAUSE)

def check_if_winner(board):
    winning_lines = [
        [1,2,3], [4,5,6], [7,8,9],  # Rows
        [1,4,7], [2,5,8], [3,6,9],  # Columns
        [1,5,9], [3,5,7]            # Diagonals
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (
            board[sq1] == HUMAN_MARKER and
            board[sq2] == HUMAN_MARKER and
            board[sq3] == HUMAN_MARKER
        ):
            return PLAYER_ONE
        elif (
            board[sq1] == COMPUTER_MARKER and
            board[sq2] == COMPUTER_MARKER and
            board[sq3] == COMPUTER_MARKER
        ):
            return PLAYER_TWO
        
    return None

def board_full(board):
    return len(empty_squares(board)) == 0

def check_end_of_game(board):
    if check_if_winner(board):
        return bool(check_if_winner(board))
    elif board_full(board):
        return bool(board_full(board))
    
scorebaord = {
	PLAYER_ONE: 0,
	PLAYER_TWO: 0,
}

def update_scoreboard(scoreboard, winner):
    scoreboard[winner] += 1

def display_scoreboard(scoreboard):
	prompt("Scoreboard")
	prompt(f"{PLAYER_ONE}: {scoreboard[PLAYER_ONE]}")
	prompt(f"{PLAYER_TWO}: {scoreboard[PLAYER_TWO]}")

def check_overall_winner():
    if scorebaord[PLAYER_ONE] == TARGET_SCORE:
        return PLAYER_ONE
    elif scorebaord[PLAYER_TWO] == TARGET_SCORE:
        return PLAYER_TWO
    else:
        return None

def want_to_play():
    response = [None]

    def get_input():
        response[0] = input("Do you want to play again? (Press any key to continue)")
        
    prompt(f"You have {PLAY_AGAIN_WAIT} seconds to press any key to play again")
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    input_thread.join(timeout=PLAY_AGAIN_WAIT)

    if response[0] is not None: 
        return True
    else:
        return False

def tictactoe():   
    board = initialise_board()
    display_board(board)
    if FIRST_MOVE == "prompt":
        while True:
            prompt('Choose who will take the first turn. 1 for player or 2 for computer')
            first_turn = input()
            if first_turn in ['1', '2']:
                break   
            prompt('That is not a valid response, please try again.')
    elif FIRST_MOVE == PLAYER_ONE:
        first_turn = '1'
    else:
        first_turn = '2'

    if first_turn == '1':
        while True:
            player_chooses_square(board)
            if check_end_of_game(board):
                break
            computers_turn(board)
            if check_end_of_game(board):
                break
            # display_board(board)
    elif first_turn == '2':
        while True:
            computers_turn(board)
            if check_end_of_game(board):
                break
            player_chooses_square(board)
            if check_end_of_game(board):
                break
            # display_board(board)
    
    if check_if_winner(board):
        update_scoreboard(scorebaord, check_if_winner(board))

        if check_overall_winner(): 
            prompt(f"{check_if_winner(board)} wins this round!")
            prompt(f"{check_overall_winner()} has won {TARGET_SCORE} and is the overall winner!")
            display_scoreboard(scorebaord)
            time.sleep(ROUND_PAUSE)
            if want_to_play():
                tictactoe()
            else: 
                prompt("...")
                prompt("See you next time!")
        else: 
            prompt(f"{check_if_winner(board)} wins this round!")
            display_scoreboard(scorebaord)
            time.sleep(ROUND_PAUSE)
            tictactoe()
    else: 
        prompt("It's a tie!")
        display_scoreboard(scorebaord)
        time.sleep(ROUND_PAUSE)
        tictactoe()

    

tictactoe()