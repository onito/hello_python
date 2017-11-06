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
import _xmas_tree2

TREE_STACK = 15
GROUND_WIDTH = 60

print('\n'*20)

def show_stars():
    print('★'.center(GROUND_WIDTH))
    print('STAR'.center(GROUND_WIDTH))
    print('BUCKS'.center(GROUND_WIDTH))

def show_stacked_body(start=1, stack=3, calc=0, star_str='*'):
    for n in range(start, stack):
        n_stars = 1 + (2*n)

        if calc:
            calc_result = str(n+1) + '...n_stars= ' + str(n_stars)
        else:
            calc_result = ''

        print((star_str * n_stars).center(GROUND_WIDTH), calc_result)

def show_trunk(height=2):
    """ height = stack height, default = 2 """
    for k in range(height):
        print("|".center(GROUND_WIDTH))

def show_ground(gound_width):
    print('M'*gound_width)
    print('Ground Width =', gound_width)

def xmas_tree_small(stack, calc=1):
    """ DOC String : MAKING X-MAS TREE
  (1) .center() string function -
  (2) use For loop
  (3) stack can be varied.
    """

    """" #1. making STAR on the Tree TOP .....   """
    show_stars()

    """ #2. making tree LEAVES BODY .....   """
    show_stacked_body(0, stack, calc)

    """ #3. making a tree TRUNK ....    """
    show_trunk(4)

    """ #4. GROUND width $ ....    """
    show_ground(GROUND_WIDTH)


if __name__ == '__main__':
    print(_xmas_tree2.xmas_tree_small.__doc__)

    show_stars()
    show_stacked_body(0, 7, 1, star_str='.')
    show_stacked_body(3, 11, 1, star_str='/')
    show_stacked_body(7, 15, calc=1, star_str='\\')
    show_stacked_body(11, 19, calc=1, star_str='=')

    show_trunk(3)
    show_ground(GROUND_WIDTH)
