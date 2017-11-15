""" DRILL - to make, small 5 stack X-mas tree- PRINT FORMAT - X-mas Tree.
  (1) .center() string function -
  (2) use For loop
  (3) stack can be varied.

 1. Result of x-mas tree ( Width=31 )
              STAR
             BUCKS
               *                1  ..... n= 1
              ***               2  ..... n= 3
             *****              3  ..... n= 5
            *******             4  ..... n= 7
           *********            5  ..... n= 9
               |
 MMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
import os
import _xmas_tree1

_a = os.path.dirname(__file__)
_b = __file__

print(_a)
print(type(_a))

print(_b)
print(type(_b))


TREE_STACK = 15
GROUND_WIDTH = 60

print('\n'*20)

def show_stars():
    print('★'.center(GROUND_WIDTH))
    print('STAR'.center(GROUND_WIDTH))
    print('BUCKS'.center(GROUND_WIDTH))

def show_stacked_body(stack):
    counter = 0
    for n_stars in range(1, 1+(2*(stack-1))+1, 2):
        counter = counter + 1
        print(("*" * n_stars).center(GROUND_WIDTH))

def show_trunk(height=2):
    """ height = stack height, default = 2 """
    for k in range(height):
        print("|".center(GROUND_WIDTH))

def show_ground(gound_width):
    print('M'*gound_width)
    print('Ground Width =', gound_width)

def xmas_tree_small(stack):
    """ DOC String : MAKING X-MAS TREE
  (1) .center() string function -
  (2) use For loop
  (3) stack can be varied.
    """

    """" #1. making STAR on the Tree TOP .....   """
    show_stars()

    """ #2. making tree LEAVES BODY .....   """
    show_stacked_body(TREE_STACK)

    """ #3. making a tree TRUNK ....    """
    show_trunk()

    """ #4. GROUND width $ ....    """
    show_ground(GROUND_WIDTH)


if __name__ == '__main__':
    print(_xmas_tree1.xmas_tree_small.__doc__)

    show_stacked_body(3)
    show_stacked_body(5)
    show_stacked_body(7)
    show_stacked_body(9)

    print('\n\n\n\n')

    xmas_tree_small(TREE_STACK)
