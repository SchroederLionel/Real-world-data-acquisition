'''
Created on 10.04.2017

@author: Wolfi
'''
import time
from math import pow
from random import randint

class Ball():
    OFFSETX = 0
    OFFSETY = 1
    MAXX = 7
    MAXY = 7
    SPEEDCOEF = 0.0025
    INITIALSPEED = None # When ball gets resettet, is initialized inside constructor
    x = None
    y = None
    velX = None
    velY = None
    ballAlive = True
    currentSpeed = None
    
    #-------------------------------------------------------------------------------------
    #-- Ball is initialized
    #-- Speed is in seconds and determintes how often the ball is moved
    #-------------------------------------------------------------------------------------
    def __init__(self, lp, speed = 0.4):
        self.x = 2
        self.y = 1
        self.velX = 1
        self.velY = 1
        self.currentSpeed = speed
        self.INITIALSPEED = speed
        self.drawBall([self.x,self.y], [self.x,self.y], lp)
        time.sleep(2)
        
    def newBall(self, lp):
        # Now we shut off the red ball after 1 SECOND
        time.sleep(1)
        lp.LedCtrlXY(self.x+self.OFFSETX, self.y+self.OFFSETY, 0, 0)
        
        # Now we set the new X and Y coordinates and draw it already
        self.x = 5 if self.x==7 else 2
        self.y = randint(3,4)
        lp.LedCtrlXY(self.x+self.OFFSETX, self.y+self.OFFSETY, 3, 3)
        
        # Initialize Speed
        self.currentSpeed = self.INITIALSPEED
        self.velX = 1 if self.x==2 else -1
        self.velY = int(pow(-1, randint(1,2))) # gives randomly -1 or 1
        time.sleep(1.5)
        self.ballAlive = True
    
    def drawBall(self, old, new, lp):
        #random = randint(0, 3)
        red = 3
        green = 3 if self.ballAlive else 0 # Ball gets red when ballAlive is False
        lp.LedCtrlXY(old[0]+self.OFFSETX, old[1]+self.OFFSETY, 0, 0)          # extingish old LED
        lp.LedCtrlXY(new[0]+self.OFFSETX, new[1]+self.OFFSETY, red, green)    # power-on new LED
        
    #-------------------------------------------------------------------------------------
    #-- x 0   1   2   3   4   5   6   7      8
    #-- +---+---+---+---+---+---+---+---+ 
    #-- |   |   |   |   |   |   |   |   |         0
    #-- +---+---+---+---+---+---+---+---+ 
    #-- W = WALL
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |0;0|   |   |   |   |   |   |7;0|  |  1|
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  2 The collsision field for the ball is from 0;0 to 7;7
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   | B | P |  |   |  3
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   | P |  |   |  4
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  5
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  6
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |   |   |   |   |   |   |   |   |  |   |  7
    #-- +---+---+---+---+---+---+---+---+  +---+
    #-- |0;7|   |   |   |   |   |   |7;7|  |8/8|  8
    #-- +---+---+---+---+---+---+---+---+  +---+  y
    #-------------------------------------------------------------------------------------
    def moveBall(self, lp, p1, p2):
        if not self.ballAlive:
            # Draw ball
            self.drawBall([self.x, self.y], [self.x, self.y], lp)
            
            return False
        MAXX = self.MAXX
        MAXY = self.MAXY
        x = self.x
        y = self.y
        
        # Check for player collisions
        if (  (((x+1)==p1.x or (x-1)==p1.x) and (y==p1.y or y==p1.y+1)) or 
              (((x+1)==p2.x or (x-1)==p2.x) and (y==p2.y or y==p2.y+1))  ):
            self.velX = self.velX*(-1)
        
        # Now we calculate the new X and Y
        newX = self.x + self.velX
        newY = self.y + self.velY
        
        # Check if ball is dead (behind the player)
        if newX==0: # Player 2 will get a point
            # Draw and update ball
            self.updateBall(newX, y if newY==p1.y or newY==(p1.y+1) else newY, False)
            self.drawBall([x, y], [self.x, self.y], lp)
            p2.incrementScore()
            return False # One point to player 2
        elif newX==MAXX:
            # Draw and update ball
            self.updateBall(newX, y if newY==p2.y or newY==(p2.y+1) else newY, False)
            self.drawBall([x, y], [self.x, self.y], lp)
            p1.incrementScore()
            return False # One point to player 1
        
        # Check for wall collision
        if newY == 0 or newY == MAXY:
            self.velY = self.velY*(-1)
        
        # Draw and update ball
        self.drawBall([self.x, self.y], [newX, newY], lp)
        self.updateBall(newX, newY)
        
    
    #-------------------------------------------------------------------------------------
    #-- Ball gets the new coordinates and saves them to self
    #-- Ball is set alive standard:True or False
    #-- Speed is updated
    #-------------------------------------------------------------------------------------
    def updateBall(self, x, y, alive=True):
        self.x = x
        self.y = y
        self.ballAlive = alive
        self.currentSpeed = self.currentSpeed - self.SPEEDCOEF
        
    