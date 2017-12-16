"""
# Youtube : https://www.youtube.com/watch?v=htXz33hXHek
#
# py3.6 turtle documentation
#   : https://docs.python.org/3.6/library/tu.html#module-turtle
"""
import time
import math
import random as rnd
import turtle as tu

tu.speed(0)
tu.colormode(255)
tu.width(3)

def set_random_pencolor(obj):
    """ change pencolor randomly """
    rgb_tuple = (rnd.randint(1, 255),
                 rnd.randint(1, 255),
                 rnd.randint(1, 255))
    obj.pencolor(rgb_tuple)
# set_random_pencolor(tu)

def test1_random_walk():
    """ draw lines several times randomly """
    PHI = (1+math.sqrt(5))/2        # fibonacci ratio
    ANGLE = 360/2*PHI               # angle = 291.2461... degree

    def random_walk(obj, turns, distance=10):
        """ main function for change pencolor randomly """
        for x in range(turns):
            print('position= (%s,%s)' %(obj.xcor(), obj.ycor()))
            obj.left(ANGLE)
            distance = rnd.random()*100
            obj.forward(distance)
            if math.fabs(obj.position()[1]) > 100:
                # fabs(x) = return abs.value of x.
                rgb_tuple = (
                    rnd.randint(1, 255),
                    rnd.randint(1, 255),
                    rnd.randint(1, 255))

                obj.pencolor(rgb_tuple)
                obj.up()
                # obj.setpos(0,0)
                obj.sety(0)
                obj.down()

    random_walk(tu, 6000)
    print('\a')
    time.sleep(10)
# test1_random_walk()

def test2_color_wheel():
    """ making simple colored wheel """
    tu.width(1)
    tu.up()
    tu.goto(370, 0)
    tu.down()

    PHI = (1+math.sqrt(5))/2        # fibonacci ratio
    ANGLE = 360/math.pi*(PHI)       # angle = 185.412037... degree

    for x in range(355):
        set_random_pencolor(tu)
        tu.right(ANGLE)
        tu.forward(700)
# test2_color_wheel()

def test3_color_wheel_v01():
    """ more complicated color wheel ver.1 """
    tu.width(3)
    tu.up()
    tu.goto(370, -60)
    tu.down()

    ANGLE = 203.78      # angle = 185.412037... degree

    color_pick = ['red', 'green', 'blue', 'yellow', 'darkgreen', 'orange',
                  'darkred', 'lightgreen', 'darkblue', 'gray', 'purple', 'pink']
    pos = 0
    for n in range(14):

        if pos >= len(color_pick)-1:
            pos = 0

        tu.pencolor(color_pick[pos])
        pos += 1
        for x in range(72):
            tu.right(ANGLE)
            tu.forward(800)
# test3_color_wheel_v01()

def test4_sunflower(posx, posy):
    """
    # Spiral Phyllotaxis Demo - Example for VSFX 705
    # https://blog.trinket.io/interactive-python/
    #
    # Turtle Sunflowers - Introduce Phyllotactic Pattern
    # Author: Deborah R. Fowler
    #
    # March 21, 2013
    # Based on original code in C 1989 using Silicon Graphics & gl
    """

    def draw_phyllotaxy_pattern(obj, times, petalstart, angle=137.508, cspread=4):
        """print a pattern of circles using spiral phyllotactic data"""
        # initialize position
        # obj.pen(outline=1,pencolor="black",fillcolor="orange")
        obj.color('black')
        obj.fillcolor("orange")
        phi = angle * (math.pi / 180.0)
        xcenter = posx
        ycenter = posy

        # for loops iterate in this case from the first value until < 4, so
        for n in range(0, times):
            r = cspread * math.sqrt(n)
            theta = n * phi

            x = r * math.cos(theta) + xcenter
            y = r * math.sin(theta) + ycenter

            # move the turtle to that position and draw
            obj.up()
            obj.setpos(x, y)
            obj.down()
            # orient the turtle correctly
            obj.setheading(n * angle)
            if n > petalstart-1:
                obj.color("yellow")
                draw_petal(obj, x, y)
            else: obj.stamp()

    def draw_petal(obj, x, y):
        """ making flower's leaves - petal """
        obj.up()
        obj.goto(x, y)
        obj.pendown()
        obj.color('black')
        obj.fillcolor('yellow')
        obj.begin_fill()
        obj.right(20)
        obj.forward(70)
        obj.left(40)
        obj.forward(70)
        obj.left(140)
        obj.forward(70)
        obj.left(40)
        obj.forward(70)
        obj.up()
        obj.end_fill() # this is needed to complete the last petal

    tina = tu.Turtle()
    tina.shape("turtle")
    tina.speed(0) # make the turtle go as fast as possible
    draw_phyllotaxy_pattern(tina, 200, 160, 137.508)
    tina.up()
    # tina.exitonclick() # lets you x out of the window when outside of idle
    tina.forward(1000)
# test4_sunflower(-30, 25)

def test5_tree_hello(posx, posy):
    """ making colored hello tree """
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    def tree(obj, b, l, d=1):
        obj.forward(l)
        if b > 0:
            obj.pencolor(rnd.choice(colors))
            obj.left(45/d)
            tree(obj, b-1, l*.8, d+1)
            obj.right(90/d)
            tree(obj, b-1, l*.8, d+1)
            obj.left(45/d)
        obj.backward(l)
    tanya = tu.Turtle()

    tanya.up()
    tanya.goto(posx, posy)
    tanya.down()

    tanya.width(3)
    tanya.left(90)
    tanya.up()
    tanya.pencolor(rnd.choice(colors))
    tanya.backward(100)
    tanya.down()
    tree(tanya, 5, 75)
    tanya.up()
    tanya.goto(posx+0, posy+180)
    tanya.down()
    tanya.write('Hello~! \nI\'m Tanya', font=("Arial", 20, "normal"), align='center')
# test5_tree_hello(-250, -200)


class BoxTurtle(tu.Turtle):
    """
    # Class Object Oriented Programming
    # https://blog.trinket.io/
    """
    def __init__(self, posx=0, posy=0, pen='blue', fill='orange'):
        """
        # (1) Inherit turtle.Turtle() class
        # (2) tu.Turtle class (parent) initialize
        # (3) Add more for local initialize .. color, shape, & more.
        """
        tu.Turtle.__init__(self)
        self.speed(1)
        self.color(pen, fill)
        self.shape("turtle")
        self.goto(posx, posy)

    def say(self, message):
        """ say hello I'm blah blah~ """
        self.write(message, font=("Arial", 20, "normal"), align='center')


def test6_multi_object_class():
    """ main executable commands """
    selly = tu.Turtle()
    selly.shape('turtle')
    selly.goto(0, 100)
    selly.write("I'm Selly", font=("Arial", 20, "normal"), align="center")

    johnny = BoxTurtle(100, 0, pen='blue', fill='orange')
    johnny.say("I'm Johnny")

    michael = BoxTurtle(0, -100, pen='red', fill='darkgreen')
    michael.say("I'm Michael")

    roy = BoxTurtle(-100, 0, pen='green', fill='pink')
    roy.say("I'm Roy")

    # help(BoxTurtle)

if __name__ == '__main__':
    test6_multi_object_class()
    tu.mainloop()
