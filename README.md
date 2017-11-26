# Connect-four
from tkinter import *
from tkinter import messagebox
    
def main():
    def exitgame():
        choice = messagebox.askyesno(title="Exit", message="Are you sure you want to exit")
        if choice == 1:
            root.destroy()
    def gamewindow():
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
        gameboard = Label(game, image=gameBG).pack()
        columnButton_1 = Button(game, image=columnicon1, bd=0, bg="#00628B", activebackground="#00628B").place(x=170, y=670)
        columnButton_2 = Button(game, image=columnicon2, bd=0, bg="#00628B", activebackground="#00628B").place(x=270, y=670)
        columnButton_3 = Button(game, image=columnicon3, bd=0, bg="#00628B", activebackground="#00628B").place(x=370, y=670)
        columnButton_4 = Button(game, image=columnicon4, bd=0, bg="#00628B", activebackground="#00628B").place(x=470, y=670)
        columnButton_5 = Button(game, image=columnicon5, bd=0, bg="#00628B", activebackground="#00628B").place(x=570, y=670)
        columnButton_6 = Button(game, image=columnicon6, bd=0, bg="#00628B", activebackground="#00628B").place(x=670, y=670)
        columnButton_6 = Button(game, image=columnicon7, bd=0, bg="#00628B", activebackground="#00628B").place(x=770, y=670)

        
        game.mainloop()
    root = Tk()
    root.title("Connect 4")
    bg = PhotoImage(file="Main Screen-1.png")
    playImage = PhotoImage(file="Play Button 1.png")
    exitImage = PhotoImage(file="Exit Button.png")
    background = Label(root, image=bg).pack()
    play = Button(root, image=playImage, bg="#00628B", bd=0, activebackground="#00628B", command=gamewindow).place(x=350, y=300)
    exitButton = Button(root, image=exitImage, bg="#00628B", bd=0, activebackground="#00628B", command=exitgame).place(x=390, y=450)
    root.mainloop()
main()
