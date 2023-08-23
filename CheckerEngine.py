class GameState:
    
    def __init__(self):
        # board 8x8 board 2D list with piece represented by 2 characters 
        self.board=[
            ['nw','--','nw','--','nw','--','nw','--'],
            ['--','nw','--','nw','--','nw','--','nw'],
            ['nw','--','nw','--','nw','--','nw','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','nb','--','nb','--','nb','--','nb'],
            ['nb','--','nb','--','nb','--','nb','--'],
            ['--','nb','--','nb','--','nb','--','nb']

        ] 
#             ['--','--','--','--','--','--','--','--'],
#             ['--','nw','--','--','--','--','--','--'],
#             ['--','--','nb','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','nw','--'],
#             ['--','--','--','--','--','--','--','nb']
            
        
#             ['nw','--','nw','--','nw','--','nw','--'],
#             ['--','nw','--','nw','--','nw','--','nw'],
#             ['nw','--','nw','--','nw','--','nw','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','nb','--','nb','--','nb','--','nb'],
#             ['nb','--','nb','--','nb','--','nb','--'],
#             ['--','nb','--','nb','--','nb','--','nb']
        
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','nw','--'],
#             ['--','--','--','--','--','--','--','nb']

#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','nw','--','--'],
#             ['--','--','--','--','--','--','--','--'],
#             ['--','--','--','--','--','--','--','nb']
        
        
        
        self.blackToMove = True
        self.moveLog = []
        
    def score(self):
        black=0
        white=0
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col][1]=='b':
                    black+=1
                if self.board[row][col][1]=='w' :
                    white+=1
        self.white_score = white
        self.black_score = black
        print("white:", self.white_score ,"black score" ,self.black_score)
    
    def checkMate(self):
        self.score()
        if self.black_score == 0 or self.white_score == 0:
            return True
        else:
            return False
           
    
    def makeMove(self , move):           # move is object of class Move
        if self.board[move.startRow][move.startCol] != "--" :     # clicked square is not empty               ####
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            if(abs(move.startRow-move.endRow)==2  and abs(move.startCol-move.endCol)==2):
                self.board[(move.startRow+move.endRow)//2][(move.startCol+move.endCol)//2] = "--"    # final position of check
# #             else:
# #                 self.board[move.endRow][move.endCol] = "--"
#             ##
            self.moveLog.append(move)   # log the move o we can undo it later
            self.blackToMove = not self.blackToMove   #swap player turn 
        else:
            print("square is empty")
#         #pawn promotion
        if move.isPawnPromotion:
            self.board[move.endRow][move.endCol] = "k"+ move.pieceMoved[1] 
            
   
    '''undo the last move '''
    def undoMove(self):
        if len(self.moveLog) != 0 : # make sure that there is a move to undo 
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
#             self.board[move.endRow][move.endCol] = move.pieceCaptured                 # changing this line of code
            if(abs(move.startRow-move.endRow)==2  and abs(move.startCol-move.endCol)==2):
                self.board[(self.startRow+self.endRow)//2][(self.startCol+self.endCol)//2] = move.pieceCaptured    # final position of check
            else:
                self.board[move.endRow][move.endCol] = move.pieceCaptured 
            
            self.blackToMove =  not self.blackToMove
            
    '''         
    def legalMove(self,move):      # move is object of class Move
        if self.blackTOMove == True :  # if black to move
            
    '''    
    def getAllPossibleMoves(self):
       
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][1]   #  2nd character  of board element gives black (b) and white (w)
                if ((turn == 'b' and self.blackToMove) or (turn == 'w' and  (not self.blackToMove))) :
                    piece = self.board[row][col][0]
                    if piece == 'n':
                        self.getNMoves(row,col,moves)       # normal piece move
                    elif piece == 'k':
                        self.getKMoves(row,col,moves)       # king move
              
        return moves              # return list of possible moves of clicked piece of given color turn 

    def getValidMoves(self):
        return self.getAllPossibleMoves()
    
    def getKMoves(self,row,col,moves):
        if self.blackToMove:   #black piece moves
            if row-1>=0 and col-1>=0 :
                if self.board[row-1][col-1] == "--":                         # forward left move for black
                    moves.append(Move((row,col),(row-1,col-1),self.board))
            if row-1>=0 and col+1<=7 :
                if self.board[row-1][col+1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row-1,col+1),self.board))
                    
                    
            if row-2>=0 and col-2>=0:
                if self.board[row-1][col-1][1] == "w":                      # forward left capture move for black
                    if self.board[row-2][col-2] == "--":
                        moves.append(Move((row,col),(row-2,col-2),self.board))  
            if row-2>=0 and col+2<=7:
                if self.board[row-1][col+1][1] == "w":                      # forward right capture move for black
                    if self.board[row-2][col+2] == "--":
                        moves.append(Move((row,col),(row-2,col+2),self.board)) 
                        
            if row+1<=7 and col+1<=7 :
                if self.board[row+1][col+1] == "--":                         # forward left move for white
                    moves.append(Move((row,col),(row+1,col+1),self.board))
            if row+1<=7 and col-1>=0 :
                if self.board[row+1][col-1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row+1,col-1),self.board))
            if row+2<=7 and col+2<=7:
                if self.board[row+1][col+1][1] == "w":                       # forward left capture move for black
                    if self.board[row+2][col+2] == "--":
                        moves.append(Move((row,col),(row+2,col+2),self.board))  
            if row+2<=7 and col-2>=0:
                if self.board[row+1][col-1][1] == "w":                      # forward right capture move for black
                    if self.board[row+2][col-2] == "--":
                        moves.append(Move((row,col),(row+2,col-2),self.board))   
                        
        if not self.blackToMove:   # white to move
            if row+1<=7 and col+1<=7 :
                if self.board[row+1][col+1] == "--":                         # forward left move for white
                    moves.append(Move((row,col),(row+1,col+1),self.board))
            if row+1<=7 and col-1>=0 :
                if self.board[row+1][col-1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row+1,col-1),self.board))
            if row+2<=7 and col+2<=7:
                if self.board[row+1][col+1][1] == "b":                       # forward left capture move for black
                    if self.board[row+2][col+2] == "--":
                        moves.append(Move((row,col),(row+2,col+2),self.board))  
            if row+2<=7 and col-2>=0:
                if self.board[row+1][col-1][1] == "b":                      # forward right capture move for black
                    if self.board[row+2][col-2] == "--":
                        moves.append(Move((row,col),(row+2,col-2),self.board)) 
                        
            if row-1>=0 and col-1>=0 :
                if self.board[row-1][col-1] == "--":                         # forward left move for black
                    moves.append(Move((row,col),(row-1,col-1),self.board))
            if row-1>=0 and col+1<=7 :
                if self.board[row-1][col+1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row-1,col+1),self.board))
                    
                    
            if row-2>=0 and col-2>=0:
                if self.board[row-1][col-1][1] == "b":                      # forward left capture move for black
                    if self.board[row-2][col-2] == "--":
                        moves.append(Move((row,col),(row-2,col-2),self.board))  
            if row-2>=0 and col+2<=7:
                if self.board[row-1][col+1][1] == "b":                      # forward right capture move for black
                    if self.board[row-2][col+2] == "--":
                        moves.append(Move((row,col),(row-2,col+2),self.board))           

        
    
    def getNMoves(self,row,col,moves):
        if self.blackToMove:   #black piece moves
            if row-1>=0 and col-1>=0 :
                if self.board[row-1][col-1] == "--":                         # forward left move for black
                    moves.append(Move((row,col),(row-1,col-1),self.board))
            if row-1>=0 and col+1<=7 :
                if self.board[row-1][col+1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row-1,col+1),self.board))
            if row-2>=0 and col-2>=0:
                if self.board[row-1][col-1][1] == "w":                      # forward left capture move for black
                    if self.board[row-2][col-2] == "--":
                        moves.append(Move((row,col),(row-2,col-2),self.board))  
            if row-2>=0 and col+2<=7:
                if self.board[row-1][col+1][1] == "w":                      # forward right capture move for black
                    if self.board[row-2][col+2] == "--":
                        moves.append(Move((row,col),(row-2,col+2),self.board))   
        
        if not self.blackToMove:   # white to move
            if row+1<=7 and col+1<=7 :
                if self.board[row+1][col+1] == "--":                         # forward left move for white
                    moves.append(Move((row,col),(row+1,col+1),self.board))
            if row+1<=7 and col-1>=0 :
                if self.board[row+1][col-1] == "--":                         # forward right move for black
                    moves.append(Move((row,col),(row+1,col-1),self.board))
            if row+2<=7 and col+2<=7:
                if self.board[row+1][col+1][1] == "b":                       # forward left capture move for black
                    if self.board[row+2][col+2] == "--":
                        moves.append(Move((row,col),(row+2,col+2),self.board))  
            if row+2<=7 and col-2>=0:
                if self.board[row+1][col-1][1] == "b":                      # forward right capture move for black
                    if self.board[row+2][col-2] == "--":
                        moves.append(Move((row,col),(row+2,col-2),self.board)) 

        
