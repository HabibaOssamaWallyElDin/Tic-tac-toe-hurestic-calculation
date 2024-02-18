PlayBoard ={1: ' ' ,   2: ' ' ,   3: ' ' ,
            4: ' ' ,   5: ' ' ,   6: ' ' ,
            7: ' ' ,   8: ' ' ,   9: ' ' , }


def printPlayBoard(board):
    print(board[1] + '  |' + board[2]+ '  |' + board[3])     
    print ("-------------")     
    print(board[4] + '  |' + board[5]+ '  |' + board[6])     
    print ("-------------")  
    print(board[7] + '  |' + board[8]+ '  |' + board[9])   


    #check columns
def checkPlayBoardColumns(board):
    for x in range(1,4):
        if board[x]== board[x+3] and board[x+3] == board[x+6] and board[x] != ' ':
            return True
    return False

#check rows
def checkPlayBoardRows(board):
    for x in range(1,9,3):
        if board[x]== board[x+1] and board[x+1] == board[x+2] and board[x] != ' ':
            return True
    return False        

#check diagonals
def checkPlayBoardDiag(board):
        if (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
            return True
        if (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
         return True
        
        return False
#No winner 
def checkPlayBoard(board):
    for v in board.values():
        if (v==' '):
            return True 
    print(" NO WINNER")  
    return False

#hurestic calculation for x .
#Rows hurestic
def huresticCheck(board,letter):
    if letter=="O":
        Hur="X"
    else:
        Hur="O"
    hurestic=0   
    #Rows
    for x in range(1,9,3):
        if board[x]!=Hur and board[x+1]!=Hur and board[x+2]!=Hur :
            hurestic=hurestic+1
    #coloumns
    for x in range(1,4):
        if board[x]!=Hur and board[x+3]!=Hur  and board[x+6]!=Hur :
            hurestic=hurestic+1
    #Diagonals        
    if board[1]!=Hur  and board[5]!=Hur  and board[9]!=Hur :
        hurestic=hurestic+1
    if board[3]!=Hur  and board[5]!=Hur  and board[7]!=Hur :
        hurestic=hurestic+1        
    return hurestic

turn='X'
while  checkPlayBoard(PlayBoard):
    printPlayBoard(PlayBoard)
    print("it's your turn," +turn+" "+ "which place do you want ?")
    move=int (input())
    if move==0:
        print(" ---> Hurestic equal = " + str(huresticCheck(PlayBoard,"X") -huresticCheck(PlayBoard,"O")))
    else:
        if PlayBoard[move]==' ':
            PlayBoard[move]= turn
            if checkPlayBoardDiag(PlayBoard) or checkPlayBoardRows(PlayBoard) or checkPlayBoardColumns(PlayBoard):
                print("the winner is "+ turn )
                exit()
            
        else:
            print("**The place is not empty**\n   choose another one\n ")
            continue
        if turn=='X':
            turn='O'
        else:
            turn='X'
        










     