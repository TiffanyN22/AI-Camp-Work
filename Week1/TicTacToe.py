import pandas as pd

d = {'col1': ["_","_","_"],'col2': ["_","_","_"], 'col3': ["_","_","_"]}
board = pd.DataFrame(data=d)
print(board)
print(board.iat[0,2])

def clearBoard(board):
    for i in range(3):
        for j in range(3):
            board.iat[i,j] = "_"

#column_pos = eval(input("Enter column: "))
#row_pos = eval(input("Enter row: "))
#board.iat[row_pos,column_pos] = "x"

def checkWin(board):
    #vertical checks
    if (board.iat[0,0] == board.iat[0,1] and board.iat[0,1] == board.iat[0,2] and board.iat[0,0]!= "_"):
        return True
    elif (board.iat[1,0] == board.iat[1,1] and board.iat[1,1] == board.iat[1,2] and board.iat[1,0]!= "_"):
        return True
    elif (board.iat[2,0] == board.iat[2,1] and board.iat[2,1] == board.iat[2,2] and board.iat[2,0]!= "_"):
        return True
    #diagonal checks
    elif (board.iat[0,0] == board.iat[1,1] and board.iat[1,1] == board.iat[2,2] and board.iat[0,0]!= "_"):
        return True
    elif (board.iat[2,0] == board.iat[1,1] and board.iat[1,1] == board.iat[0,2] and board.iat[2,0]!= "_"):
        return True
    #horizontal checks
    elif(board.iat[0,0] == board.iat[1,0] and board.iat[1,0]==board.iat[2,0] and board.iat[0,0]!= "_"):
        return True
    elif(board.iat[0,1] == board.iat[1,1] and board.iat[1,1]==board.iat[2,1] and board.iat[0,1]!= "_"):
        return True
    elif(board.iat[0,2] == board.iat[1,2] and board.iat[1,2]==board.iat[2,2] and board.iat[0,2]!= "_"):
        return True
    else:
        return False

clearBoard(board)
i = 0
print(board)
while(not checkWin(board) and i != 10):
    column_pos = eval(input("Enter column: "))
    row_pos = eval(input("Enter row: "))
    
    if (i%2 == 0):
        board.iat[row_pos,column_pos] = "X"
    else:
        board.iat[row_pos,column_pos] = "O"
    print(board)
    i+=1
    
print("game has ended")
if(i == 10):
    print("There was a tie!")
elif((i-1)%2 == 0):
    print("Player X won the game!")
else:
    print("Player O won the game!")
