
import random
import os


def tied():     
    print("______________________ ___ ______ _____     ___ ___ ___  _______________________")
    print("_____________/__   __//  //  ___//  _  #   /  //  //  / ________________________")
    print("_______________/  /  /  //  /_  /  / |  | /  //  //  / _________________________")
    print("______________/  /  /  //  __/ /  /  /  //__//__//__/ __________________________")
    print("_____________/  /  /  //  /__ /  /__/  /___ ___ ___  ___________________________")
    print("____________/__/  /__/ |____//________//__//__//__/ ____________________________")


def win():     
    print("_______________   ___   ___  ___  ___   ___   ___ ___ ___  _____________________")
    print("____________|  | /   | /  / /  / /   | /  /  /  //  //  / ______________________")
    print("____________|  |/    |/  / /  / /    |/  /  /  //  //  / _______________________")
    print("____________|     /|    / /  / /  /|    /  /__//__//__/ ________________________")
    print("____________|    / |   / /  / /  / |   /  ___ ___ ___  _________________________")
    print("____________|___/  |__/ /__/ /__/  |__/  /__//__//__/ __________________________")


def logo():    
    print("")
    print("           _____________________________________________________________________")
    print("WELCOME TO ___________ ___ ______  _____________________________________________")
    print("_____________/__   __//  //  ___/ ______________________________________________")
    print("_______________/  /  /  //  /  _________________________________________________")
    print("______________/  /  /  //  /________ ________   _____  _________________________")
    print("_____________/  /  /  //  //__   __//  ___   |/  ___/ __________________________")
    print("____________/__/  /__/ |____//  /  /  /__/  //  / ______________________________")
    print("____________________________/  /  /  ___   //  / _______________________________")
    print("___________________________/  /  /  /  /  //  /___  ____________________________")
    print("____________________ _____/__/ _/__/_ /__/ |_____/ _____________________________")
    print("___________/__   __//  ___   |/  ___/ __________________________________________")
    print("_____________/  /  /  /  /  //  /_  ____________________________________________")
    print("____________/  /  /  /  /  //  __/ _____________________________________________")
    print("___________/  /  /  /__/  //  /___  ____________________________________________")
    print("__________/__/   |_______/ |_____/ _____________________________________________")
    print("________________________________________________________by RichardGLara (2024)__")
    print("")


logo()  


player1 = input(f"\n\bPlayer 1 name\n\t:") 
player2 = input(f"\n\bPlayer 2 name\n\t:") 


def print_board(board):
    print("")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}                   1 2 3")
    print("------------------                4 5 6")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}                   7 8 9")
    print("------------------")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("")


def choose_marker():
    marker = ""                                
    while not (marker == "X" or marker == "O"):
        marker = input(f"{player1.title()}, do you want to be X or O? ").upper()
    if marker == "X":
        return ("X", "O" )    
    else:                                 
        return ("O", "X") 


def mark_position(board, marker, position):
    board[position] = marker


def check_victory(board, marker):
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or   
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[1] == marker and board[5] == marker and board[9] == marker) or
        (board[7] == marker and board[5] == marker and board[3] == marker)
    )


def first_player():
    if random.randint(0, 1) == 0:
        return player1 
    else: 
        return player2


def check_space(board, position):
    return board[position] == " " 


def check_tied(board):
    for i in range(1, 10):
        if check_space(board, i):
            return False
    return True


def choice_move(board, player):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(board, int(position)):
        position = input(f"{player.title()} - Choose your move between 1-9: ")
    return int(position) 


def replay():
    return input('Do you want to play again? Yes or no? ').lower().startswith('y')


while True:
    os.system("cls" if os.name == 'nt' else "clear")
    logo()
    board = [" "] * 10 
    player_1, player_2 = choose_marker()
    shift_player = first_player()
    print(shift_player, "START!!!")
    game_status = True
    while game_status:
        if shift_player == player1 :
            os.system("cls" if os.name == 'nt' else "clear")
            print_board(board)
            played_position = choice_move(board, shift_player)
            mark_position(board, player_1, played_position)
            if check_victory(board, player_1):
                print_board(board)
                print(f"Congratulations {player1.upper()}, you won the match!!!")
                win()
                game_status = False
            else:
                if check_tied(board):
                    print_board(board)
                    tied()
                    break
                else:
                    shift_player = player2
        else:
            os.system("cls" if os.name == 'nt' else "clear")
            print_board(board)
            played_position = choice_move(board, shift_player)
            mark_position(board, player_2, played_position)

            if check_victory(board, player_2):
                print_board(board)
                print(f"Congratulations {player2.upper()}, you won the match!!!")
                win()
                game_status = False
            else:
                if check_tied(board):
                    print_board(board)
                    tied()
                    break
                else:
                    shift_player = player1
    if not replay():
        break