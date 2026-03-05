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
    win = False
    #draw
    if not (board == 0).any() and win == False:
        return "Draw"
    #win

    

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
            currentPlayersTurn = 2
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                print("Game is a draw")
                break
        else:
            print("You cannot move here, please try again")
    elif currentPlayersTurn == 2:
        if ifDecider:
            board[row][playerInput-1] = "2"
            currentPlayersTurn = 1
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                print("Game is a draw")
                break
        else:
            print("You cannot move here, please try again")
