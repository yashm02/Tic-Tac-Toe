
import os

def display_board(board):
    os.system("cls")
    print(vert1+hori1+board[1]+hori1+hori2+hori1+board[2]+hori1+hori2+hori1+board[3]+hori1)
    print(vert2+vert1+hori1+board[4]+hori1+hori2+hori1+board[5]+hori1+hori2+hori1+board[6]+hori1)
    print(vert2+vert1+hori1+board[7]+hori1+hori2+hori1+board[8]+hori1+hori2+hori1+board[9]+hori1)
    print(vert1)


def player_input():
    mark=""
    while mark!="X" and mark!="O":
        mark=input("Player 1: Choose X or O: ").upper()
        if mark!="X" and mark!="O":
            print("Invalid input")
        
    if mark=="X":
        print("Player 1 will go first")
        turn="Player 1"
        return 'X','O',turn
    elif mark=="O":
        print("Player 2 will go first")
        turn ="Player 2"
        return 'O','X',turn
    
    
def choose_index(board):
    index=0
    while index not in indexes or not space_check(board,index):
        index=int(input("Pick the index where you want to insert (1-9): "))
        if index not in indexes:
            print("Sorry, Invalid choice")

    return index
    

def replace(board,index,mark):
    board[index]=mark
        
def space_check(board,index):
    return board[index]==" "

def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True


def check_win(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[3]==mark and board[5]==mark and board[7]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark))


def replay():
    choice=input("Do you want to play again? Enter Y or N: ")
    return choice == "Y"


print("WELCOME TO TIC-TAC-TOE")
while True:
    indexes=[1,2,3,4,5,6,7,8,9]    
    board=[' ']*10
    hori1="\t"
    hori2="|"
    vert1="\t\t|\t\t|\t\t\n"
    vert2="________________|_______________|_______________\n"
    player1_marker,player2_marker,turn=player_input()
    per=""
    while not (per=="Y" or per=="N"):
        per=input("Ready to play? Y or N?: ").upper()
        if per!='Y' and per!='N':
            print("Sorry, Invalid choice")
    if per=="Y":
        gameon = True
    else:
        gameon = False
    
    while gameon:
        if turn=="Player 1":
            display_board(board)
            chosen_index=choose_index(board)
            print(player1_marker)
            replace(board,chosen_index,player1_marker)
            if check_win(board,player1_marker):
                display_board(board)
                print("Congratulations, Player 1 has won")
                gameon=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE")
                    break
                else:
                    turn = "Player 2"
        else:
            display_board(board)
            chosen_index=choose_index(board)
            replace(board,chosen_index,player2_marker)
            if check_win(board,player2_marker):
                display_board(board)
                print("Congratulations, Player 2 has won")
                gameon=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE")
                    gameon=False
                else:
                    turn ="Player 1"
    if not replay():
        break

