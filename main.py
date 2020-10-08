# ----- Global Variables -------------

#Game Board
board = ["-"]*9

#if game is going on
game_still_going = True

winner = None

current_player = 'X'


def Display_board():
    print(board[0]+  "|" + board[1] + "|" + board[2])
    print(board[3]+  "|"  + board[4] + "|" + board[5])
    print(board[6]+  "|"  + board[7] + "|" + board[8])

def play_game():
    # Display initial board
    Display_board()
    
    while game_still_going:
        #handle a single turn of arbitary player

        Handle_turn(current_player)

        #check if the game as ended

        check_if_game_over()

        #flip to the other player

        flip_player()
#Game has ended
    if winner == 'X' or winner == 'O':
       print(winner + " " + "Won")
    elif winner == None:
        print("Tie")





def check_if_game_over():
    check_for_winner()
    check_if_tie()
   

def check_for_winner():

    global winner

    #check rows
    row_winner = check_rows()
    #check diagonals
    dia_winner = check_diagonals()
    #check columns
    col_winner = check_columns()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

def check_diagonals():
    global game_still_going
    dia_1 = board[0] == board[4] == board[8] !=  "-"
    dia_2 = board[2] == board[4] == board[6] !=  "-"

    if dia_1 or dia_2:
        game_still_going = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return
   
  
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return




def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

def Handle_turn(player):
    print(player + "turn")
    position = int(input("choose a position from 1-9: "))
    # while position not in ["1","2","3","4","5","6","7","8","9"]:
    #     position = int(input("Invalid Input: choose a position from 1-9: "))
    position -= 1
    board[position] = player
    Display_board()


play_game()








# display board
# play game
# handle turn
#check win
 #check rows
 #check columns
 #check diagonals
#check tie
#flip moves

