print('\n'*10)

def xmas_tree_small(stack):
    """ DRILL - to make, small n stack X-mas tree- using PRINT FORMAT
  (1) .center() string function -
  (2) use For loop
  (3) stack can be varied.
    """

    """ #1. making STAR on the Tree TOP .....   """
    print('STAR'.center(31))
    print('BUCKS'.center(31))

    """ #2. making tree LEAVES BODY .....   """
    counter = 0
    for m in range(1, 1+(2*(stack-1))+1, 2):
        counter = counter + 1
        print(("*" * m).center(31), counter, " ..... n=", m)

    """ #3. making a tree TRUNK ....    """
    for k in range(3):
        print("|".center(31))

    """ #4. GROUND width = 31 ....    """
    print('M'*31)


if __name__ == '__main__':
    print(xmas_tree_small.__doc__)
    xmas_tree_small(10)
