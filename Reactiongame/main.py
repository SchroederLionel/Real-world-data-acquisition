import myTarget
import random
import launchpad_py
import time

lp = launchpad_py.Launchpad()
lp.Open()
lp.LedAllOn(0)

class Main():
    global lp
    #row = 0
    #col = 0
    def __init__(self):
        global lp
        self.delay = 5
        self.score = 0
        self.my = myTarget.myTarget()
        
    def calculateDelay(self):
        self.delay = self.delay - 0.5
    
    def run(self):
        global lp
        while(self.delay >= 0):
            self.row = random.randrange(0,6)
            self.col = random.randrange(0,6)
            print(self.col)
            print(self.row)
            
            lp.LedCtrlXY(self.col, self.row, 3, 3)
            
            if(self.my.launchfunc(self.delay, lp,  self.col, self.row) == True):
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                self.score = self.score +1
            else:
                lp.LedCtrlXY(self.col,self.row,3,0)
                time.sleep(2)
                lp.LedAllOn(0)
                exit()
                
            print(self.score)
            self.calculateDelay()
            
            if self.score == 1:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 8, 0, 3)
                
            if self.score == 2:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 7, 0, 3)
                
            if self.score == 3:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 7, 0, 3)
                lp.LedCtrlXY(0, 8, 0, 3)
                
            if self.score == 4:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 6, 0, 3)
                
            
            if self.score == 5:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 6, 0, 3)
                lp.LedCtrlXY(0, 8, 0, 3)
            
            if self.score == 6:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 6, 0, 3)
                lp.LedCtrlXY(0, 7, 0, 3)
                
            if self.score == 7:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 6, 0, 3)
                lp.LedCtrlXY(0, 7, 0, 3)
                lp.LedCtrlXY(0, 8, 0, 3)
            
            if self.score == 8:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 5, 0, 3)
            
            if self.score == 9:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 5, 0, 3)
                lp.LedCtrlXY(0, 8, 0, 3)
            
            if self.score == 10:
                for i in range(9):
                    lp.LedCtrlXY(0, i, 0, 0)
                lp.LedCtrlXY(0, 5, 0, 3)
                lp.LedCtrlXY(0, 7, 0, 3)
                      
#    def __init__(self):
#        while(self.delay >= 0):
#            self.row = random.randrange(0,8)
#            self.col = random.randrange(0,8)
#            print(self.col)
#           print(self.row)
#           lp[input()][input()] = True
#            target.Target(self.delay, lp, self.col, self.row)
#            self.calculateDelay()
            
Main().run()