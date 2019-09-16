#tic tac toe

import random

def printBoard(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print('   |   |')

def inputPlayerLetter():
    #get player letter
    letter=''
    while not(letter=='X' or letter=='O'):
        print("Choose X or O")
        letter=input().upper()

    #return player letter(first) and computer letter(second)
    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']

def firstPlayer():
    #randomly choose
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #if input is Y or y return true else false
    print("Do you want to play again (yes or no)")
    return input().lower().startswith('y')
    
def getPlayerMove(board):
    move=''

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('what is your next move? (1-9)')
        move=input()
    return int(move)

def isSpaceFree(board,space):
    return board[space]==' ' 

def isBoardFull(board):
    return not ' ' in board

def makeMove(board,letter,space):
    board[space]=letter

#theBoard=[' ']*10
#theBoard=['1','2','3','4','5','6','7','8','9','10']
print()

print('Welcome to Tic Tac Toe!!')

while True:
    theBoard=[' ']*10
    #theBoard=['1','2','3','4','5','6','7','8','9','10']
    playerLetter,computerLetter=inputPlayerLetter()
    turn=firstPlayer()
    print('The ' + turn + ' will go first')

    if turn=='player':
        print('player!!!')
        printBoard(theBoard)

        while True:
            move=getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)
            printBoard(theBoard)

    elif turn=='computer':
        print('computer!!!')
        printBoard(theBoard)
        
    if not playAgain():
        break

