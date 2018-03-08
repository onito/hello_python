""" TEST : ATOM TELETYPE PACKAGE:
  - DAY09_1210_tkinter_turtle.py
  - DOCUMENTATION :
        https://docs.python.org/3.6/library/turtle.html
  - Cursor Notes :
        YELLOW : Junhyeok
        ORANGE : Junhaa
        BLUE   : Sam Okyere
        GREEN  : Jiyong
"""

import turtle as tu
import random
import time

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']
SCREEN_X = 470
SCREEN_Y = 400

tu.speed(0)
tu.shape('turtle')

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.pendown()

def go(forward, angle=0):
    """
    forward=go forward
    angle=turn: left=minus 180 / right= plus 180
    """
    tu.forward(forward)
    tu.right(angle)

def star(pos_x, pos_y, size=10, width=3):
    move(pos_x, pos_y)
    tu.width(width)
    tu.begin_fill()
    tu.left(90+126)
    for i in range(5):
        tu.forward(size)
        tu.right(144)
        tu.forward(size)
        tu.left(72)
    tu.end_fill()
    tu.setheading(0)

def test1_simple_filled_triangle():
    _pen = random.choice(COLOR_PICK)
    _fill = random.choice(COLOR_PICK)
    # tu.color('blue','yellow') # pen, fill-color
    tu.color(_pen, _fill) # pen, fill-color
    tu.width(5)

    tu.begin_fill()

    tu.forward(100)
    tu.left (90)

    tu.forward(100)
    tu.right(90)

    tu.setpos(0,0)

    tu.end_fill()

while True:
    move()
    tu.bgcolor('white')
    for n in range(36):
        test1_simple_filled_triangle()
        go(0,10)

    tu.bgcolor('black')
    tu.color('red','yellow')

    for n in range(40):
        POS_X = random.randint(-470, 470)
        POS_Y = random.randint(-400, 400)
        RANDOME_SIZE = random.randint(10, 50)

        star(POS_X, POS_Y, size=RANDOME_SIZE, width=5)

    time.sleep(10)
    tu.clear()

tu.mainloop()
