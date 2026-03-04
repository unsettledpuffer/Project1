#Connect4Learn

import numpy as np

def createBoard():
    return np.zeros((6,7),dtype=int)

board = createBoard()

def displayBoard():
    print(board)


#player 1 yellow
#player 2 red

def getPlayerMove():
    playerMove = int(input("Which column would you like to drop in?"))
    return playerMove


def getColumnLowestSlot(playerInput):
    for row in range(5,-1,-1):
        if board[row][playerInput-1] == 0:
            return True,row,playerInput
        else:
            pass
    return False, 0, 0

displayBoard()

gameIsNotWon = True
currentPlayersTurn = "one"
while gameIsNotWon:

    ifDecider, row, playerInput = getColumnLowestSlot(getPlayerMove())

    if currentPlayersTurn.lower() == "one":
        if ifDecider:
            board[row][playerInput-1] = "1"
            currentPlayersTurn = "two"
            displayBoard()
        else:
            print("You cannot move here, please try again")
    elif currentPlayersTurn.lower() == "two":
        if ifDecider:
            board[row][playerInput-1] = "2"
            currentPlayersTurn = "one"
            displayBoard()
        else:
            print("You cannot move here, please try again")
