import turtle as tu
import random
import math

COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

tu.speed('fastest')

def move(pos_x=0, pos_y=0):
    tu.penup()
    tu.setx(pos_x)
    tu.sety(pos_y)
    tu.pendown()

def go(go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    tu.forward(go)
    tu.right(angle)

def star(pos_x, pos_y, size=10, width=3):
    tu.color('red','yellow')
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

def draw_triangle(pos_x, pos_y, lowerside, angle=40):
    l = lowerside / 2
    radian = math.radians(angle)
    sameside = l/math.cos(radian)

    tu.color('darkgreen', 'green')
    tu.width(3)
    move(pos_x, pos_y)

    tu.begin_fill()
    tu.right(angle)
    tu.forward(sameside)
    tu.left(180+angle)
    tu.forward(lowerside)
    tu.left(180+angle)
    tu.forward(sameside)
    tu.right(angle)
    tu.end_fill()

def tree_trunk(pos_x, pos_y, forward, width):
    tu.setheading(0)
    tu.setpos(pos_x, pos_y)
    tu.width(width)
    tu.pencolor('brown')
    tu.right(90)
    tu.forward(forward)
    tu.setheading(0)

def xmas_tree(pos_x, pos_y, scale):
    _ratio = 1/scale

    star(pos_x, pos_y+10*_ratio, 20*_ratio, 5*_ratio)
    tree_trunk(pos_x, pos_y-(50*_ratio), 250*_ratio, 10*_ratio)
    draw_triangle(pos_x, pos_y, 100*_ratio)
    draw_triangle(pos_x, pos_y-30*_ratio, 200*_ratio)
    draw_triangle(pos_x, pos_y-60*_ratio, 300*_ratio)
    draw_triangle(pos_x, pos_y-90*_ratio, 400*_ratio)

star(0, 270, 20, 5)
tree_trunk(0, 250, 350, 20)
draw_triangle(0, 260, 100)
draw_triangle(0, 230, 200)
draw_triangle(0, 180, 300)
draw_triangle(0, 110, 400)

for n in range(80):
    _size = random.randint(2,5)
    _posx = random.randint(-470, 470)
    _posy = random.randint(-400, 400)
    xmas_tree(_posx, _posy, _size)

tu.mainloop()
