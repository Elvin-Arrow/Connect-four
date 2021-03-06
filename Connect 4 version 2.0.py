from tkinter import *
from tkinter import messagebox
import pygame
from pygame import mixer
import time
#--------------------------------------------------------------------------------------------------------------
pygame.init()
move_sound = pygame.mixer.Sound("Move.wav")
win_sound = pygame.mixer.Sound("Win_Sound.wav")
#--------------------------------------------------------------------------------------------------------------
def initialiseGameBoard():  #Function to initialise the Game board
    for row in range(6):
        for column in range(7):
            gameBoard[row][column] = "-"
#--------------------------------------------------------------------------------------------------------------
def setPlayerColumn(buttonNumber):  #Function to store the player selected column 
    global playerColumn    #Telling python that the vairables exists globally and needs to be iniliased a new
    global moveFlag
    if gameBoard[0][buttonNumber] == "-":   #Check whether this column is empty
        playerColumn = buttonNumber     
        moveFlag = True 
        print("Player selected column:", int(playerColumn) + 1)
    else:
        messagebox.showerror(title="Caution", message="The following column is already full")
        print("Column is full!")
#--------------------------------------------------------------------------------------------------------------
def nextEmptyPosition(playerColumn, playerMarker):  
    row = int(5)    #Start checking from the bottom of the board
    while gameBoard[row][playerColumn] != "-" and row >= 0:
        row -= 1
    if row >= 0:
        gameBoard[row][playerColumn] = playerMarker
    return row
#--------------------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------
def horizontalJudge(playerMarker, playerRow, playerColumn): #Judge to check for horizontal player victory
    global winList
    victoryFlag = False
    column = playerColumn
    winList.append(column) #Store the player's latest move's column number
    victoryCounter = int(0)  # Counter for same pieces
    # Checking West from the point of player's latest move
    while column >= 0 and not victoryFlag:
        column -= 1
        if column >= 0:
            if gameBoard[playerRow][column] == playerMarker:
                winList.append(column) #If there is a same piece on the left of the current piece, store its coordinates
                victoryCounter += 1
                if victoryCounter == 3:
                    winList.append(playerRow)   #Store the row in which the player has won
                    victoryFlag = True
            else:
                break
    # Checking East from the point of player's latest move
    column = playerColumn
    while column < 7 and not victoryFlag:
        column += 1
        if column < 7:
            if gameBoard[playerRow][column] == playerMarker:
                winList.append(column)
                victoryCounter += 1
                if victoryCounter == 3:
                    winList.append(playerRow)
                    victoryFlag = True
            else:
                break
    if not victoryFlag:
        winList = []    #If no one won, reset the win list
    return victoryFlag
#--------------------------------------------------------------------------------------------------------------
def verticalJudge(playerMarker, playerRow, playerColumn):
    global winList
    victoryFlag = False
    verticalFlag = False
    row = playerRow
    winList.append(row) #Store the player's latest move's row number
    victoryCounter = int(0)
    # Checking South from the point of player's latest move
    row = playerRow
    while row < 6 and not victoryFlag:
        row += 1
        if row < 6:
            if gameBoard[row][playerColumn] == playerMarker:
                winList.append(row)
                victoryCounter += 1
                if victoryCounter == 3:
                    winList.append(playerColumn) #If there is a same piece below the current piece, store its coordinates
                    victoryFlag = True
            else:
                break
    if not victoryFlag:
        winList = [] #If no one won, reset the win list
    return victoryFlag
