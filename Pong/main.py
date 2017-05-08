'''
Created on 09.04.2017

@author: Wolfi
'''

import launchpad_py
import time
import player
import ball
from threading import Thread

lp = launchpad_py.Launchpad()  # We create an instance for my classic Launchpad S
lp.Open()                   # We search and open a connection to the Launchpad
lp.LedAllOn(0)              # We set all LEDs to off (in case some were on!)

b = None                  # Ball variable for the thread to interact with
bThreadState = True       # Variable to kill ballThread if the game is decided or stopped

p1 = None                 # Player variables for the thread to interact with
p2 = None
gameThreadState = True    # Variable to kill gameThread if the game is decided or stopped

class ballThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        global bThreadState, lp, b, p1, p2
        
        while bThreadState:
            time.sleep(b.currentSpeed)
            bThreadState = False if b.moveBall(lp, p1, p2) is False else True
        
        newBall()

class gameThread(Thread): # This thread is only for game interaction
    global lp
    
    def __init__(self):
        Thread.__init__(self)
        #global p1, p2
        #p1 = player.Player(lp, 0)   # Here we initialize player 1 & 2
        #p2 = player.Player(lp, 7)   # Player 1 is left & player 2 is right side
    
    #----------------------------------------------------------------------------------------------------------
    #-- Here we analyse the pressed buttons and move the player accordingly
    #----------------------------------------------------------------------------------------------------------
    def run(self):
        global gameThreadState, lp
        #self.drawPoints(lp)
        while gameThreadState:
            self.controlButton()
            self.drawPoints(lp)
            time.sleep(0.0001)
    
    #----------------------------------------------------------------------------------------------------------
    #-- We use ButtonStateXY() to analyze the pressed buttons.
    #-- This way we get a history of every button that was pressed and released.
    #-- [7, 7, True]     Player 1 UP
    #-- [7, 7, False]    Button released
    #-- [7, 8, True]     Player 1 DOWN
    #-- [7, 8, False]    Button released
    #-- [0, 7, True]     Player 2 UP
    #-- [0, 7, False]    Button released
    #-- [0, 8, True]     Player 2 DOWN
    #-- [0, 8, False]    Button released
    #----------------------------------------------------------------------------------------------------------
    def controlButton(self):
        # We will only look for TRUE buttons.
        # The player will have to press each time to move up or down! (at the moment, could possibly be changed)
        global gameThreadState, lp, p1, p2
        button = lp.ButtonStateXY()
        
        if len(button)>0:
            if button[2] == True: # Second element is True if button was pressed
                if   button[0] == 7 and button[1] == 7: # 7, 7 is for p2 up
                    self.movePlayerUp(p2)
                elif button[0] == 7 and button[1] == 8: # 7, 8 is for p2 up
                    self.movePlayerDown(p2)
                elif button[0] == 0 and button[1] == 7: # 0, 7 is for p2 up
                    self.movePlayerUp(p1)
                elif button[0] == 0 and button[1] == 8: # 0, 8 is for p2 up
                    self.movePlayerDown(p1)
                elif button[0] == 8 and button[1] == 5: # To stop Thread & shut all the LEDs(Stop button on the right side of the launchpad)
                    gameThreadState = False
                    lp.LedAllOn(0)
                else:
                    #print(button)
                    pass
    
    def drawPoints(self, lp):
        global p1, p2
        
        p1.drawPoints(lp, 1)
        p2.drawPoints(lp, 2)
    
    def movePlayerDown(self, p):    # self.movePlayerDown(self.p1)
        global lp
        p.down(lp)
    
    def movePlayerUp(self, p):      # self.movePlayerUp(self.p1)
        global lp
        p.up(lp)

# TODO: Win announcement

# INITIALIZATION TIME
p1 = player.Player(lp, 0)   # Here we initialize player 1 & 2
p2 = player.Player(lp, 7)   # Player 1 is left & player 2 is right side
b = ball.Ball(lp)           # Ball is created and drawn

#We create the threads for our game
gThread = gameThread()
gThread.daemon = True  # Thread shuts off if main thread is closed
bThread = ballThread()
bThread.daemon = True

def newBall():
    # Control if a player won
    if playerWon():
        return
    global bThread, bThreadState, b, lp
    b.newBall(lp) # Initializes the ball
    # Make thread ready to be started
    bThreadState = True
    bThread = ballThread()
    bThread.daemon = True
    bThread.start()

def playerWon():
    global p1, p2, lp, gameThreadState
    if p1.hasWon():
        lp.LedCtrlString("P1-WON", 3, 3, lp.SCROLL_LEFT, 80)
        lp.LedCtrlChar('1', 3, 3, 1, 1)
        time.sleep(3)
        gameThreadState = False
    if p2.hasWon():
        lp.LedCtrlString("P2-WON", 3, 3, lp.SCROLL_LEFT, 80)
        lp.LedCtrlChar('2', 3, 3, 1, 1)
        time.sleep(3)
        gameThreadState = False

    #-------------------------------------------------------------------------------------
    #-- Draws the walls
    #-- NOT USED!! DO NOT USE!!!
    #-------------------------------------------------------------------------------------
def drawGrid(red, green):
    lp.LedAllOn(0)  #initialize Playfield by setting all lights off.
    
    for i in range(8):
        '''Old Game Field. Wall all around the entire field.
        lp.LedCtrlRaw(i*16, red, green)
        lp.LedCtrlRaw(i*16+7, red, green)
        if i > 0:
            lp.LedCtrlRaw(i, red, green)
            lp.LedCtrlRaw(i+112, red, green)
        '''
        #Playfield with only top and bottom walls
        lp.LedCtrlRaw(i, red, green)
        lp.LedCtrlRaw(i+112, red, green)
    
    lp.LedCtrlXY(8, 5, 3, 0) # Stop button lights in red

lp.LedCtrlXY(8, 5, 3, 0) # Stop button lights in red, right round buttons


gThread.start()
bThread.start()

gThread.join()
lp.LedAllOn(0)
