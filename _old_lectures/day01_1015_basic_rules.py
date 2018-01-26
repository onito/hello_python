#! python
""" Python Coding Convention : PEP-8 (Python Enhanced Proposal)
  --------------------
  1. fname, vari =  start /w _, a (_=temp, __=Built-in func), B(x), 1(x), &(x)
  2. 1-line = within 80 charactors, (= recommand)
  3. Indent = (don't tab, but 4 spaces), Atom-TAB=4 Spaces, DON'T mix-use these
  4. Spaces btw '=','+', but don't with '(',
  5. 1-line blank /w def, 2-line blanks /w class
  6. def_name = snake type, class_name = pascal type    .... etc.
  """
def test1_various():   # c = a + b print(a)
    """  DOC String : c = a + b : variable assignment """
    _a = 300
    _b = 333
    _c = _a * _b

    print(_c)                       # 99900
    print('{:,}'.format(_c))        # 99,900
    print()
# test1_various()

""" Indentation Drill : 4 spaces  or 1 Tab in 'Atom-TAB', "DON'T" mix-use
"""
def test2_for_loop():   # pring 5 times - HELLO PYTHON, END
    """ (1) ---- FOR LOOP ---- """
    counter = 0
    for i in range(5):              # 0,1,2,3,4  .... n=4
        counter = counter + 1
        print(counter,'HELLO PYTHON')

    print('END')

def t_in_t():                       # Test in Test : other for-loop
    for n in range(0, 11, 3):       # range(start='0', end+1, step='1')
        print(n)
# test2_for_loop()
# t_in_t()

def test3_if_state(arg_n):   # if n = 4?
    """ (2) ---- IF STATE ----
    Func, Arg.'arg_n'=int, judge whether big/small/even than INPUT Arg.
    """
    _compare = 4

    if arg_n > _compare:
        print('ooooo')
        print('Yes!.. The Arg. is greater than 4..')

    elif arg_n == _compare:
        print('=====')
        print('Huh?.. The Arg. is even to 4..')

    else:
        print('No!!.. xxxxx')
        print('The Arg. is less than 4..')

    print('END', end="\n\n")
    print('Because, n=', arg_n)
# print(test3_if_state.__doc__)
# test3_if_state(4)

def test4_while_state(limit):
    # counter = 0
    # number = 0
    # string = '0'
    # counter, number = 0, 0
    counter = number = 0
    string = '0'

    while True:
        counter = counter + 1
        number = number + (counter*1)
        string = string + (' + ' + str(counter))
        if counter >= limit :
            break

    return number, string

def test4_main():
    _a, _string  = test4_while_state(10)
    print(_string, ' = ', _a)
# test4_main()

""" FUNCTIONS : def(define) - call(execute) """
# (1) Typical 'FUNCTION' definition
def a_add_b(a, b):          #
    c = a + b
    return c

# (2) typical 'METHOD' definition
def _a_add_b(a, b):         #
    c = a + b
    print(c)

def call_test():
    """ (1) CALL : Receive use """
    _a = a_add_b(5,9)       # Have to assign to Receiver '_a'
    print('_a =', _a)

    print('a_add_b(5,9)=', a_add_b(5,9))    # When without Reciever

    """ (2) CALL : Direct use"""
    _a_add_b(5,9)

    """ Over all test"""
    _a_add_b                # FUNC(Method) BODY(OBJECT) - w/o brackets
    print('_a_add_b (function body)=', _a_add_b)

    _a_add_b(3, 4)

    answer = a_add_b(3, 4)  # vari. assignment --> point out MEM.Address
    print('answer=', answer)
# call_test()

""" DRILL - to make, small 5 stack X-mas tree- PRINT FORMAT - X-mas Tree.
  (1) .center() string function -
  (2) use For loop
  (3) stack can be varied.

 1. Result of x-mas tree ( Width=31 )
              STAR
             BUCKS
               *                1  ..... n of stars= 1
              ***               2  ..... n of stars= 3
             *****              3  ..... n of stars= 5
            *******             4  ..... n of stars= 7
           *********            5  ..... n of stars= 9
               |
 MMMMMMMMMMMMMMMMMMMMMMMMMMM """
def hints_xmas_tree():
    """ ---- Xmas Tree Hint !! ----- """
    print('       *        ')
    print(" "*30 + "*" + " "*30)
    print('dddddddddd'.center(31))
    print(('b' * 10).center(31))
# hints_xmas_tree()

def xmas_tree_small(stack):
    """ DOC String : MAKING X-MAS TREE
  (1) .center() string function -
  (2) use For-loop
  (3) stack can be varied (controled by INPUT Vari.)
    """

    """ # making STAR on the Tree TOP .....   """
    print('★'.center(31))
    print('STAR'.center(31))
    print('BUCKS'.center(31))

    """ # making tree LEAVES BODY : n stack of tree .....   """
    num = 0

    start = 1                       # start numbers of '*'
    end = 1+(2*(stack-1))           # finall numbers of '*' depend on stack!
    step = 2                        # 1, 3, 5, 7... (every +2 steps)
    for n_stars in range(start, end+1, step): # (start, end+1, step)
        num = num + 1
        print(("*" * n_stars).center(31), num, " ..... n_*=", n_stars)
        # print(" "*(15-m), '*'*(2*m-1))

    """ # making a tree TRUNK ....    """
    for n in range(3):
        print("|".center(31))

    """ # GROUND width = 31 ....    """
    print('M'*31)
# xmas_tree_small(16)

def main():
    if __name__ == '__main__':
        print(xmas_tree_small.__doc__)
        xmas_tree_small(11)
main()
