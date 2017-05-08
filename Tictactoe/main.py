# +---+---+---+---+---+---+---+---+  +---+
	# |0/1| x | | | x | x | | | x | x |  |   |  1
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  2
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |5/3|   |   |  |   |  3
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  4
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  5
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |4/6|   |   |   |  |   |  6
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |   |  7
	# +---+---+---+---+---+---+---+---+  +---+
	# |   |   |   |   |   |   |   |   |  |8/8|  8
	# +---+---+---+---+---+---+---+---+  +---+



import launchpad_py
import random
import time

field = [" "]*10

def theWinnerIs(field, letter):
    """ Return true or false if there is a Winner """
    return (field[1] == letter and field[2] ==letter and field[3] == letter
    or field[4] == letter and field[5] == letter and field[6] == letter
    or field[7] == letter and field[8] == letter and field[9] == letter
    or field[1] == letter and field[4] == letter and field[7] == letter
    or field[2] == letter and field[5] == letter and field[8] == letter
    or field[3] == letter and field[6] == letter and field[9] == letter
    or field[1] == letter and field[5] == letter and field[9] == letter
    or field[3] == letter and field[5] == letter and field[7] == letter)

def displayField(lp):
    """ Displays the Field on the pad """
    for i in range(0, 8):
        for j in range(1, 9):
            if i== 2 or i == 5:
                lp.LedCtrlXY(i, j, 3, 3)
            if j%3 == 0 and j > 0:
                lp.LedCtrlXY(i, j, 3, 3)

def setDisplayToBeginnig(lp):
    """ Reset field """
    for i in range(0, 9):
        for j in range(1, 9):
            lp.LedCtrlXY(i, j, 0, 0)
    displayField(lp)

def setCross(lp,player,field,letter):
    """ User can set X or 0 on the Launchpad """
    r = 0
    g = 0
    print("player selected: ", player)
    #Player selection:
    if player == 1:
        r = 3
        g = 0
    elif player == 2:
        r = 0
        g = 3
    #Row 1
    button = lp.ButtonStateXY()
    
    while True:
        if len(button) > 0:
            break
        else:
            button = lp.ButtonStateXY()
        time.sleep(0.01)
    
    if button[2] == False: return False
    
    if (button[0] == 0 or button[0] == 1) and (button[1] == 1 or button[1] == 2) and (field[1] == " "):
        field[1] = letter
        for i in range (0, 2):
                for j in range (1, 3):
                    lp.LedCtrlXY(i, j, g, r)
    elif (button[0] == 3 or button[0] == 4) and (button[1] == 1 or button[1] == 2) and (field[2] == " "):
        field[2] = letter
        for i in range (3, 5):
                for j in range (1, 3):
                    lp.LedCtrlXY(i, j, g, r)
    elif (button[0] == 6 or button[0] == 7) and (button[1] == 1 or button[1] == 2) and (field[3] == " "):
        field[3] = letter
        for i in range (6, 8):
                for j in range (1, 3):
                    lp.LedCtrlXY(i, j, g, r)

    #Row 2
    elif (button[0] == 0 or button[0] == 1) and (button[1] == 3 or button[1] == 4) and (field[4] == " "):
        field[4] = letter
        for i in range (0, 2):
                for j in range (4, 6):
                    lp.LedCtrlXY(i, j, g, r)

    elif (button[0] == 3 or button[0] == 4) and (button[1] == 3 or button[1] == 4) and (field[5] == " "):
        field[5] = letter
        for i in range (3, 5):
                for j in range (4, 6):
                    lp.LedCtrlXY(i, j, g, r)

    elif (button[0] == 7 or button[0] == 9) and (button[1] == 3 or button[1] == 4) and (field[6] == " "):
        field[6] = letter
        for i in range (6, 8):
                for j in range (4, 6):
                    lp.LedCtrlXY(i, j, g, r)
        #Row 3
    elif (button[0] == 0 or button[0] == 1) and (button[1] == 7 or button[1] == 8) and (field[7] ==" "):
            field[7] = letter
            for i in range (0, 2):
                for j in range (7, 9):
                    lp.LedCtrlXY(i, j, g, r)
    elif (button[0] == 3 or button[0] == 4) and (button[1] == 7 or button[1] == 8) and (field[8] == " "):
            field[8] = letter
            for i in range (3, 5):
                for j in range (7, 9):
                    lp.LedCtrlXY(i, j, g, r)
    elif (button[0] == 6 or button[0] == 7) and (button[1] == 7 or button[1] == 8) and (field[9] ==" "):
            field[9] = letter
            for i in range (6, 8):
                for j in range (7, 9):
                    lp.LedCtrlXY(i, j, g, r)
    else:
        return False
    return True


def equal(field):
    """ Looks if all the fields are played """
    return (field[1] != " " and field[2] != " " and field[3] != " "
    and field[4] != " " and field[5] != " " and field[6] != " "
    and field[7] != " " and field[8] != " " and field[9] != " ")

def allOnForWinner(field,letter,lp):
    """ Leds of the field in one color to see the winner """
    g = 0
    r = 0
    if letter == " X ":
        r = 3
        g = 0
    else:
        r = 0
        g = 3
    for i in range(0,8):
        for j in range(1,9):
            lp.LedCtrlXY(i, j, g, r)
    time.sleep(2)
    lp.LedAllOn(0)


def main():
    """ Main function as known in C or Java """
    lp = launchpad_py.Launchpad() 
    lp.Open()
    lp.LedAllOn(0)
    displayField(lp)
    player = 1
    while True:
        time.sleep(0.01)
        if player == 1:
            letter = " X "
        if player == 2:
            letter = " O "
        if setCross(lp, player, field, letter):
            if player == 1:
                player = 2
            else:
                player = 1
            if  theWinnerIs(field, letter):
                if letter == " X ":
                    allOnForWinner(field,letter,lp)
                if letter == " O ":
                    allOnForWinner(field,player,lp)
                break
            if equal(field):
                lp.LedAllOn(lp.LedGetColor(3, 3))
                break
  
        

if __name__ == '__main__':
    main()