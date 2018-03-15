""" 주로 사용 되는 비중이 높은, 모듈 들 """
# time, tys, randome, os, pickle.. eTC

import os
import sys
import time
import pickle
import random
import copy
import inspect

from tkinter import *
from tkinter import messagebox

BASE = "hello_python\\"
DIRS = os.path.dirname(__file__).partition(BASE)
ROOT = DIRS[0] + DIRS[1]


# ------------ Copy() -----------------------------
_="""_dict = inspect.currentframe().f_back.f_locals
 - 클래스와 관련된 모든 정보가 담긴 'dict'를 반환 한다.
 - 필요에 따라서 골라 쓰면 됨.
"""

import copy
import inspect


class Animal(object):

    def __init__(self, kind, legs, color):
        self.kind = kind
        self.legs = legs
        self.color = color

    def get_my_name(self):
        """ Using Animal CLASS() ---
         find instances NAME = more_animals[x].get_my_name()[0]
         refer to : https://goo.gl/3T8hrw = Stack Over Flow.
         """
        answer = []

        frame = inspect.currentframe()
        # print(frame)                    # frame object at 0x...e08
        # print(frame.f_back)             # frame object at 0x...b88
        # print(frame.f_back.f_locals)    # dict = {inst_name: __main__}

        # 'dict' ... + frame.f_globals.items()= ERR
        keys = inspect.currentframe().f_back.f_locals.keys()     # inst_name
        values = inspect.currentframe().f_back.f_locals.values() # __main__
        items = inspect.currentframe().f_back.f_locals.items()
        # print(list(keys))
        # print(list(values))

        for key, value in items:                        # inst_name : __main__
            if isinstance(value, self.__class__):
                if hash(self) == hash(value):
                    answer.append(key)
        return answer

def copy_show():
    print('\n'+_)
    harry = Animal('hippogriff', 6, 'pink')
    carrie = Animal('chimera', 4, 'green polka dots')
    billy = Animal('bogill', 0, 'paisley')

    # COPY: 'Harry' --> 'Harriet'
    harriet = copy.copy(harry)
    print("(1) Harry   = %s"% harry.kind)                   # hippogriff
    print("(2) Harriet = %s"% harriet.kind, end='\n\n')     # hippogriff

    print(harry.get_my_name())                              # ['harry']
    print(carrie.get_my_name())                             # ['carrie']
    print(billy.get_my_name())                              # ['billy']
    print(harriet.get_my_name())                            # ['harriet']

    # New Tuple group is created as My_Animal
    my_animals = [harry, carrie, billy, harriet]     # 변수가 아닌 '인스턴스'

    # New Tuple Data were created as More_Animal
    more_animals = copy.copy(my_animals)

    """
    for animal in my_animals:
        print(animal)         # <__main__.Animal object at 0x000001C3BB41C0F0>

    for animal in more_animals:
        print(animal.get_my_name()[0])             # <class '__main__.Animal'>
    """

    print("\nGroup of more_animals().kind)")
    print("-----------------------------")

    for x in range(len(more_animals)):      # for x in more_animals: => Error
        print("  %s) %-7s = %-8s" % (
            x + 1,
            more_animals[x].get_my_name()[0],       # [0]NAME, [1]CLASS
            more_animals[x].kind))

    # print(type(harry).__name__)             # find class name from instance
    # print(harry.__class__.__name__)         # all the same above. = 'Animal'
# copy_show()

# ------------- TIME() = Sh0w Time and TIME_Format
def time_show():
    print("(1) ASCtime NOW =  ", time.asctime(), "\n")
    t = (2017, 3, 9, 11, 45, 57, 5, 0, 0)

    print("(2) ASCtime(t) =   ", time.asctime(t))
    print("    t=", t, end="\n\n")
    print("(3) SHOW time.localtime(NOW) = \n", time.localtime(), "\n")

    t = time.localtime()        # declair Class
    year = t[0]
    month = t[1]
    print("(4) DIV localtime(NOW) [year=0],[month=1]=", year, month)
# time_show()


def time_elapse():
    t1 = time.time()            # secs from 1979. 1/1 .... SET(t1)
    for x in range(9):
        print(x + 1, end="\n")
        time.sleep(1)
    t2 = time.time()            # secs from 1979. 1/1 .... SET(t2)
    print("elapsed time =", t2 - t1)
# time_elapse()

# ------------ PICKLE() : Dump & Load for Data


