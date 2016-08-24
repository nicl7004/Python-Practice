#simple tic tac toe game

numberSpaces = int(input("Enter your number of spaces."))

x = 0

def sideSpace():
    print(" ___" * numberSpaces)

def verticalBar():
    print("|   " * (numberSpaces + 1))



while x < numberSpaces:
    sideSpace()
    verticalBar()
    x += 1
sideSpace()


def threeInRow(scoreList):
    x=0
    for x in range(len(scoreList)):
        vertMatches = verticalWin(scoreList,x)
        horizMatches = horizWin(scoreList, x)
        if (horizMatches) != 0:
            break
        elif (vertMatches) != 0:
            break
        x+=1

    return horizMatches, vertMatches, diagWin(scoreList)
# # verticalWin finds if all the cells in the current column are the same value and returns 1 if this is true
def horizWin(scoreList, column):
    vert = 1
    for i in range(len(scoreList)-1):
        if scoreList[column][i]==scoreList[column][i+1]:
            vert += 1
            #print("Vert =", vert)
            if vert == len(scoreList):
                return [1, scoreList[column][i]]
    return 0
#horizWin finds if all the cells in the current row are the same value and returns (1, value in cell)
def verticalWin(scoreList, row):
    horiz = 1
    for i in range(len(scoreList)-1):
        if scoreList[i][row]==scoreList[i+1][row]:
            horiz += 1
            #print("horiz = ", horiz)
            if horiz == len(scoreList):
                return [1, scoreList[i][row]]
    return 0

def diagWin(scoreList):
    diag = 1
    for i in range(len(scoreList)-1):
        if scoreList[i][i] == scoreList[i+1][i+1]:
            diag += 1

            if diag == len(scoreList):
                return[1, scoreList[0][0]]
    return 0




myList = [[0,1,0],
          [1,2,0],
          [0,1,0]]
score = threeInRow(myList)

#print("Horiz wins =", score[0])
if score[0] != 0:
    print("Horiz win = true")
    print("Horiz win number", score[0][1])
#print("Vert wins =", score[1])
if score[1] != 0:
    print("Vert win = true")
    print("Vert wins number", score[1][1])
#print("Diag wins =", score[2])
if score[2] != 0:
    print("Diag win = true")
    print("Diag wins number", score[2][1])
