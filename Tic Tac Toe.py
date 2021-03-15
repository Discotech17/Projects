#Tic Tac Toe game in Python

import random

def drawBoard(board):
    # Print the board in order.
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Lets the player choose X or O.
    # Returns a list with the player's letter as the first item and the computer's as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # First element in the list is players; second is the computer.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose who goes first
    if random.randint (0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given the board and player letter, true if player wins.
    # bo instead of board le instead of letter.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
    # Make a copy list and return
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Free space? move there
    return board[move] == ' '

def getPlayerMove(board):
    # Enter player move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print('What is your next move?')
            move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move.
    # Returns none if no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    #Given a board, determine where to move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move!= None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        return True

print('Welcome to Tic-Tac-Toe!')

while True:
    #Resets the board
    board = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board, playerLetter, move)

            if isWinner(board, playerLetter):
                drawBoard(board)
                print('Hooray! You have won!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('The game is a tie.')
                    gameIsPlaying = False
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)

            if isWinner(board, computerLetter):
                drawBoard(board)
                print('The computer has beaten you!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('The game is a tie.')
                    gameIsPlaying = False
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
