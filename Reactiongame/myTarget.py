import time

class myTarget():
    def launchfunc(self, delay, lp, col, row):
        self.endTime = 0
        self.startTime = 0
        self.hit = False
        self.startTime = time.time()
        
        while(self.endTime - self.startTime <= delay and self.hit == False):
            self.endTime = time.time()
            
            #self.getButton(lp)
            
            button = lp.ButtonStateXY()
            if len(button)>0:
                print(button)
                if(button[2] == True and button[0] == col and button[1] == row):
                    self.hit = True
                    print("You hit me in Time!")
                    lp.LedCtrlXY(col,row,0,3)
                    time.sleep(2)
                    lp.LedCtrlXY(col,row,0,0)
                    return self.hit
        print("Too slow!")
        return self.hit