#--------------------------------------------------------------------------------------------------------------
def diagonalJudge(playerMarker, row, column):
    global winDirection
    global winList
    victoryFlag = False
    subRow = int(0)
    subColumn = int(0)
    victoryCounter = int(0)    
    # Checking first diagonal
    # North west
    subRow = row
    subColumn = column
    #Store the player's latest move's coordinates
    winList.append(subRow)
    winList.append(subColumn)
    while subRow >= 0 and subColumn >= 0 and not victoryFlag:
        subRow -= 1
        subColumn -= 1
        if subRow >= 0 and subColumn >= 0:
            if gameBoard[subRow][subColumn] == playerMarker:
                winList.append(subRow)
                winList.append(subColumn)
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                break
    # South east
    subRow = row
    subColumn = column
    while subRow < 6 and subColumn < 7 and not victoryFlag:
        subRow += 1
        subColumn += 1
        if subRow < 6 and subColumn < 7:
            if gameBoard[subRow][subColumn] == playerMarker:
                winList.append(subRow)
                winList.append(subColumn)
                victoryCounter += 1
                if victoryCounter == 3:
                    victoryFlag = True
            else:
                break
    if not victoryFlag:
        winlist = [] #If no one won, reset the win list
    else:
        winDirection = "Left Diagonal"
    # Checking the other diagonal
    # North East
    victoryCounter = int(0)
    subRow = row
    subColumn = column
    winList.append(subRow)
    winList.append(subColumn)
    while subRow >= 0 and subColumn < 7 and not victoryFlag:
        subRow -= 1
        subColumn += 1
        if subRow >= 0 and subColumn < 7:
            if gameBoard[subRow][subColumn] == playerMarker:
                winList.append(subRow)
                winList.append(subColumn)
                victoryCounter += 1
                if victoryCounter == 3:
                    winDirection = "Right Diagonal"
                    victoryFlag = True
            else:
                break
    # South West
    subRow = row
    subColumn = column
    while subRow < 6 and subColumn >= 0 and not victoryFlag:
        subRow += 1
        subColumn -= 1
        if subRow <= 5 and subColumn >= 0:
            if gameBoard[subRow][subColumn] == playerMarker:
                winList.append(subRow)
                winList.append(subColumn)
                victoryCounter += 1
                if victoryCounter == 3:
                    winDirection = "Right Diagonal"
                    victoryFlag = True
            else:
                break
    if not victoryFlag:
        winList = [] #If no one won, reset the win list
    return victoryFlag
#--------------------------------------------------------------------------------------------------------------
def toggleMusic(window, buttonClicked):
    global musicState
    #Check whether thrr window was changed or the button was clicked
    if (window == "Main" or window == "Game") and not buttonClicked:    
        if musicState == 1:
            pygame.mixer.music.play(-1)
        else:
            #if the music is not to be played then, start then load the new window's music 
            pygame.mixer.music.play(-1)
            pygame.mixer.music.pause()
        pygame.mixer.music.set_volume(0.1) #Setting the volume of the music
    elif (window == "Main" or window == "Game") and buttonClicked:
        if musicState == 1:
          pygame.mixer.music.pause()
          musicState = 0
        else:
          pygame.mixer.music.unpause()
          musicState = 1
