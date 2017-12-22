"""
#
# - DOCUMENTATION : TURTLE
# : https://docs.python.org/3.6/library/turtle.html
"""

import turtle as tu
import random
import math
import time

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

tu.speed(0)

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setpos(pos_x, pos_y)
    tu.pendown()

def go(go, angle=0):
    """
    # go=forward
    # angle=turn: left=minus 180 / right= plus 180
    """
    tu.forward(go)
    tu.right(angle)



def draw_color_bulb(pos_x, pos_y, size=10, width=3, pen='red', fill='yellow'):
    move(pos_x, pos_y+size/2)
    tu.width(width)
    tu.color(pen, fill)
    tu.begin_fill()
    tu.circle(size)
    tu.end_fill()


if __name__ == '__main__':
    while True:
        for n in range(random.randint(5,20)):
            posy = random.randint(-250,450)
            posx = random.choice([-1,1])*0.3*(500-posy)/random.randint(1,4)
            size = random.randint(10,20)
            width = 3
            pen = random.choice(COLOR_PICK)
            fill = random.choice(COLOR_PICK)

            draw_color_bulb(posx, posy, size=size, width=width, pen=pen, fill=fill)
            print('%s , %s' %(posx, posy))
        time.sleep(1)
