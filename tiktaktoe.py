                #Importando as bibliotecas RANDOM e OS 
import random   #-RANDOM gera opções randomicamente a partir de um range ou uma lista 
import os       #-OS possibilita o uso de comandos de terminal, possibiliando interação com o S.O.


def logo():     #Função para exibir a logomarca do jogo
    print("")
    print("           _____________________________________________________________________")
    print("WELCOME TO ___________ ___ _____________________________________________________")
    print("_____________/__   __//  //  ___/_______________________________________________")
    print("_______________/  /  /  //  /___________________________________________________")
    print("______________/  /  /  //  /________ ________   ________________________________")
    print("_____________/  /  /  //  //__   __//  ___   |/  ___/___________________________")
    print("____________/__/  /__/ |____//  /  /  /__/  //  /_______________________________")
    print("____________________________/  /  /  ___   //  /________________________________")
    print("___________________________/  /  /  /  /  //  /_________________________________")
    print("____________________ _____/__/ _/__/_ /__/ |_____/______________________________")
    print("___________/__   __//  ___   |/  ___/___________________________________________")
    print("_____________/  /  /  /  /  //  /_ _____________________________________________")
    print("____________/  /  /  /  /  //  __/______________________________________________")
    print("___________/  /  /  /__/  //  /_________________________________________________")
    print("__________/__/   |_______/ |_____/______________________________________________")
    print("________________________________________________________by RichardGLara (2024)__")
    print("")

logo()  #Chamando a função da logomarca

        #Enquanto a logomarca é exibida e o jogo pede os nomes dos jogadores 
player1 = input(f"\n\bPlayer 1 name\n\t:")  #Espera entrada do nome do jogador1
player2 = input(f"\n\bPlayer 2 name\n\t:")  #Espera entrada do nome do jogador2


def print_board(board):
        #Função para exibir o tabuleiro do jogo e o tabuleiro guia.
        #O tabuleiro começa limpo e vai sendo preenchido com o decorer do jogo.
        #A guia ajuda a identificar as posições a serem escolhidas.

    print("")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}                   1 2 3")
    print("------------------                4 5 6")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}                   7 8 9")
    print("------------------")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("")



def choose_marker():
        #Função para possibilitar que o jogado 1 escolha se quer
        #jogar com X ou com O 
    
    marker = ""                                 #A variavel MARKER começa vazia
    while not (marker == "X" or marker == "O"): #Enquando MARKER NÃO é X ou O
                                                # será exibido a mensagem "do you want to be X or O?"
        marker = input(f"{player1.title()}, do you want to be X or O? ").upper()

    if marker == "X":                           #Se a escolha for X
        return ("X", "O" )                      #MARKER será setado como ("X", "0")
    else:                                       #Se não,
        return ("O", "X")                       #MARKER será setado como ("O", "X")



def mark_position(board, marker, position):

    board[position] = marker


def check_victory(board, marker):
        #Função com a lista com as vitórias possiveis
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker) or
        # 1, 2 e 3 com a mesma marcação
        (board[4] == marker and board[5] == marker and board[6] == marker) or   
        # 4, 5 e 6 com a mesma marcação
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        # 7, 8 e 9 com a mesma marcação
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        # 1, 4 e 7 com a mesma marcação
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        # 2, 5 e 8 com a mesma marcação
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        # 3, 6 e 9 com a mesma marcação
        (board[1] == marker and board[5] == marker and board[9] == marker) or
        # 1, 5 e 9 com a mesma marcação
        (board[7] == marker and board[5] == marker and board[3] == marker)
        # 3, 5 e 7 com a mesma marcação
    )


def first_player():
        #Função de sorteio de quem iniciará a partida
    if random.randint(0, 1) == 0:   #Chama a biblioteca RANDOM, sorteando um dos itens listados, 1 ou 0
        return player1              #Se for 0, quem inicia o jogo será o jogador1
    else:                           #Se não
        return player2              #quem começa é o player2


def check_space(board, position):
        #Função que checa se a posição escolhida para a jogada está vazia
    return board[position] == " "   #Retornando a posição dentro do tabuleiro como 'vazia'


def check_tied(board):
        #Função para checar empate
    for i in range(1, 10):          #Para a posição de 1 a 9
        if check_space(board, i):   #Se a resposta do 'check_space' for " "
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

    board = [" "] * 10  #Lista das opções de jogadas dentro do tabuleiro
    player_1, player_2 = choose_marker() # 'player_1' e 'player_2' são diferentes de 'player1' e 'player2'
    turno_jogador = first_player()
    print(turno_jogador, "START!!!")
    status_jogo = True

    while status_jogo:

        if turno_jogador == player1 :
            os.system("cls" if os.name == 'nt' else "clear")
            print_board(board)
            posicao_jogada = choice_move(board, turno_jogador)
            mark_position(board, player_1, posicao_jogada)

            if check_victory(board, player_1):
                print_board(board)
                print(f"Congratulations {player1.upper()}, you won the match!!!")
                status_jogo = False
            else:
                if check_tied(board):
                    print_board(board)
                    print("The game TIED!!!")
                    break
                else:
                    turno_jogador = player2

        else:
            os.system("cls" if os.name == 'nt' else "clear")
            print_board(board)
            posicao_jogada = choice_move(board, turno_jogador)
            mark_position(board, player_2, posicao_jogada)

            if check_victory(board, player_2):
                print_board(board)
                print(f"Congratulations {player2.upper()}, you won the match!!!")
                status_jogo = False
            else:
                if check_tied(board):
                    print_board(board)
                    print("The game TIED!!!")
                    break
                else:
                    turno_jogador = player1

    if not replay():
        break