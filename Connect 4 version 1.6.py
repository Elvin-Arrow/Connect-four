from tkinter import *
from tkinter import messagebox


def initialiseGameBoard():
    for row in range(6):
        for column in range(7):
            gameBoard[row][column] = "-"


def printGameBoard():
    for row in range(6):
        for column in range(7):
            print(gameBoard[row][column], end='')
        print()


def setPlayerColumn(buttonNumber):
    print()
    global playerColumn
    global moveFlag
    if gameBoard[0][buttonNumber] == "-":
        playerColumn = buttonNumber
        moveFlag = True
        print("Player selected column:", int(playerColumn) + 1)
    else:
        global columnFlag
        columnFlag = True
        print("Column is full!")


def nextEmptyPosition(playerColumn, playerMarker):
    row = int(5)
    while gameBoard[row][playerColumn] != "-" and row >= 0:
        row -= 1
    if row >= 0:
        gameBoard[row][playerColumn] = playerMarker
    return row


def swapPlayers(playerMarker, turnCounter):
    if playerMarker == "o":
        playerMarker = "x"
        print("Player two")
        print("Player Marker: ", playerMarker)
    else:
        playerMarker = "o"
        print("Player one")
        print("player Marker: ", playerMarker)
    turnCounter += 1
    return playerMarker, turnCounter


def horizontalJudge(playerMarker, playerRow, playerColumn):
    victoryFlag = False
    column = playerColumn
    victoryCounter = int(0)  # Counter for same pieces
    # Checking West
    while column >= 0 and not victoryFlag:
        column -= 1
        if column >= 0:
            if gameBoard[playerRow][column] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0

    # Checking East
    column = playerColumn
    while column < 7 and not victoryFlag:
        column += 1
        if column < 7:
            if gameBoard[playerRow][column] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0

    return victoryFlag


