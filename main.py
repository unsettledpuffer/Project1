#Connect4Learn

import numpy as np

#errorchecks
def typeCheck():
    while True:
        try:
            playerMove = int(input("Which column would you like to drop in?"))
            return playerMove
        except ValueError:
            print("Invalid character entered")

#generation

def createBoard():
    return np.zeros((6,7),dtype=int)

board = createBoard()

def displayBoard():
    print(board)

def clearConsole():
    for x in range(10):
        print(" ")
#player 1 yellow
#player 2 red

def getPlayerMove():
    playerMove = typeCheck()
    while playerMove > 7 or playerMove < 1:
        print("That is not a column. Re enter")
        playerMove = typeCheck()
    return playerMove

def getColumnLowestSlot(playerInput):
    for row in range(5,-1,-1):
        if board[row][playerInput-1] == 0:
            return True,row,playerInput
        else:
            pass
    return False, 0, 0

#wincheck
def winCheck(currentPlayersTurn):
    #draw
    if not (board == 0).any() and win == False:
        return "Draw"
    #horizontalwin
    for row in range(len(board)):
        for column in range(4):
            if (board[row][column] == 1 and board[row][column+1] == 1 and board[row][column+2] == 1 and board[row][column+3] == 1) or (board[row][column] == 2 and board[row][column+1] == 2 and board[row][column+2] == 2 and board[row][column+3] == 2):
                return "Win"
    #verticalwin
    for row in range(3):
        for column in range(len(board)):
            if (board[row][column] == 1 and board[row+1][column] == 1 and board[row+2][column] == 1 and board[row+3][column] == 1) or (board[row][column] == 2 and board[row+1][column] == 2 and board[row+2][column] == 2 and board[row+3][column] == 2): 
                return "Win"
    #diagonalwindown
    for row in range(3):
        for column in range(4):
            if (board[row][column] == 1 and board[row+1][column+1] == 1 and board[row+2][column+2] == 1 and board[row+3][column+3] == 1) or (board[row][column] == 2 and board[row+1][column+1] == 2 and board[row+2][column+2] == 2 and board[row+3][column+3] == 2): 
                return "Win"
    #diagonalwinup
    for row in range(3,6):
        for column in range(4):
            if (board[row][column] == 1 and board[row+-1][column+1] == 1 and board[row-2][column+2] == 1 and board[row-3][column+3] == 1) or (board[row][column] == 2 and board[row-1][column+1] == 2 and board[row-2][column+2] == 2 and board[row-3][column+3] == 2):
                return "Win"
#main
gameIsNotWon = True
currentPlayersTurn = 1
clearConsole()
displayBoard()
while gameIsNotWon:
    print("It is currently the turn of player",currentPlayersTurn)

    ifDecider, row, playerInput = getColumnLowestSlot(getPlayerMove())

    if currentPlayersTurn == 1:
        if ifDecider:
            board[row][playerInput-1] = "1"
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                print("Game is a draw")
                break
            if winCheck(currentPlayersTurn) == "Win":
                print("Player",currentPlayersTurn, "Wins")
                break
            currentPlayersTurn = 2
        else:
            print("You cannot move here, please try again")
    elif currentPlayersTurn == 2:
        if ifDecider:
            board[row][playerInput-1] = "2"
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                print("Game is a draw")
                break
            if winCheck(currentPlayersTurn) == "Win":
                print("Player",currentPlayersTurn, "Wins")
                break
            currentPlayersTurn = 1
        else:
            print("You cannot move here, please try again")
