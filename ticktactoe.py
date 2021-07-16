#! python3
# tictactoe.py - commandline Tic Tac Toe game

import pyinputplus as pyip

board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9, ]

players = ['X', 'O']
currentPlayer = 'X'

winPossibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                    [1, 4, 7], [2, 5, 8], [3, 6, 9],
                    [1, 5, 9], [3, 5, 7]]

count = 0


def win(plr):
    for i in range(0, 8):
        if board[winPossibilities[i][0] - 1] == plr and board[winPossibilities[i][1] - 1] == plr and board[winPossibilities[i][2] - 1] == plr:
            print('*******************')
            print(f'** Winner is: {plr}! **')
            print('*******************')
            return True
    return False


def is_valid(plr):
    while True:
        place = pyip.inputNum(min=1, max=9)
        if isinstance(board[place - 1], int):
            board[place - 1] = plr
            return True
        else:
            print('This place is already taken')
            return False


def print_board():
    print('----+---+----')
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i + 1], '|', board[i + 2], '|')
        print('----+---+----')


print_board()

while count < 5 or not win(currentPlayer):
    if currentPlayer == 'X':
        currentPlayer = 'O'
    elif currentPlayer == 'O':
        currentPlayer = 'X'
    print(f'Move:{currentPlayer}')

    if is_valid(currentPlayer):
        count += 1
    print_board()

    if count == 10:
        print('That is a draw')
        break