#--------------------------------------------------------------------------------------------------------------                
def main():
    def lableUpdate(): #Function to decide music button's image
        if musicState == 1:
            icon = music_icon_off
            musicButton.config(image=icon)      
        else:
            icon = music_icon_on
            musicButton.config(image=icon)
        root.update()   #Refresh the screen to show changes
        #Call function toggleMusic and let it know that it was called from main via a button
        toggleMusic("Main", True) 
        
    def exitgame():
        choice = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
        if choice == 1:
            pygame.mixer.music.stop()
            root.destroy()
    
    def gamewindow():   #The function for main game window
        def reset():    #Function to reset the current game board
            choice = messagebox.askyesno(title="Exit", message="Are you sure you want to reset the game?")
            if choice == 1:                
                global resetFlag
                resetFlag = True
                game.destroy()
                gamewindow()

        def exit_main():    #Function to quit to main from the game board
            global resetFlag
            resetFlag = False
            #Check whether the game has ended or is the player force ending the game
            if not gameExit:
                choice = messagebox.askyesno(title="Exit", message="Are you sure you want to exit?")
                if choice == 1:
                    pygame.mixer.music.stop()
                    game.destroy()
                    main()
            else:               
                pygame.mixer.music.stop()
                game.destroy()
                main()

        def setPlayerBar(marker):   #Function to update the location of player turn indicator
            if marker == "o":
                xcoords = 25
            else:
                xcoords = 908
            barLabel.place(x=xcoords, y=130)

        def setPlayerIcon():    #Function to place the player piece on the game board
            global musicState
            if musicState == 1:
                pygame.mixer.Sound.play(move_sound)
            xcoords = int(168)
            ycoords = int(65)
            # Finding the Column, meaning x-coordinates of the piece as per the game board
            for i in range(playerColumn):
                xcoords += 100
            # Finding the Row, meaning the y-coordinates of the piece as per the game board
            for i in range(pieceRow):
                ycoords += 100
            if playerMarker == "o":
                    Label(game, image=playerOne, bg="#00628B").place(x=xcoords, y=ycoords)
            else:
                Label(game, image=playerTwo, bg="#00628B").place(x=xcoords, y=ycoords)

        def setVictoryBar():    #Function to display cross on the four connected pieces
            global winDirection
            if winDirection == "Horizontal":
                xcoords = int(208)
                ycoords = int(100)
                cross = PhotoImage(file="Horizontal cross.png")
                #Find the least the column number from the win list
                smallest = winList[0]   
                for i in range(1, 4):
                    if winList[i] < smallest:
                        smallest = winList[i]    
                for i in range(smallest):
                    xcoords += 100
                for i in range(winList[4]):
                    ycoords += 100
                Label(game, image = cross).place(x=xcoords, y=ycoords)
                game.update()
                time.sleep(1)
            elif winDirection == "Vertical":
                  xcoords = 204
                  ycoords = 102
                  cross = PhotoImage(file="Vertical cross.png")
                  smallest = winList[0]
                  for i in range(winList[4]):
                      xcoords += 100
                  for i in range(1, 4):
                      if winList[i] < smallest:
                          smallest = winList[i]
                  for i in range(smallest):
                      ycoords += 100
                  Label(game, image = cross).place(x=xcoords, y=ycoords)
                  game.update()
                  time.sleep(1)
            elif winDirection == "Right Diagonal":                
                xcoords = 205
                ycoords = 305
                cross = PhotoImage(file="Right_DC.png")
                smallest_x = winList[1]
                largest_y = winList[0]
                for i in range(1, len(winList)+1, 2):
                    if winList[i] < smallest_x:
                        smallest_x = winList[i]
                for i in range(0, len(winList), 2):
                    if winList[i] > largest_y:
                        largest_y = winList[i]
                for i in range(smallest_x):
                    xcoords += 100
                for i in range(5, largest_y+1, -1):
                    ycoords -= 100
                Label(game, image=cross).place(x=xcoords, y=ycoords)
                game.update()
                time.sleep(1)
            else:           
                xcoords = 205
                ycoords = 105
                cross = PhotoImage(file="Left_DC.png")
                smallest_x = winList[1]
                smallest_y = winList[0]
                for i in range(1, len(winList)+1, 2):
                    if winList[i] < smallest_x:
                        smallest_x = winList[i]
                for i in range(0, len(winList), 2):
                    if winList[i] < smallest_y:
                        smallest_y = winList[i]
                for i in range(smallest_x):
                    xcoords += 100
                for i in range(0, smallest_y, 1):
                    ycoords += 100
                cr = Label(game, image=cross)
                cr.place(x=xcoords, y=ycoords)
                game.update()
                time.sleep(1)

        global resetFlag
        if not resetFlag:
            root.destroy()
        pygame.mixer.music.load("Friday_Morning.wav")
        toggleMusic("Game", False)
        game = Tk()
        menubar = Menu()
        game.title("Connect 4")
        game.geometry("1024x776+250+20")        
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
        music_icon_on = PhotoImage(file="music on.png")
        music_icon_off = PhotoImage(file="music off.png")
        gameboard = Label(game, image=gameBG).pack()
        soundlist = Menu()
        exitMenu = Menu()
        state = BooleanVar()
        global musicState
        if musicState == 1:
            state.set(True)
            soundlist.add_checkbutton(label="Music", variable=state, command=lambda: toggleMusic("Game", True))
        else:
            state.set(False)
            soundlist.add_checkbutton(label="Music", variable=state, command=lambda: toggleMusic("Game", True))       
        menubar.add_cascade(label="Sound options", menu=soundlist)       
        exitMenu.add_command(label="Reset Game", command=reset)
        exitMenu.add_command(label="Exit to main", command=exit_main)
        menubar.add_cascade(label="Exit", menu=exitMenu)
        game.config(menu=menubar)
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
        setPlayerBar("o")
        while not gameExit:
            while not victoryFlag and moveFlag:
                marker = playerMarker
                playerMarker, turnCounter = swapPlayers(playerMarker, turnCounter)
                if turnCounter > 42:
                    break
                setPlayerBar(marker)
                pieceRow = nextEmptyPosition(playerColumn, playerMarker)
                setPlayerIcon()
                if turnCounter >= 7:
                    global winDirection
                    if not victoryFlag:
                        victoryFlag = horizontalJudge(playerMarker, pieceRow, playerColumn)
                        if victoryFlag:
                            winDirection = "Horizontal"
                    if not victoryFlag:
                        victoryFlag = verticalJudge(playerMarker, pieceRow, playerColumn)
                        if victoryFlag:
                            winDirection = "Vertical"
                    if not victoryFlag:
                        victoryFlag = diagonalJudge(playerMarker, pieceRow, playerColumn)
                moveFlag = False
            if playerMarker == "o" and victoryFlag and turnCounter <= 42:
                pygame.mixer.music.stop()
                print("Congratulations! Player one")
                winner = PhotoImage(file="Congrats P1.png")
            elif playerMarker == "x" and victoryFlag and turnCounter <= 42:
                pygame.mixer.music.stop()
                print("Congratulations! Player two")
                winner = PhotoImage(file="Congrats P2.png")
            elif turnCounter > 42:
                pygame.mixer.music.stop()
                print("Game draw")
                messagebox.showinfo(title="Drawi", message="Game Draw!")
            if victoryFlag and turnCounter <= 42:
                if musicState == 1:
                    pygame.mixer.Sound.play(win_sound)
                pygame.mixer.music.load("W!nner.wav")
                setVictoryBar()
                time.sleep(1)                
                bg = PhotoImage(file="WinnerBG.png")
                if musicState == 1:
                    pygame.mixer.music.play()
                Label(game, image=bg).place(x=0, y=0)
                Label(game, image= winner).place(x=250, y=200)
                game.update()
                if musicState == 1:
                    time.sleep(9)
                else:
                    time.sleep(3)
                gameExit = True
            elif turnCounter > 42:
                messagebox.showinfo(title="Draw", message="Game draw!")
                gameExit = True
            game.update_idletasks()
            game.update()
        exit_main()