'''elif abs(move.startRow-move.endRow)==2 and abs(move.startCol-move.endCol)==2 :                #for piece capture MOVE
                self.board[move.startRow][move.startCol] = "--"
                self.board[move.endRow][move.endCol] = move.pieceMoved
                move.pieceCaptured = self.board[(move.startRow + move.endRow)//2][(move.startCol + move.endCol)//2]
                self.board[(move.startRow + mov.endRow)//2][(move.startCol + move.endCol)//2] = '--'
                self.moveLog.append(move)
                self.blackToMove = not self.blackToMove '''
        
    
    
    
class Move():
    
#     def __init__(self , startSq , endSq , board):      # startSq   endSq are list of coordinates clicked by user for making move
#         self.startRow = startSq[0]
#         self.startCol = startSq[1]
#         self.endRow = endSq[0]
#         self.endCol = endSq[1]
#         # own logic applied for piece capture
#         self.pieceMoved = board[self.startRow][self.startCol]     # inital position of checker
#         self.pieceCaptured = board[self.endRow][self.endCol]      # final position of checker
#         self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow *10 + self.endCol
#         print(self.moveID)
    
    def __init__(self , startSq , endSq , board):      # startSq   endSq are list of coordinates clicked by user for making move
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        # own logic applied for piece capture
        self.pieceMoved = board[self.startRow][self.startCol]     # inital position of checker
        self.isPawnPromotion = False
        if (self.pieceMoved == "nb" and self.endRow == 0) or (self.pieceMoved == "nw" and self.endRow == 7) :         # black reaches  end 
            self.isPawnPromotion = True
            
            
            
            
        if(abs(self.startRow-self.endRow)==2  and abs(self.startCol-self.endCol)==2):
            self.pieceCaptured = board[(self.startRow+self.endRow)//2][(self.startCol+self.endCol)//2]     # final position of checker
        else:
            self.pieceCaptured = "--"
        
        
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow *10 + self.endCol
        print(self.moveID)
        
        
    def __eq__(self,other):
        if isinstance(other,Move):
            return self.moveID == other.moveID 
        return False
    