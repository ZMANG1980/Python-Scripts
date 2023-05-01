#the | sign is the pipe-> will see this again
artBoard='''
    |   |   
-------------
    |   |
-------------
    |   |
'''

gameBoard=[["1 ","2 ","3 "],[" 4","5 ","6 "],["7 ","8 ","9 "]]
#board=[[row1],[[row2]],[[row3]]
#print(board)
#print(board[0])
#print(board[1])
#print(board[2])
def printBoard(board):
    for row in range (len(board)):
        for col in range( len(board[0])):
            if col!=2:
                print(board[row][col],end="|")
            else:
                print(board[row][col])
        if row!=2:
            print("-"*6)
        else:
            print("\n"*2) #\n is a new line
printBoard(gameBoard)

symbol="x"
While (symbol!="Q"):
    #printBoard
printBoard(gameBoard)
    #player() x pr o) goes
     #check to see if the spot is taken
     #check for a winner
     symbol="x"

print("Winner is;")
