import turtle as tu

screen = tu.Screen()        # create the screen

t1 = tu.Turtle()            # create the first turtle
t1.shape('turtle')
t1.color('blue','yellow')

t2 = tu.Turtle()            # create the second turtle
t2.color('red', 'green')
t2.pensize(3)               # the same as t2.width(3)

screen.onscreenclick(t1.goto)
# set up the callback for moving the first turtle (t1)

def move_second():          # the function to move the second turtle
    t2.back(100)
    t2.forward(200)
    t2.back(100)
    screen.ontimer(move_second) # which sets itself up to be called again

screen.ontimer(move_second) # set up the initial call to the callback
screen.mainloop() # start everything running
