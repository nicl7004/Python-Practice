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

def sanitize(input):
    input = input.replace(' ', '')
    input = input.replace(',', '')
    input = list(input)
    return input

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
    y = len(scoreList) - 1

    x = 0
    while len(scoreList)>x:
        if scoreList[x][y] == scoreList[x+1][y-1]:
            diag += 1
            y -= 1
            x += 1
            if diag == len(scoreList):
                return[1, scoreList[0][len(scoreList)-1]]
    return 0

myList = [[1,1,2],
          [1,2,1],
          [2,1,0]]
score = threeInRow(myList)

# #print("Horiz wins =", score[0])
# if score[0] != 0:
#     print("Horiz win = true")
#     print("Horiz win number", score[0][1])
# #print("Vert wins =", score[1])
# if score[1] != 0:
#     print("Vert win = true")
#     print("Vert wins number", score[1][1])
# #print("Diag wins =", score[2])
# if score[2] != 0:
#     print("Diag win = true")
#     print("Diag wins number", score[2][1])
# else:
#     print("No winner")
winner = 0
print (myList)
myList = [9] * numberSpaces
myList = [myList for x in range(numberSpaces)]
# myList = [9]*numberSpaces
# myList = [myList]* numberSpaces
print (myList)
while winner == 0:
    playerOne = input("Please select the coordinates where you want to put your piece player 1")
    playerTwo = input("Please select the coordinates where you want to put your piece player 2")
    # sanatize
    playerOne = sanitize(playerOne)
    playerTwo = sanitize(playerTwo)
    playerOneX = int(playerOne[0])-1
    playerOneY = int(playerOne[1])-1
    playerTwoX = int(playerTwo[0])-1
    playerTwoY = int(playerTwo[1])-1
    print (playerOneX)
    print (playerOneY)
    myList[playerOneX][playerOneY][playerOneY]= 1

    print(myList)
    break

#print ("Player One", playerOne, "Player Two", playerTwo)
