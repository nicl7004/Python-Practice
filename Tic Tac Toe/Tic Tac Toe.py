#simple tic tac toe game

numberSpaces = int(input("Enter your number of spaces."))

x = 0

def sideSpace():
    print("___" * numberSpaces)

def verticalBar():
    print("|  " * numberSpaces)


while x < numberSpaces:
    sideSpace()
    verticalBar()

    x += 1
sideSpace()