def verticalJudge(playerMarker, playerRow, playerColumn):
    victoryFlag = False
    row = playerRow
    victoryCounter = int(0)
    # Checking North
    while row >= 0 and not victoryFlag:
        row -= 1
        if row >= 0:
            if gameBoard[row][playerColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0

    # Checking South
    row = playerRow
    while row < 6 and not victoryFlag:
        row += 1
        if row < 6:
            if gameBoard[row][playerColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0

    return victoryFlag


def diagonalJudge(playerMarker, row, column):
    victoryFlag = False
    subRow = int(0)
    subColumn = int(0)
    victoryCounter = int(0)

    # Checking first diagonal
    # North west
    subRow = row
    subColumn = column
    while subRow >= 0 and subColumn >= 0 and not victoryFlag:
        subRow -= 1
        subColumn -= 1
        if subRow >= 0 and subColumn >= 0:
            if gameBoard[subRow][subColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0
    # South east
    subRow = row
    subColumn = column
    while subRow < 6 and subColumn < 7 and not victoryFlag:
        subRow += 1
        subColumn += 1
        if subRow < 6 and subColumn < 7:
            if gameBoard[subRow][subColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0
    # Checking the other diagonal
    # North East
    victoryCounter = int(0)
    subRow = row
    subColumn = column
    while subRow >= 0 and subColumn < 7 and not victoryFlag:
        subRow -= 1
        subColumn += 1
        if subRow >= 0 and subColumn < 7:
            if gameBoard[subRow][subColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0

    # South West
    subRow = row
    subColumn = column
    while subRow < 6 and subColumn >= 0 and not victoryFlag:
        subRow += 1
        subColumn -= 1
        if subRow <= 5 and subColumn >= 0:
            if gameBoard[subRow][subColumn] == playerMarker:
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                victoryCounter = 0
    return victoryFlag


gameBoard = [[0 for i in range(7)] for j in range(6)]


def main():
    def exitgame():
        choice = messagebox.askyesno(title="Exit", message="Are you sure you want to exit")
        if choice == 1:
            root.destroy()

    def gamewindow():
        def fullNotification():
            messagebox.showerror(title="Caution", message="The following column is already full")
            global columnFlag
            columnFlag = False

        def setPlayerBar(marker):
            if marker == "o":
                xcoords = 25
            else:
                xcoords = 908
            barLabel.place(x=xcoords, y=130)

        def setPlayerIcon():
            xcoords = int(168)
            ycoords = int(65)
            # Row, meaning x-coordinates of the piece
            for i in range(playerColumn):
                xcoords += 100
            # Column, meaning the y-coordinates of the piece
            for i in range(pieceRow):
                ycoords += 100
            if playerMarker == "o":
                    Label(game, image=playerOne, bg="#00628B").place(x=xcoords, y=ycoords)
            else:
                Label(game, image=playerTwo, bg="#00628B").place(x=xcoords, y=ycoords)

        root.destroy()
        game = Tk()
        game.title("Connect 4")
        gameBG = PhotoImage(file="GameBG.png")
        icon1 = PhotoImage(file="Player 1.png")
        icon2 = PhotoImage(file="Player 2.png")
        columnicon1 = PhotoImage(file="Column Button-1.png")
        columnicon2 = PhotoImage(file="Column Button-2.png")
        columnicon3 = PhotoImage(file="Column Button-3.png")
        columnicon4 = PhotoImage(file="Column Button-4.png")
        columnicon5 = PhotoImage(file="Column Button-5.png")
        columnicon6 = PhotoImage(file="Column Button-6.png")
        columnicon7 = PhotoImage(file="Column Button-7.png")
        bar = PhotoImage(file="Player bar.png")
        playerOne = PhotoImage(file="Player 1.png")
        playerTwo = PhotoImage(file="Player 2.png")
        gameboard = Label(game, image=gameBG).pack()
        columnButton_1 = Button(game, image=columnicon1, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(0)).place(x=170, y=670)
        columnButton_2 = Button(game, image=columnicon2, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(1)).place(x=270, y=670)
        columnButton_3 = Button(game, image=columnicon3, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(2)).place(x=370, y=670)
        columnButton_4 = Button(game, image=columnicon4, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(3)).place(x=470, y=670)
        columnButton_5 = Button(game, image=columnicon5, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(4)).place(x=570, y=670)
        columnButton_6 = Button(game, image=columnicon6, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(5)).place(x=670, y=670)
        columnButton_6 = Button(game, image=columnicon7, bd=0, bg="#00628B", activebackground="#00628B",
                                command=lambda: setPlayerColumn(6)).place(x=770, y=670)
        barLabel = Label(game, image=bar)
        winnerMessage = StringVar()
        victoryFlag = False
        global moveFlag
        gameExit = False
        drawFlag = False
        playerMarker = "x"
        turnCounter = int(0)
        piecerow = int(0)
        initialiseGameBoard()
        printGameBoard()
        setPlayerBar("o")
        while not gameExit:
            if columnFlag:
                fullNotification()
            while not victoryFlag and moveFlag:
                marker = playerMarker
                playerMarker, turnCounter = swapPlayers(playerMarker, turnCounter)
                if turnCounter > 42:
                    break
                setPlayerBar(marker)
                pieceRow = nextEmptyPosition(playerColumn, playerMarker)
                setPlayerIcon()
                printGameBoard()
                if turnCounter >= 7:
                    if not victoryFlag:
                        victoryFlag = horizontalJudge(playerMarker, pieceRow, playerColumn)
                    if not victoryFlag:
                        victoryFlag = verticalJudge(playerMarker, pieceRow, playerColumn)
                    if not victoryFlag:
                        victoryFlag = diagonalJudge(playerMarker, pieceRow, playerColumn)
                moveFlag = False
            if playerMarker == "o" and victoryFlag and turnCounter <= 42:
                print("Congratulations! Player one")
                winnerMessage = "Congratulations! Player one, you just won the game."
            elif playerMarker == "x" and victoryFlag and turnCounter <= 42:
                print("Congratulations! Player two")
                winnerMessage = "Congratulations! Player two, you just won the game."
            elif turnCounter > 42:
                print("Game draw")
            if victoryFlag and turnCounter <= 42:
                messagebox.showinfo(title="Winner", message=winnerMessage)
                gameExit = True
            elif turnCounter > 42:
                messagebox.showinfo(title="Winner", message="Game draw!")
                gameExit = True
            game.update_idletasks()
            game.update()
        game.destroy()
        main()
    root = Tk()
    root.title("Connect 4")
    bg = PhotoImage(file="Main Screen-1.png")
    playImage = PhotoImage(file="Play Button.png")
    exitImage = PhotoImage(file="Exit Button.png")
    background = Label(root, image=bg).pack()
    play = Button(root, image=playImage, bg="#00628B", bd=0, activebackground="#00628B", command=gamewindow).place(
        x=350, y=300)
    exitButton = Button(root, image=exitImage, bg="#00628B", bd=0, activebackground="#00628B", command=exitgame).place(
        x=390, y=450)
    root.mainloop()


moveFlag = False
columnFlag = False
playerColumn = int(0)
main()