#--------------------------------------------------------------------------------------------------------------       
    root = Tk()
    root.title("Connect 4")
    root.geometry("1024x776+250+20")
    bg = PhotoImage(file="Main Screen.png")
    playImage = PhotoImage(file="Play Button.png")
    exitImage = PhotoImage(file="Exit Button.png")
    music_icon_on = PhotoImage(file="music on.png")
    music_icon_off = PhotoImage(file="music off.png")
    background = Label(root, image=bg).pack()
    pygame.mixer.music.load("Prelude_No_8.wav")
    global winDirection
    winDirection = ""
    play = Button(root, image=playImage, bg="#00628B", bd=0, activebackground="#00628B", command=gamewindow).place(
        x=365, y=300)
    exitButton = Button(root, image=exitImage, bg="#00628B", bd=0, activebackground="#00628B", command=exitgame).place(
        x=400, y=450)
    toggleMusic("Main", False)
    #Check whether music is on or not before setting the button's image
    if musicState == 1:
        musicButton = Button(root, image=music_icon_on, bd=0, bg="#00628B", activebackground="#00628B", command=lableUpdate)
    else:
        musicButton = Button(root, image=music_icon_off, bd=0, bg="#00628B", activebackground="#00628B", command=lableUpdate)
    musicButton.place(x=950, y=670)
    root.mainloop()
#--------------------------------------------------------------------------------------------------------------    
gameBoard = [[0 for i in range(7)] for j in range(6)]
musicState = 1
winDirection = ""   #Variable to store the winning direction of the player
moveFlag = False    
resetFlag = False
playerColumn = int(0)
winList = []    #List to store the location of the winner's pieces
main()  #Calling the main function
