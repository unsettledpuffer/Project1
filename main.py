#Connect4Learn

import numpy as np
import random
import os 

if os.path.exists("connect4.npz"):
    data = np.load("connect4.npz", allow_pickle=True)
    weights=data["weights"]
    bias=data["bias"]
    outputWeights=data["outputWeights"]
    outputBias=data["outputBias"]
else:
    pass


explorationRate = 0.1
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
#player 2 AI

def getPlayerMove():
    playerMove = typeCheck()
    while playerMove > 7 or playerMove < 1:
        print("That is not a column. Re enter")
        playerMove = typeCheck()
    return playerMove

def getAIMove():
    global inputLayer, weights, bias, hiddenLayer, outputWeights, outputBias, outputLayer, memoryBoards, memoryMoves

    inputLayer = flattenBoard()

    for x in range(len(hiddenLayer)):
        calculation = 0
        for y in range(len(inputLayer)):
            result = inputLayer[y] * weights[x][y]
            calculation += result
        calculation += bias[x]
        hiddenLayer[x] = calculation


    for x in range(7):
        calculation = 0
        for y in range(len(hiddenLayer)):
            result = hiddenLayer[y] * outputWeights[x][y]
            calculation += result
        calculation += outputBias[x]
        outputLayer[x] = calculation

    if random.random() > explorationRate:
        columnChoice = random.randint(0,6)
    else:
        columnChoice = outputLayer.index(max(outputLayer))
    memoryBoards.append(inputLayer.copy())
    memoryMoves.append(columnChoice)
    return columnChoice

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
    if not (board == 0).any():
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

#AIlogic
def flattenBoard():
    flattenedBoard = []
    for row in board:
        for item in row:
            if item == 0:
                flattenedBoard.append(0)
            elif item == 1:
                flattenedBoard.append(1)
            elif item == 2:
                flattenedBoard.append(2)
    return np.array(flattenedBoard)

#math

inputLayer = flattenBoard()
hiddenLayer = [0] * 20
weights =  []
for x in range(len(hiddenLayer)):
    nodesList = [random.uniform(-0.01,0.01) for y in range(len(inputLayer))]
    weights.append(nodesList)
bias = [0] * 20

outputWeights = []
outputBias = [0] * 7
outputLayer = [0] * 7
for x in range(7):
    nodesList = [random.uniform(-0.01,0.01) for y in range(len(hiddenLayer))]
    outputWeights.append(nodesList)

#main
memoryBoards = []
memoryMoves = []
gameIsNotWon = True
currentPlayersTurn = 1
clearConsole()
displayBoard()
status = "null"
reward = 0
while gameIsNotWon:
    print("It is currently the turn of player",currentPlayersTurn)

    if currentPlayersTurn == 1:
        ifDecider, row, playerInput = getColumnLowestSlot(getPlayerMove())
        if ifDecider:
            board[row][playerInput-1] = "1"
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                print("Game is a draw")
                status = "draw"
                break
            if winCheck(currentPlayersTurn) == "Win":
                print("Player",currentPlayersTurn, "Wins")
                status = "1wins"
                break
            currentPlayersTurn = 2
        else:
            print("You cannot move here, please try again")
    elif currentPlayersTurn == 2:
        ifDecider, row, playerInput = getColumnLowestSlot(getAIMove())
        if ifDecider:
            board[row][playerInput] = "2"
            clearConsole()
            displayBoard()
            if winCheck(currentPlayersTurn) == "Draw":
                status = "draw"
                print("Game is a draw")
                break
            if winCheck(currentPlayersTurn) == "Win":
                print("Player",currentPlayersTurn, "Wins")
                status = "2wins"
                break
            currentPlayersTurn = 1
        else:
            print("You cannot move here, please try again")

if status == "1wins":
    reward = -1
elif status == "2wins":
    reward = 1
else:
    reward = 0 
learningRate = 0.01
def learnFromGame():
    for x in range(len(memoryMoves)):
        boardState = memoryBoards[x]
        move = memoryMoves[x]
        for y in range(len(hiddenLayer)):
            calculation = 0
            for i in range(len(boardState)):
                result = boardState[i] * weights[y][i]
                calculation += result
            calculation += bias[y]
            hiddenLayer[y] = calculation
    for h in range(len(hiddenLayer)):
        outputWeights[move][h] += learningRate * reward * hiddenLayer[h]
    outputBias[move] += learningRate * reward
learnFromGame()
np.savez(
    "connect4.npz",
    weights=weights,
    bias=bias,
    outputWeights=outputWeights,
    outputBias=outputBias
)