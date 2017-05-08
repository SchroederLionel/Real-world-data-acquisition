'''
Created on 10.04.2017

@author: Wolfi
'''

class Player():
    OFFSETY = 1 # Gamefield offset. First row is the scoreboard!
    #-------------------------------------------------------------------------------------
    #-- x 0   1   2   3   4   5   6   7      8
    #-- +---+---+---+---+---+---+---+---+ 
    #-- |0/0|1/0|   |   |   |   |   |   |         0
    #-- +---+---+---+---+---+---+---+---+ 
    #-- 
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |0/1|   |   |   |   |   |   |7/1|  |  1|
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- | P1|   |   |   |   |   |   |P2 |  |   |  2
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |5/3|   |   |  |   |  3
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  4
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  5
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |4/6|   |   |   |  |   |  6
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  7
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |8/8|  8
    #-- +---+---+---+---+---+---+---+---+  +---+  y
    #-------------------------------------------------------------------------------------
    #-- x: Should be 0 for first player & 7 for second player
    #-- y: Standard value is 2
    #-------------------------------------------------------------------------------------
    def __init__(self, lp, x, y = 0):
        self.x = x  # Is used for player column
        self.y = y  # Is the vertical position for the player and collision control
        self.p = 0  # These are the points the player has
        self.drawPlayer(y, y, lp)
    
    #-------------------------------------------------------------------------------------
    #-- Player moves upwards until he reaches the wall
    #-------------------------------------------------------------------------------------
    def up(self, lp):
        if self.y > 0:
            self.y = self.y - 1
            self.drawPlayer(self.y+1, self.y, lp)
    
    #-------------------------------------------------------------------------------------
    #-- Player moves downwards until he reaches the wall
    #-------------------------------------------------------------------------------------
    def down(self, lp):
        if self.y+1 < 7:
            self.y = self.y + 1
            self.drawPlayer(self.y-1, self.y, lp)
    
    #-------------------------------------------------------------------------------------
    #-- Player is drawn to the Launchpad. Player color is standard green
    #-------------------------------------------------------------------------------------
    def drawPlayer(self, old, new, lp):
        lp.LedCtrlXY(self.x, old+self.OFFSETY, 0, 0)     # We shut off the LED at the old place
        lp.LedCtrlXY(self.x, old+self.OFFSETY+1, 0, 0)     # Second LED
        lp.LedCtrlXY(self.x, new+self.OFFSETY, 0, 3)     # We set the new LED at the new place
        lp.LedCtrlXY(self.x, new+self.OFFSETY+1, 0, 3)   # Second LED
    
    #-------------------------------------------------------------------------------------
    #-- Reset points to 0. If new game started!
    #-------------------------------------------------------------------------------------
    def resetPoints(self):
        self.p = 0
    
    #-------------------------------------------------------------------------------------
    #-- Score +1
    #-------------------------------------------------------------------------------------
    def incrementScore(self):
        self.p = self.p + 1
    
    #-------------------------------------------------------------------------------------
    #-- Returns True: if player has 4 or more points
    #-------------------------------------------------------------------------------------
    def hasWon(self):
        return self.p >= 4
    
    #-------------------------------------------------------------------------------------
    #-- Draws the points to the scoreboard (Top round buttons on launchpad)
    #-- n the player (1 or 2)
    #-------------------------------------------------------------------------------------
    def drawPoints(self, lp, n=1):
        n = n - 1
        scoreboardXY = [    [   [0,0],[1,0],[2,0],[3,0]    ],       #Points for player 1 (x,y)
                            [   [7,0],[6,0],[5,0],[4,0]    ]    ]   #Points for player 2 (x,y)
        color = [   [3,3],       # Color for player 1 (red, green) amber
                    [0,3]   ]    # Color for player 2 (red, green) green
        ''' To clear the scoreboard (I dont use it because the scoreboard lights start flickering)
        for i in range(8):
            lp.LedCtrlXY(i, 0, 0, 0)
        '''
        
        # Now we draw the amount of points the player has
        for i in range(min(self.p,4)):
            lp.LedCtrlXY(scoreboardXY[n][i][0], scoreboardXY[n][i][1], color[n][0], color[n][1])
        
