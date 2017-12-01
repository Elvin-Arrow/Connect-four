# Connect-four
# v1.6
from tkinter import *

from tkinter import messagebox


    def initialiseGameBoard():  # Function for initialising the game board (console)

        for row in range(6):
            for column in range(7):
                gameBoard[row][column] = "-"


    def printGameBoard(): # Function for printing game board on the console

        for row in range(6):
            for column in range(7):
                print(gameBoard[row][column], end='')
            print()


    def setPlayerColumn(buttonNumber):  # Function for setting the value for column number for which the button was pressed

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


    def nextEmptyPosition(playerColumn, playerMarker):  # Find next empty position in the player's choosen column

        row = int(5)
        while gameBoard[row][playerColumn] != "-" and row >= 0:
            row -= 1
        if row >= 0:
            gameBoard[row][playerColumn] = playerMarker
        return row


    def swapPlayers(playerMarker, turnCounter): # Change players

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


    def horizontalJudge(playerMarker, playerRow, playerColumn): # Check for horizontal combinations

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


    def verticalJudge(playerMarker, playerRow, playerColumn): # Checks for vertical combinations

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


    def diagonalJudge(playerMarker, row, column): # Checks for diagonal combinations

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


    gameBoard = [[0 for i in range(7)] for j in range(6)] # Initialising the 2-D array


    def main():

        def exitgame(): # Function for closing the game

            choice = messagebox.askyesno(title="Exit", message="Are you sure you want to exit")
            if choice == 1:
                root.destroy()

        def gamewindow(): # Function containing the game

            def fullNotification(): # Function responsible for notifying player when a column is full

                messagebox.showerror(title="Caution", message="The following column is already full")
                global columnFlag
                columnFlag = False

            def setPlayerBar(marker): # Function for adjusting the player bar

                if marker == "o":
                    xcoords = 25
                else:
                    xcoords = 908
                barLabel.place(x=xcoords, y=130)

            def setPlayerIcon():  # Function for placing the player piece in the game window

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

            root.destroy()  # Close main screen
            game = Tk() # Create game screen
            game.title("Connect 4")
        
   # All images assigned to respective variables
        
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
            bar = PhotoImage(file="Player bar.png") # Set the image for the player indicator
            playerOne = PhotoImage(file="Player 1.png")
            playerTwo = PhotoImage(file="Player 2.png")

   # Placement of all the labels and buttons
        
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
            barLabel = Label(game, image=bar) # Label generated using the image stored in 'bar' variable

            winnerMessage = StringVar() # Variable to store winner message (belongs to Tk class)
            victoryFlag = False 
            global moveFlag # Tellng python that moveFlag is a global var, so look for the var
            gameExit = False
            drawFlag = False
            playerMarker = "x"  # Variable for current player initialised with dummy value
            turnCounter = int(0)  # Variable responsible for storing number of turns
            piecerow = int(0) # Variable responsible for housing the row (x-coordinates) of recently placed piece
            initialiseGameBoard() # setup console gameboard
            printGameBoard()  # print gameboard on the console
            setPlayerBar("o") # Place the turn indicator

            while not gameExit: # Game loop

                if columnFlag:  # Check whether column is full or not
                    fullNotification()

                while not victoryFlag and moveFlag: # Loop responsible for decisions

                    marker = playerMarker # Store the marker for the last player 
                    playerMarker, turnCounter = swapPlayers(playerMarker, turnCounter)
                    if turnCounter > 42:  # Check for draw
                        break

                    setPlayerBar(marker)
                    pieceRow = nextEmptyPosition(playerColumn, playerMarker)  # Get the row for the lastest move
                    setPlayerIcon() # Place the player icon at the found position
                    printGameBoard()  # Print on console 
                    if turnCounter >= 7:  # No combination possible before 7 moves. If true call the judges

                        if not victoryFlag:
                            victoryFlag = horizontalJudge(playerMarker, pieceRow, playerColumn)

                        if not victoryFlag:
                            victoryFlag = verticalJudge(playerMarker, pieceRow, playerColumn)

                        if not victoryFlag:
                            victoryFlag = diagonalJudge(playerMarker, pieceRow, playerColumn)

                    moveFlag = False  # One move has been completed
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

                game.update_idletasks() # Allow game window to receive click events
                game.update() # Refresh the game window to show new items

            game.destroy()  # Close game window
            main()

        root = Tk() # Create main screen
        root.title("Connect 4") # Set main screen title
        bg = PhotoImage(file="Main Screen-1.png") # Set main screen background
        playImage = PhotoImage(file="Play Button 1.png")
        exitImage = PhotoImage(file="Exit Button.png")
        background = Label(root, image=bg).pack()
        play = Button(root, image=playImage, bg="#00628B", bd=0, activebackground="#00628B", command=gamewindow).place(
            x=350, y=300)
        exitButton = Button(root, image=exitImage, bg="#00628B", bd=0, activebackground="#00628B", command=exitgame).place(
            x=390, y=450)
        root.mainloop()

    moveFlag = False  # Flag for checking whether the player made a move or not

    columnFlag = False  # Flag for checking whether a column is empty or not

    playerColumn = int(0) # Varialbe responsible for housing player selected column

    main()  # main function called
