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
    y = 1
    x = 0
    vert = 1
    while x < (numberSpaces -1):
        print("first while")
        if 1==1:
            while y < (numberSpaces -1):
                print("second while")
                print("x is",x,"y is",y)
                if scoreList[x][y-1] == scoreList[x][y]:
                    print("vertical match")
                    #print(scoreList[x][y])
                    vert += 1
                    print("Vertical count", vert)
                y += 1

        x += 1
        if vert == numberSpaces:
            print("Winner")
# verticalWin finds if all the cells in the current column are the same value and returns 1 if this is true
def verticalWin(scoreList, column):
    vert = 1
    for i in range(len(scoreList)-1):
        if scoreList[column][i]==scoreList[column][i+1]:
            vert += 1
            print("Vert =", vert)
        else:
            break
    if vert == (len(scoreList)):
        return 1
    else:
        return 0

def horizWin(scoreList, row):
    horiz = 1
    for i in range(len(scoreList)-1):
        if scoreList[i][row]==scoreList[i+1][row]:
            horiz += 1
            print("horiz = ", horiz)
            if horiz == len(scoreList):
                return 1, scoreList[i][row]







myList = [[0,1,0], [1,1,1], [0,1,2]]
print (verticalWin(myList,1))
print (horizWin(myList,1))

# print (myList)
# threeInRow(myList)
# print (myList[0][0], myList[0][1])
# #
# # print (myList)
# #
# #
# # threeInRow(myList)