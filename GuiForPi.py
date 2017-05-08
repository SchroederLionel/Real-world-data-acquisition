'''
Created on 08.05.2017

@author: Jerome
'''
from Tkinter import *
import subprocess as sub


def playPong(event):
    p = sub.Popen(["python", "/home/pi/launchpad/pong/main.py"])
    p.wait()

def playTicTacToe(event):
    p = sub.Popen(["python", "/home/pi/launchpad/tictactoe/main.py"])
    p.wait()

def playReactionGame(event):
    p = sub.Popen(["python", "/home/pi/launchpad/reactiongame/main.py"])
    p.wait()

root = Tk()
root.title("Launchpad Gaming Station")
root.geometry("480x320")
topFrame = Frame(root)
topFrame.pack()

theLabel1 = Label(topFrame, text="Launchpad Gaming Station!", fg="red", font=("Arial", 16))
theLabel = Label(topFrame, text="Choose a game to play!", fg="blue")
theLabel1.pack()
theLabel.pack()

button1 = Button(topFrame, width="70", height="5", text="Play Pong")
button1.bind("<Button-1>", playPong)
button2 = Button(topFrame, width="70", height="5", text="Play TicTacToe")
button2.bind("<Button-1>", playTicTacToe)
button3 = Button(topFrame, width="70", height="5", text="Play ReactionGame")
button3.bind("<Button-1>", playReactionGame)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()

