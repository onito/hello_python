import turtle as tu
import random
import math


COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']
SCREEN_X = 470
SCREEN_Y = 400

tu.speed('fastest')

def go(obj, go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    obj.forward(go)
    obj.right(angle)

def circle(obj, _go, _angle):
    _repeat = int(360/_angle)
    obj.color(random.choice(COLOR_PICK), random.choice(COLOR_PICK))
    obj.begin_fill()
    for n in range(_repeat):
        go(obj, _go, _angle)
        print(obj.pos())
    obj.end_fill()
    # print(tu.pos())

def test1_multi_object():
    _tu = tu.Turtle()
    _tu.speed('fastest')
    _tu.shape('turtle')
    _tu.color('blue', 'green')

    print(_tu.pos())

    # _go = 10
    # _angle = 5
    # _repeat = int(360/_angle)
    # for n in range(_repeat):
    #     go(_go, _angle)
    #     print(tu.pos())
    # # print(tu.pos())

    heading = 0
    for i in range(10):
        heading += 45
        _tu.setheading(heading)
        for n in range(3, 50):
            circle(_tu, 10, n)

        _tu.penup()
        _tu.home()
        _tu.pendown()

        go(_tu, 0, 45)
# test1_multi_object()

def star(obj, pos_x, pos_y, size=10, width=1, trailing=False):
    obj.width(width)
    if trailing:
        obj.setx(pos_x)
        obj.sety(pos_y)
    else:
        obj.penup()
        obj.setx(pos_x)
        obj.sety(pos_y)
        obj.pendown()

    obj.begin_fill()
    obj.left(90+126)
    for i in range(5):
        obj.forward(size)
        obj.right(144)
        obj.forward(size)
        obj.left(72)
    obj.end_fill()
    obj.setheading(0)

def test2_drawing_stars():
    tu.bgcolor('black')

    while True:
        tu.color("orange", "yellow")
        posx = random.randint(-1*SCREEN_X, 1*SCREEN_X)
        posy = random.randint(-1*SCREEN_Y, 1*SCREEN_Y)
        star(tu,posx, posy, size=10, trailing=False)
        print(tu.pos())
        tu.penup()
        tu.home()
        tu.pendown()
# test2_drawing_stars()

_a = tu.Turtle()
_a.color('red', 'yellow')
_a.speed(0)

_b = tu.Turtle()
_b.color('blue', 'orange')
_b.speed(0)

# star(_a, 0, 200, size=80)

def repeat_circle(obj, *loop_args):
    """
    *args = tuple format
    ** Kwargs = dict format
    """
    # if loop_args == ():     # tuple is empty
    if not loop_args:     # tuple is empty
        loop_args = (5, 201, 5)
    obj.begin_fill()
    for n in range(loop_args[0], loop_args[1], loop_args[2]):
        obj.circle(n)
    obj.end_fill

# for n in range(24):
#     line = random.choice(COLOR_PICK)
#     fill = random.choice(COLOR_PICK)
#     _b.color(line, fill)
#     repeat_circle(_b, 100, 201, 10)
#     _b.left(15)

def move(obj, pos_x=0, pos_y=0):
    obj.penup()
    obj.setx(pos_x)
    obj.sety(pos_y)
    obj.pendown()

def triangle(obj, _longi=50):
    """ height : longitude : slop : theta
    s = L / cos(th)             # SLOPE
    h = L * (sin(th)/cos(th))   # HEIGHT
    n(deg)/360 = x(rad)/2.pi() ---> x(rad) = n * 2.PI() / 360
    math.radians(degree)
    """
    _degree = - 40
    _radian = math.radians(_degree)
    _slope = _longi / math.cos(_radian)
    _height = _longi * (math.sin(_radian) / math.cos(_radian))
    print('rad=%s\n\n longi=%s\n slope=%s\n height=%s\n'%(_radian, _longi ,_slope, _height))

    obj.color('darkgreen','green')
    obj.begin_fill()
    go(obj, _longi , -140)
    go(obj, _slope, -80)
    go(obj, _slope, -140)
    go(obj, _longi, 0)
    obj.end_fill()

def xmas_tree():
    tu.color('red', 'yellow')
    star(tu, 0, 360, size=20, width=3)
    tu.width(7)

    pos_x = 0
    pos_y = 350
    _add =10

    for size in range(50, 201, 50):
        _add += 30
        pos_x += 0
        pos_y -= _add

        move(tu, pos_x, pos_y)
        triangle(tu, size)

    tu.width(20)
    tu.pencolor('brown')
    tu.home()
    move(tu, 0, -70)
    tu.home()
xmas_tree()


tu.mainloop()
