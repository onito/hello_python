#! python
""" Day 03. DATA TYPE - v2
 --------------------
 4. Tuple type - not changeable
 5. Dict  type - { keyd : values } combinations
 6. Set   type - union(), intersection(), difference()
 7. Bool  type - Which is True / False ??
 8. Variables = Slicing, Indexing etc. - what's the memory address ??
 """

""" (4) Tuple == List(array) """
def test1_tuple_test():
    _a_str ='abcdefg'
    print('ef' in _a_str)   # True
# test1_tuple_test()

""" What is the OBJECT? - individualy independant each things
  1. Class - (OOP) Object Oriented Programming  : 객체 지향형 파이썬
  2. Function - Functional Programming          : 함수형 파이썬
    - id()= check memory address,
    - dir()= check object's built-in functions
"""
def test2_object_test():
    print(id(3)) # 1813399216

    for command in dir('ABC'):
        print(command)

    _a = 3

    print(id(_a)) # 1813399216
    print(id(3))  # 1813399216

    _a = 4

    print(id(_a)) # 1723025088
    print(id(3))  # 1723025072

    print(id(4))  # 1723025088


    _a = 11111111
    _c = _a

    import sys

    print('ref number =', sys.getrefcount('jumping Jack flash'))
    print('ref number =', sys.getrefcount(11111111))# return 5, let's guess why
    print(sys.getrefcount.__doc__)          # shows function doc-string below..
    """   getrefcount(object) -> integer
Return the reference count of object.  The count returned is generally
one higher than you might expect, because it includes the (temporary)
reference as an argument to getrefcount().

getrefcount 는 객체(object)를 언급한 횟수를 int 값으로 반환합니다. 생각 했던 것
보다 +1을 더 반환 하는 것을 염두해 둬야 합니다. 최초 객체를 함수로 카운트하면 3을
반환(return) 하는데, 그것은 객체를 2번을 언급 했다는 사실입니다..
"""
# test2_object_test()

""" set function - union / intersection / defference
"""
def test3_set_test():
    _str_1 = 'hello'
    _s1_set = set(_str_1)
    print(_s1_set)              # {'h', 'o', 'l', 'e'}

    _str_2 = 'how are you'
    _s2_set = set(_str_2)
    print(_s2_set, '\n\n')      # {'o', 'u', 'e', 'y', 'h', 'r', 'a', ' ', 'w'}

    """ (1) Union() """
    union_ = _s1_set.union(_s2_set)
    print(len(union_), union_)  # 10 {'u', 'e', 'h', ' ', 'o', 'y', 'r', 'a', 'l', 'w'}

    """ (2) intersection() """
    inter_ = _s1_set.intersection(_s2_set)
    print(len(inter_), inter_)  # 3 {'h', 'o', 'e'}

    """ (3) Difference(s1 - s2) """
    differ_ = _s1_set.difference(_s2_set)
    print(len(differ_), differ_)# 1 {'l'}
# test3_set_test()
import random
import time
""" random function drill
 (1) random.randint()
 (2) random.choice()
 (3) random.shuffle()
 """
def test1_dirtest():
    print(dir(random))

    for n in dir(random):
        print(n)

def test2_randint():
    """ randint """
    for n in range(30):
        _a = random.randint(0, 10)
        print(_a)
# test2_randint()

def test3_randchoice():
    _a = random.choice('abcdefg')
    _a = random.choice([1, 2, 3, 4])
    # _a = random.choice({1:'a', 3:'b', 4:'c'}) # KeyError
    # _a = random.choice({'a':1, 'b':2, 'c':3}) # KeyError
    print(_a)
# test3_randchoice()

def test4_rand_shuffle():
    _a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    _a = [ n for n in range(10) if n/1 == n ]   # comprehension list.

    for n in range(10):
        random.shuffle(_a)
        print(_a)
# test4_rand_shuffle()

import random
import time
import os

def drill_bar_test():
    _a_str = '■'

    for n in range(10, 0, -1):      # (start, end+1, step)
        print(n, _a_str*n)
        time.sleep(0.5)
        os.system('cls')

    _b_format = """
    -----------------------------
      HP (Health)      : %3s points
      MP (Magic)       : %3s points
      LUCK (fortune)   : %3s %%
    _____________________________
    """
    _c = random.randint(1, 100)
    _d = random.randint(1, 100)
    _e = random.randint(1, 100)
    print(_b_format% (_c , _d, _e))
# drill_bar_test()

def show_10random_by(times):    # IN='int' / OUT=None
    for n in range(times):
        _a = random.randint(0,10)
        print('%2s times .... rand(1-10) = %-2s'% (n+1, _a))
    print()
    return _a
# show_10random_by(10)

def weired_number_guess():
    INTRODUCE = """
    어서 오라..용사 '%s' %s... !!

    컴퓨터가 1 ~ %s 숫자를 가지고 있습니다.
    10번 기회 안에 맞춰보세요.

    비밀번호 '13'을 누르면 탈출 할 수 있습니다\n\n.
    """
    user_name = input('너의 이름을 말하라....  : ')

    _looking_arr = ['잘생긴', '못생긴', '키작은', '이상한', '똑똑한', '배고픈' ]
    looking = random.choice(_looking_arr)

    limit = random.randint(10, 100)

    print(INTRODUCE % (looking, user_name, limit))
    comp_num = random.randint(1, limit)

    counter = 0
    winning_condition = ''

    while True:
        your_chances = 10 - counter

        _a_str = '■'
        print('남은 챤스 (%s) %s'% (your_chances, (_a_str * your_chances)))

        counter = counter + 1       # counter += 1
        _a_int = int(input("'%s' th Try..!! Guess numder = "% counter))
        # print(comp_num)

        if comp_num < _a_int:
            print('크다... \n\n')

        elif comp_num > _a_int:
            print('작다... \n\n')

        elif comp_num == _a_int:
            print('맞았다... \n\n')
            winning_condition = 'win'
            break

        if _a_int == 13:
            print('call ... Friday the 13th.--- OK You are OUT!!.. ')
            winning_condition = 'give-up'
            break
        time.sleep(0.5)

        if counter >= 10:
            print('...너의 기회는 다 되었다...')
            print("정답은 '%s' 이었다.." %comp_num)
            winning_condition = 'lose'
            break

    if winning_condition == 'win':
        print('이겼다..')
    elif winning_condition == 'lose':
        print('졌구나..')
    elif winning_condition == 'give-up':
        print('포기했냐?..')
    else:    # 혹시, 예외적 경우에는 에러를 강제로 발생시킴 (그럴 경우 없음)
        raise EnvironmentError

    # TRY-AGAIN? 은 어떻게 처리 할 수 있을까??
    # 인터넷에서 Geany Editor (window 64bit)를 설치하자 (geany.org)

weired_number_guess()
