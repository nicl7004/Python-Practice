#simple tic tac toe game

numberSpaces = 0 #int(input("Enter your number of spaces."))

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
    print(scoreList[0][0], scoreList[1][0], scoreList[2][0])
    #if scoreList[0,]

myList = [[0,1,2], [0,1,2], [0,1,2]]

print (myList)


threeInRow(myList)