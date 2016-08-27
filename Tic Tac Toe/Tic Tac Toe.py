#simple tic tac toe game

numberSpaces = int(input("Enter your number of spaces."))

winner = 0
while (winner == 0):
    myList = [[9] * numberSpaces for i in range(numberSpaces)]
    def sanitize(input):
        input = input.replace(' ', '')
        input = input.replace(',', '')
        input = list(input)
        return input
    def playerMove(myList):
        while winner == 0:
            playerNum = input("Are you X or O?")
            player = input("Please select the coordinates where you want to put your piece player ")
            # sanatize
            player = sanitize(player)
            playerOneX = int(player[0]) - 1
            playerOneY = int(player[1]) - 1
            print(playerOneX)
            print(playerOneY)
            return (playerOneX, playerOneY, playerNum)
            myList[playerOneX][playerOneY] = playerNum
            print(myList)
            break
    def sideSpace():
        print("_____" * numberSpaces)


    coordinates = playerMove(myList)
    def verticalBar(y):
        #print("|   " * (numberSpaces + 1))
        for x in range(numberSpaces+1):
            print("|   ", end = " ")
            if (x) == coordinates[0]:
                if(y) == coordinates[1]:
                    print(coordinates[2], end=" ")


    x = 0
    y = 0

    while x < numberSpaces:
        print("")
        sideSpace()
        verticalBar(y)
        x += 1
        y+= 1



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


    winner = threeInRow(myList)





    #print ("Player One", playerOne, "Player Two", playerTwo)
