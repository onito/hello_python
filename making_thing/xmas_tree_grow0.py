import _xmas_tree2 as xtr
import time


def clear():
    print('\n\n'*30)

def show_grow_tree(stack_num=7):
    for n in range(1, stack_num):
        xtr.show_stacked_body(0, 1+(2*n), 0)
        xtr.show_trunk(3)
        xtr.show_ground(60)

        time.sleep(1)
        clear()

def show_plain_xmas_tree():
    xtr.show_stars()
    xtr.show_stacked_body(0, 7, 0)
    xtr.show_stacked_body(3, 11, 0)
    xtr.show_stacked_body(7, 15, 0)
    xtr.show_stacked_body(11, 19, 0)
    xtr.show_trunk(6)
    xtr.show_ground(60)


while True:
    clear()
    show_grow_tree(7)
    xtr.xmas_tree_small(19, 0)

    time.sleep(3)
    clear()
    show_plain_xmas_tree()

    time.sleep(3)
    clear()

    import os
    import _xmas_tree3 as xtr3

    for n in range(15):
        print('\n\n\n'*9)
        xtr3.make_xmas_tree()
        time.sleep(1)
        os.system('cls')
