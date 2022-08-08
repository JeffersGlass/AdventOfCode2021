with open ("input.txt", 'r') as infile:
    inputChunks = infile.read().split('\n\n')

#---Parse the Input to make it useful----

allCalledNumbers = [int(num) for num in inputChunks[0].split(',')]
boards = [' '.join(chunk.split('\n')) for chunk in inputChunks[1:]] #get boards

#Make board list of ints instead of long string by splitting every 3 characters
intBoards = [[int(b[n:n+2]) for n in range(0, len(b), 3)] for b in boards]

#boardrows is a list of boards, each of which are a list of rows in each board,
#each of which is a list of ints
boardRows = [[b[index:index+5] for index in range(0, 25, 5)] for b in intBoards]

#boardcols is a list of boards, each of of which is a list of columns in each board, 
#each of which is a list of ints
boardCols = [[[b[row][index] for row in range(5)] for index in range(5)] for b in boardRows]

#---Define some functions to help us solve the problem as written---

#For a given board (by row or column), are any of its lines made up only of numbers in 'calledNums'?
def isBoardAWin(board, calledNums):
    return any([all([num in calledNums for num in line]) for line in board])

#Score is (sum of uncalled numbers on board) * (last number called)
def calcScore(board, calledNumbers):
    unusedNumbers = [num for line in board for num in line if num not in calledNumbers]
    return sum(unusedNumbers) * calledNumbers[-1]

def doWin(board, calledNumbers):
    print(f"Score is {calcScore(b, calledSoFar)}")
    exit()

#---Find solution---

for i in range(len(allCalledNumbers)):
    calledSoFar = allCalledNumbers[:i]
    print(f"Searching for wins with numbers {calledSoFar}")
    winner = False
    for b in boardRows:
        if isBoardAWin(b, calledSoFar):
            print(f"Winner board by row! \n {b}")
            doWin(b, calledSoFar)

    
    for b in boardCols:
        if isBoardAWin(b, calledSoFar):
            print(f"Winner board by column! \n {b}")
            doWin(b, calledSoFar)

    print(f"No winners after {i} numbers, calling next number")