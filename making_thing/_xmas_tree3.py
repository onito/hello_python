""" DRILL - to make, small 5 stack X-mas tree- PRINT FORMAT - X-mas Tree.
  1) .center() string function -
  2) Use For-loop properly -
  3) Stack can be varied by function arguments.
  4) Flash lights blinking by options below.

    - chance        : Mixed with 3 ornarments together.
    - stack_sort    : change ornarmants stack by stack.
    - ORNAMENT_SORT : select 1 ornarment on whole tree.
"""
import os
import time
import random

GROUND_WIDTH = 60
ORNAMENT_SORT = random.randint(0, 3)

def show_stars():
    print('★'.center(GROUND_WIDTH))
    print('STAR'.center(GROUND_WIDTH))
    print('BUCKS'.center(GROUND_WIDTH))

def show_stacked_body(start=0, stack=3, show_calc=0):
    """ Arguments Explanation
     - start = start number of stars on the layer
     - stack = number of stack layers
     - show_calc = 0:(False) w/o results, 1:(True)/w calc.restults

     Flash lights blinking ... by options below.
     - by chance        : Mixed with 3 ornarments together.
     - by stack_sort    : change ornarmants stack by stack.
     - by ORNAMENT_SORT : select 1 ornarment on whole tree.
     """
    stack_sort  = random.randint(0, 3)

    for n in range(start, stack):
        n_stars = 1 + (2*n)

        if show_calc:
            calc_result = str(n+1) + '...n_stars= ' + str(n_stars)
        else:
            calc_result = ''

        chance = random.randint(0, 10)
        star_body = ("-" * n_stars)

        if chance in [0,1,2,3,4,5,6,7,8,9,10]:
            for n in range(n_stars):
                pos = random.randint(0, n_stars-1)

                # chance%3 or stack_sort%3 or ORNAMENT_SORT%3
                if stack_sort%3 == 0:
                    ornaments = random.choice('_.^:;\'')    # _.^:;\'
                elif stack_sort%3 == 1:
                    ornaments = random.choice("abcdefghijklmnopqrstuvwxyz")    # _.^:;\'
                elif stack_sort%3 == 2:
                    ornaments = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")    # _.^:;\'

                star_body = star_body[:pos] + ornaments + star_body[pos+1:]

        line_print = star_body.center(GROUND_WIDTH) + calc_result
        print(line_print)

def show_trunk(height=2):
    """ height = stack height, default = 2 """
    for k in range(height):
        print("|".center(GROUND_WIDTH))

def show_ground(width=40):
    print('M'*width)
    print('Ground Width =', width)

def make_xmas_tree():
    """ Function DOC String : MAKING X-MAS TREE
  1) .center() string function -
  2) Use For-loop properly -
  3) Stack can be varied by function arguments.
  4) Flash lights blinking by options below.

    - chance        : Mixed with 3 ornarments together.
    - stack_sort    : change ornarmants stack by stack.
    - ORNAMENT_SORT : select 1 ornarment on whole tree.
    """

    """" #1. making STAR on the Tree TOP .....   """
    show_stars()

    """ #2. making tree LEAVES BODY .....   """
    show_stacked_body(0, 7, 0)
    show_stacked_body(3, 11, 0)
    show_stacked_body(7, 15, 0)
    show_stacked_body(11, 19, 0)

    """ #3. making a tree TRUNK ....    """
    show_trunk(6)

    """ #4. GROUND width $ ....    """
    show_ground(GROUND_WIDTH)


if __name__ == '__main__':
    import _xmas_tree3

    print(_xmas_tree3.make_xmas_tree.__doc__)
    print('\n'*1)

    ORNAMENT_SORT = 0
    make_xmas_tree()

    time.sleep(10)
    os.system('cls')

    while True:
        print('\n'*11)

        ORNAMENT_SORT = random.randint(0, 3)
        make_xmas_tree()

        print('\a')
        time.sleep(1)
        os.system('cls')
