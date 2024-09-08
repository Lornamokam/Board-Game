# Author: Lorna Sisang Mokam 
# Email: lmokam@umass.edu
# Spire ID: 34317469

def make_empty_board (nrows,ncols):
    return ["." * ncols for i in range(nrows)]
#print(make_empty_board(6, 4)) # 6 rows and 4 cols

def print_board (board):
    nrows = len(board)
    ncols = len (board [0])
    for r in range(nrows):
        rows = ""
        for c in range(ncols):
            if board [r][c] == "X":
                rows += " X "
            elif board [r][c] == "O":
                rows += " O "
            else:
                rows += "   "

            if c < ncols-1:
                rows += "|"
        print (rows)
        if r < (nrows -1):
            dash = "---+" * (ncols - 1) + "---"
            print (dash)
#print_board(make_empty_board(5, 6))
#print_board([".......", ".......", "..O....", "..OX...", ".OXOX..",".OXXOXX"])

def verify_board (board):
    nrows = len(board)
    ncols = len (board [0])
    numX = 0
    numC = 0
    for r in range(nrows):
        for c in range(ncols):
            if board [r][c] == "X":
                numX += 1
            elif board [r][c] == "O":
                numC += 1
    if numX - numC < 0:
        if numC -numX > 1:
            return False
    else:
        if numX - numC > 1:
            return False
    for r in range(nrows-1):
        for c in range(ncols):
            if board [r][c] != ".":
                if board[r+1][c] == ".":
                    return False
                
    return True
                


    
board = [".......", ".......", "..O....", "..OX...", ".O.OX..",".O.XOX."]
print(verify_board(board))
board = ["X......", ".......", "..O....", "..OX...", ".O.OX..",".O.XOXX"]
print(verify_board(board))

def verify_move (board, column):
    nrows = len(board)
    ncols = len (board [0])
    if column <0 or column>= ncols:
        return False
    if board [0][column]!= ".":
        return False
    return True
board = ["..O....", "..X....", "..O....", "..OX...", ".OXOX..",".OXXOX."] 
print(verify_move(board, 2)) 

def update_board(board,column,disc):
    nrows = len(board)
    for r in range(nrows-1,-1,-1): 
        if board [r][column]== ".":
            board [r] =  board [r][:column] + disc + board [r][column +1:]
            return board
game_board = [".......", ".......", "..O....", "..OX...", ".OXOX..", ".OXXOX."]
updated_board = update_board(game_board, 2, "X")
print(updated_board)


def has_won(board, column):
    nrows = len(board)
    ncols = len(board[0])
    toprow = -1
    disc = None
    for r in range(nrows):
        if board[r][column] != ".":
            toprow = r
            disc = board[toprow][column]
            break
    if toprow == -1 or nrows - toprow < 4:
        return False

    count = 1  
    for i in range(1, 4):
        if 0 <= toprow + i < nrows and board[toprow + i][column] == disc:
            count += 1
        else:
            break
    if count == 4:
        return True

   
    count = 1 
    for i in range(column - 1, -1, -1):
        if 0 <= i < ncols and board[toprow][i] == disc:
            count += 1
        else:
            break
    for i in range(column + 1, min(column + 4, ncols)):
        if 0 <= i < ncols and board[toprow][i] == disc:
            count += 1
        else:
            break

    if count >= 4:
        return True

    count = 1
    for i, j in zip(range(toprow - 1, -1, -1), range(column - 1, -1, -1)):
        if 0 <= i < nrows and 0 <= j < ncols and board[i][j] == disc:
            count += 1
        else:
            break

    for i, j in zip(range(toprow + 1, nrows), range(column + 1, ncols)):
        if 0 <= i < nrows and 0 <= j < ncols and board[i][j] == disc:
            count += 1
        else:
            break

    if count >= 4:
        return True

    count = 1
    for i, j in zip(range(toprow - 1, -1, -1), range(column + 1, ncols)):
        if 0 <= i < nrows and 0 <= j < ncols and board[i][j] == disc:
            count += 1
        else:
            break

    for i, j in zip(range(toprow + 1, nrows), range(column - 1, -1, -1)):
        if 0 <= i < nrows and 0 <= j < ncols and board[i][j] == disc:
            count += 1
        else:
            break

    if count >= 4:
        return True

    return False

































