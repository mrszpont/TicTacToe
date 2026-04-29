from tkinter import *
from tkinter import ttk
from typing import List
import tkinter.font
root = Tk("TicTacToe","TicTacToe","TicTacToe")
tkFont = tkinter.font.Font(root,family="Calibri",size=34)
tkFont2 = tkinter.font.Font(root,family="Calibri",size=17)
root.configure(background="#0F0F0F")
frm = Frame(root)
frm.place(in_=root, anchor="c", relx=.5, rely=.5,y=14)
player_turn = 0
players = ("X","O")
WIN = None
ttk.Label(root, text="Kółko i Krzyżk",foreground="white",background="#0F0F0F", font=tkFont).place(in_=root,anchor="n",relx=.5)
informacje = ttk.Label(root, text="Kolej \"X\"",foreground="white",background="#0F0F0F", font=tkFont2)
informacje.place(in_=root,anchor="n",relx=.5,y=52)
def checkIfWon():
    global Pola, WIN
    for _y in range(3):
        y = _y*3
        a = None
        Lost = False
        for i in range(3):
            Pole = Pola[y+i]
            if Pole.claimedBy == "" or (a != None and a != Pole.claimedBy):
                Lost = True
                break
            a = Pole.claimedBy
        if not Lost:
            WIN = a
            break
    for _x in range(3):
        x = _x
        a = None
        Lost = False
        for i in range(3):
            Pole = Pola[x+i*3]
            if Pole.claimedBy == "" or (a != None and a != Pole.claimedBy):
                Lost = True
                break
            a = Pole.claimedBy
        if not Lost:
            WIN = a
            break
    if Pola[0].claimedBy != "" and Pola[0].claimedBy == Pola[4].claimedBy and Pola[0].claimedBy == Pola[8].claimedBy:
        WIN = Pola[0].claimedBy
    if Pola[6].claimedBy != "" and Pola[6].claimedBy == Pola[4].claimedBy and Pola[6].claimedBy == Pola[2].claimedBy:
        WIN = Pola[6].claimedBy
    if WIN != None:
        informacje.config(text= f"{WIN} WYGRAŁ!")
    else:
        czyremis = True
        for v in Pola:
            if v.claimedBy == "":
                czyremis = False
                break
        if czyremis:
            WIN = "REMIS"
            informacje.config(text=f"REMIS!")
def reset():
    global WIN,player_turn
    player_turn = 0
    WIN = None
    informacje.config(text="Kolej \"X\"")
    for v in Pola:
        v.claimedBy = ""
        v.button.config(text="")
class Pole():
    def __init__(self,i):
        self.claimedBy = ""
        self.button = Button(frm, text="", width=4,height=1,command= lambda: self.press(players[player_turn]))
        self.button["font"] = tkFont
        self.button.grid(column=(i % 3), row=int(i / 3))
    def press(self,claimedby):
        global player_turn
        if WIN != None:
            reset()
            return
        if self.claimedBy != "": return
        player_turn = (player_turn+1)%len(players)
        informacje.config(text= f"Kolej \"{players[player_turn]}\"")
        self.claimedBy = claimedby
        self.button.config(text=claimedby)
        checkIfWon()
Pola: List[Pole] = []
for i in range(9):
    Pola.append(Pole(i))
root.mainloop()