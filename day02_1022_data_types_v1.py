#! python
""" Day 02. DATA TYPE
 --------------------
 1. Number = int, float, 0b, 0h, 0o / Built-in funcs. / operators =..//, %
 2. String = str, chr, /Built-in funcs. / operators = +
 3. List type (array)      <-- (partially..) wraped up 'HERE' on Day.02
  ..........
 4. Tuple type - 튜플타입 (리스트의 불변버젼)
 5. Dict  type - 딕트타입 (딕셔너리:사전)
 6. Set   type - 집합타입 (합집합, 교집합, 차집합)
 7. Bool  type - 부울타입 (참, 거짓)
 8. Variables = Slicing, indexing etc. (변수저장, 슬라이싱, 인덱싱)
 """

""" (1) NUMBER type DATA """
def test1_number():
    _a = 100
    _b = 3

    _c = _a + _b    # = 103

    _d = _a / _b    # = 33.3333333      'float' = 'int' / 'int'
    _e = _a // _b   # = 33 'int'
    _f = _a % _b    # = 1   'int'

    print('_a / _b = ', _d)
    print('_a // _b =', _e)
    print('_a % _b =', _f)
    print()

    print('ABC', end='')
    print('ABC', end='')
    print('ABC', end='')
    print()

    print('ABC', end='\n\n\n')
    print('ABC', end='\n\n\n')
    print('ABC', end='\n\n\n')
    print()

    print('0b1111 =', bin(15))

    _a = '1.0'
    print(float(_a))
    print(type(_a))
# test1_number()

""" --- NUMBERS
 (1) INTEGER
 (2) FLOAT
 (3) Octa-decimal, Binary, Hexa-decimal
 """
def test1_types():
    a = 5.2                             # float
    b = 2                               # int
    c = a / b                           # float c=2.6

    print("FLOAT answer=" ,c)           # c=2.6
    print("INTEGER answer=" ,int(c))    # c=2

    d = int(c)
    print(d)           # d = int(2.6) = 2

    e = float(d)       # e = float(2) = 2.0
    print(e)

    print(0b_1110)     # 8+4+2+0 = 14
    print(0b_0111)     # 4+2+1 = 7
    print(0b_111)      # 0+4+2+1 = 7
    print(0b_111)      # 0+4+2+1 = 7
# test1_types()

""" --- OPERATORS
 + - / * = four essencial operaters
 %, **, //
 """
def test2_operators():
    # iterator (LOOP)
    print(7%7)              # 0
    print(7%6)              # 1
    print(7%5)              # 2
    print(7%4)              # 3
    print(7%3)              # 1
    print(7%2)              # 1
    print(7%1, end='\n\n')  # 0

    """ '%' drill : """
    for n in range(7, 0, -1):
        print('7 %% %s ='%n, 7%n)
    print()

    """ '//' drill """
    for n in range(10, 0, -1):
        print('10/{} = '.format(n), 10//n)
        # print('10/%s = '%n, 10//n)
    print()

    """ '**' drill """
    for n in range(1, 8, 1):
        print('%s ** 2 = '%n, n**2)
    print()
# test2_operators()

""" (2) TEXT type DATA : escape code + string operating """
def test3_text_basic():
    _a = """
          o  !    Baseball..!!
          --%
          |
         //
         !!
        """

    _b ='\a\n\t  o  !    Baseball..!!\n\t  --%\n\t  |\n\t //\n\t !!\n'
    print(_a)       # multi-line-string, to be bound with """
    print(_b)       # All the same!  -- one line --

    _a = "Python's favorite food is perl"
    _a = '\aPython\'s \\favorite food is perl'
    print(_a, end='\n\n')

    _a = "this"
    _b = " is a book"

    _c = (_a + _b + '\n')*5
    print(_c)
# test3_text_basic()

""" INDEXING (position) """
_a = "Life is too short, You need Python"

def test4_indexing():
    print(len(_a))     # 34
    print(_a[0])       #'L'
    print(_a[33])      #'n'
    print(_a[-1])      #'n'
# test4_indexing()

""" SLICING """
def test5_slicing():
    print(_a[0:4])          # (POS_start: POS_end+1) = 'Life'
    print(_a[28:34])        # Python
    print(_a[-6:])          # Python
    print(_a[:-6])          # Life is too short, You need
    print(len(_a[:-6]))     # 28

    _b = "Pithon"           # There's a misspell 'i', change it to 'y'
    _b = _b[:1] + "y" + _b[2:]
    print(_b)               # Python
# test5_slicing()

""" FORMATING : random selection drill /w list-DATA """
import random

def test6_formating(action_str):
    _who = ('I', 'You', 'he', 'she', 'your mom', 'my dog')
    _number = ('one', 'two', 'three', 'four', 'five', 'six', 'seven')
    _objects = ('apple(s)', 'banana(s)', 'grapes', 'man\'s nose(s)')

    for repeat in range(10):
        print("%s '%s' %s %s"% (
                    random.choice(_who),
                    action_str,
                    random.choice(_number),
                    random.choice(_objects)))
test6_formating('saw')
# test5_formating('ate')
# test5_formating('crushed')