def pickle_show():
    game_data = {
        'Player_POS': 'N23 E45',
        'Pockets': ['Keys', 'Pocket knife', 'Polished stone', 'Coins'],
        'BackPack': ['Rope', 'Hammer', 'Apple', 'Map', 'Lantern', 'Blanket'],
        'Inventory': ['-'] * 5,
        'Money': 158.50
    }

    save_file = open('./data/pickle_save.dat', 'wb')     # Write Binary module
    pickle.dump(game_data, save_file)         # Put(dump) game_data to file
    save_file.close()

    load_file = open('./data/pickle_save.dat', 'rb')     # Read Binary module
    # Put (load) loaded_file to var.
    loaded_file = pickle.load(load_file)
    load_file.close()

    # Pickle.dump or load       # Load & save_file (Open & Close)
    print(loaded_file)
# pickle_show()

# ----- SYS() : sys.stdin.readline() ...  annswer =input("message")


def sys_show():
    answer = input("Input Your Message : Input() = ")
    print(answer, "\n")
    print("Letters =", len(answer))           # TEXT format and Slicing TEST

    # sys.stdin.readline() = input()과 동일
    print("\nInput Your Message : Sys.stdin.readline")
    print("Your whole Message=", sys.stdin.readline())

    # sys.stdin.readline(int)
    print("Input Your Message : Sys.stdin.readline ( > 5 letters) :")
    print("Your first 5 Letter :", sys.stdin.readline(5))

    # sys.stdout.write('Str')
    print(sys.stdout.write("\nstdout.write = Where's the Carmen in San Diago? "))

    # sys.exit('메시지')
    print("\nPython Version =", sys.version, "\n")    # Py3 Version
    sys.exit("\nProgram's terminated")              # Sys.exit()
# sys_show()

# ------------ RANDOME()--------------------------


def random_show():
    print("(1) Print rand(Loop) =  ", end=" ")
    for i in range(10):
        v = random.randint(1, 10 + 1)
        print(v, end=",")            # continuous print = (end=" ")

    ansTuple = [random.randint(1, 11) for n in range(10)]
    print("\n(2) Print Tuple[rand] = ", ansTuple)

    random.shuffle(ansTuple)
    print("(3) Random Shuffling =  ", ansTuple)
    print("(4) Randomly Picked NUM=", random.choice(ansTuple))
# random_show()

# ------------ Tkinter ---------------------------


def hello_callback():
    # 버튼을 누르면, 활성화(call-back) 되는 메시지 창
    head = "HEAD : Hello Python 3.6 World"
    cntx = "CONTEXT : This is Practice for Message Box\n"+\
        "   You will never be satisfied with this \n"+\
        "   This is a only a example"
    return messagebox.showinfo(head, cntx)


def tkinter_show():
    """ TkInter 모듈은 '튜토리얼포인트' 싸이트 샘플을 참조!
     - http://www.tutorialspoint.com 사이트 한정으로 구글검색
    """
    tk = Tk()           # tk 는 Tk()...ToolKit'클래스'의 '인스턴스'다... 선언!
    # canvas 는 Canvas() '클래스'의 '인스턴스'다... 선언!
    canvas = Canvas(tk, width=640, height=500, bd=3, highlightthickness=0)

    """ 파라매터 선언 """
    tk.title("HELLO TkInter WORLD~!!(640 x 500)")  # Header
    tk.resizable(0, 0)                   # resize's not allowed (=0)
    tk.wm_attributes("-topmost", 1)      # Always on top

    """ 'ball' 오브젝트(인스턴스) 생성 """
    # canvas.create_oval(x1, y1 ,x2 ,y2, fill='red')... 기준점 = (기본): NW
    ball = canvas.create_oval(0, 0, 40, 40, fill='red')  # make Ball.object
    canvas.move(ball, 450, 300)     	  		         # move to canvas_center

    # draw POLY: see this 'tutorialspoint' = https://goo.gl/x1qck2
    points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
    poly = canvas.create_polygon(
        *points, fill='yellow', outline='black', width='3')
    canvas.move(poly, 450, 300)

    # 포토 이미지 오브젝트(클래스/인스턴스)를 생성한다.
    aaa = PhotoImage(file=ROOT + '_static/_img/Felix.png')
    bbb = PhotoImage(file=ROOT + '_static/_img/Felix_munch.png')
    ccc = PhotoImage(file=ROOT + '_static/_img/Felix_dizzy.png')

    # aaa can't be changed as Direct use
    canvas.create_image(120, 200, image=aaa, anchor='nw')
    canvas.create_image(0, 0, image=bbb, anchor='nw')
    canvas.create_image(350, 50, image=ccc, anchor='nw')

    B = Button(tk, text=" Comm'n man, take it easy! ",
               command=hello_callback)   # TK_window Button(Text)
    B.place(x=200, y=10)

    canvas.pack()                       # Draw Window
    tk.mainloop()                       # Keep screen turn on. -- makeing a loop. '''
tkinter_show()           # Felix the CAT images on Board
