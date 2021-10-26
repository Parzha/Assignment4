
import random
from time import*
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# turns malom mikone alan nobate kie ke bazi kone
turns = 0
time_played_ai=0
time_played_player=0


# ye board misazim khali albate
global board
board = [[" " for x in range(3)] for y in range(3)]


# condition haie barande shodan
def winning_cond(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))


# greftan info bad az click kardan roie button and vared kardane on be board

def get_text(i, j, gb, l1, l2):

    global turns,time_played_player
    if board[i][j] == ' ':
        if turns % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        turns += 1

        if board[i][j] == 'X':
          button[i][j].config(text=board[i][j])
          button[i][j].config(fg='blue')
        elif board[i][j] == 'O':
          button[i][j].config(text=board[i][j])
          button[i][j].config(fg='red')


    if winning_cond(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", f'player 1 won the match')
    elif winning_cond(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", f'player 2 won the match')
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("DRAW", f'its draw..time played')



def isfree(i, j):
    return board[i][j] == " "



def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


# baraie sakhtam GUI

def gameboard_pl(game_board, l1, l2):

    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()



# AI next move
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winning_cond(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]



def get_text_pc(i, j, gb, l1, l2):
    global turns
    if board[i][j] == ' ':
        if turns % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        turns += 1

        button[i][j].config(text=board[i][j])
        button[i][j].config(fg='blue')

    x = True
    if winning_cond(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", f'player won the match' )
    elif winning_cond(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", f'Computer won the match')
    elif (isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Draw", f'its draw')
    if (x):
        if turns % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)



def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)

    game_board.mainloop()


# intial kardan board and karaie avaliash baraie AI-player albate
def withpc(game_board):

    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)



# intial kardane board va karaie avalie baraie bazi ba player

def withplayer(game_board):

    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")


    l1 = Button(game_board, text="Player 1 : X", width=10)

    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)



def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")

    command_pc = partial(withpc, menu)

    command_player = partial(withplayer, menu)


    head = Button(menu, text="---Welcome to tic-tac-toe---",
                  activeforeground='red',
                  activebackground="white", bg="gray",
                  fg="yellow", width=500, font='summer', bd=5)

    First_button = Button(menu, text="Single Player", command=command_pc,
                activeforeground='red',
                activebackground="yellow", bg="blue",
                fg="yellow", width=500, font='summer', bd=5)

    Second_button = Button(menu, text="Multi Player", command=command_player, activeforeground='red',
                activebackground="yellow", bg="green", fg="yellow",
                width=500, font='summer', bd=5)

    third_button = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="yellow",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    First_button.pack(side='top')
    Second_button.pack(side='top')
    third_button.pack(side='top')

    menu.mainloop()



if __name__ == '__main__':
    play()
