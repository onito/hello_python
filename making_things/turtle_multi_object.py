import turtle as tu
COLOR_PICK = ['red','green','yellow','blue','orange','violet','gray',
    'purple','pink', 'darkblue','darkgreen','darkorange','darkred','darkgray']

def move(obj, pos_x=0, pos_y=0):
    obj.penup()
    obj.setx(pos_x)
    obj.sety(pos_y)
    obj.pendown()

def go(obj, go, angle=0):
    """
    go=forward
    angle=turn: left=minus 180 / right= plus 180
    """
    obj.forward(go)
    obj.right(angle)

_a = tu.Turtle()
_a.color('red','green')
_a.width(10)

for n in range(3):
    go(_a, 100, -90)
    go(_a, 100, 90)

_b = tu.Turtle()
_b.speed(0)
_b.speed('fastest')

for n in range(3):
    go(_b, 100, 90)
    go(_b, 100, -90)

_c = tu.Turtle()
_c.shape('turtle')
_c.speed(1)
_c.color('blue','green')
_c.width(10)

for n in range(5):
    go(_c, 50, 90)
    go(_c, 50, -90)

tu.mainloop()
