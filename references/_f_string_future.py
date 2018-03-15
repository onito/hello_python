""" Python3.6 add f-string :
 - article = The new f-strings in Python 3.6
   Hurray! It’s Christmas time - and Python 3.6 has been released!
   : https://cito.github.io/blog/f-strings/
"""
answer = 'PYTHON'
_from, _now = 1991, 2018
print(f"'{answer}' is the answer, its age of {_now - _from} years..")
print('----------------------')


# 파이썬에서 코드 실행시간 측정하기 (timeit)
# https://juliahwang.kr/algorism/python/2017/09/12/파이썬코드실행시간측정하기.html
import timeit

formats = [
"""
def format(name, age):
    return f'He said his name is {name} and he is {age} years old.'
""",
"""
def format(name, age):
    return 'He said his name is %s and he is %s years old.' % (name, age)
""",
"""
def format(name, age):
    return 'He said his name is ' + name + ' and he is ' + str(
        age) + ' years old.'
""",
"""
def format(name, age):
    return 'He said his name is {} and he is {} years old.'.format(name, age)
""",
"""
from string import Template

template = Template('He said his name is $name and he is $age years old.')

def format(name, age):
    return template.substitute(name=name, age=age)
""",
]

test = """
def test():
    for name in ('Fred', 'Barney', 'Gary', 'Rock', 'Perry', 'Jackie'):
        for age in range (20, 200):
            format(name, age)
"""

TITLE = [
    'f-strings  =',
    '%-format   =',
    '+ operand  =',
    '.format()  =',
    'template() =',
    ]

for i, _format in enumerate(formats):
    print("{}. {} {:2.5f} sec.".format(
        i+1,
        TITLE[i],
        timeit.timeit('test()', _format + test, number=10000)))



"""
'PYTHON' is the answer, its age of 27 years..
----------------------
1. f-strings  = 7.93894 sec.
2. %-format   = 8.19734 sec.
3. + operand  = 11.02691 sec.
4. .format()  = 13.30449 sec.
5. template() = 78.62707 sec.

Process returned 0 (0x0)        execution time : 119.293 s
계속하려면 아무 키나 누르십시오 . . .
"""
