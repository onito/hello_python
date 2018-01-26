import os
import time
import datetime
""" Refer : DATETIME module Documentation
  - format here : https://docs.python.org/2/library/datetime.html
  (1) datetime, time module
  (2) recursive functions - countdown, factorial, fibonacci(yield)
  (3) Graph Module : Turtle (by Tkinter)
"""
def test1_datetime_module():
    while True:
        _time = datetime.datetime.now() # '2017-12-03 10:06:59.241000'
        print(_time)
        print(type(_time),end='\n\n')  # <class 'datetime.datetime'>

        ampm = _time.strftime('%p')     # AM, PM
        hour = _time.strftime('%H')     # %H = 24, %I = 12 format.
        minute = _time.strftime('%M')   # 01
        second = _time.strftime('%S')   # 01
        weekday = _time.strftime('%A')  # MONDAY

        print(ampm + ' ' +
                hour + ' : '  +
                minute + ' : '  +
                second + ' - '  +
                weekday)
        _time_format = _time.strftime('%p %I:%M:%S - %A, %d. %B')
        print(_time_format)

        time.sleep(1)
        os.system('cls')
# test1_datetime_module()

""" countdown """
def countdown_normal(start_number):
    for n in range(start_number, -1, -1):
        print(n)
        time.sleep(0.2)
    print('Fire!')
# countdown_normal(10)

def countdown_recursive(start_number):
    """ RECURSIVE FUNCTION
      - call function (start_number -1)
    """
    if start_number >= 0:
        print(start_number)
        time.sleep(0.2)

        countdown_recursive(start_number-1)
    else:
        print('Fire!')
# countdown_recursive(10)

def get_factorial(number):
    """ FACTORIAL = 5! = 5 * 4* 3 * 2 * 1
    GF(3) = 3 * GF(2)
                2 * GF(1)
                     1
    there for, GF(4) = 4 * 3 * 2 * 1
    """
    if number != 1:
        return number * get_factorial(number-1)
    else:
        return 1
# _a = get_factorial(365)   # 1
# # _a = get_factorial(2)   # 2 * 1 = 2
# # _a = get_factorial(3)   #  3 * 2 * 1 = 6
# # _a = get_factorial(4)   # 4 * 3* 2 * 1 = 24
# print('{:,}'.format(_a), end='\n\n')

def show_factorial(number):
    _equation = str(number)
    _value = get_factorial(number)

    for i in range(number-1, 0, -1):
        _equation += ' x ' + str(i)
    print('{}! = {} = {:,}'.format(number, _equation, _value))
# show_factorial(365)

def get_fibonacci(times):
    if times > 1:
        a, b = 0, 1
        for n in range(times-1):
            a, b = b, a + b
        return b
    # """ Exceptional condition """
    elif times <= 1:
        # if times == 1, 0:
        return times
# _a = get_fibonacci(200)
# print('{:,}'.format(_a))

def show_fibonacci_golden_ratio(times):
    """
    GOLDEN RATIO = (1+math.sqrt(5))/2 = 1.618033988749895
    """
    for n in range(times):
        _a = get_fibonacci(n)
        if n <= 1:
            print('{:3}={:15,}, '.format(n, _a), end='\n')
        else:
            _a_n_1 = get_fibonacci(n-1)
            print('{:3}={:15,}, ---> ratio= {:} '.format(n, _a, _a/_a_n_1), end='\n')
show_fibonacci_golden_ratio(2000)

def fibonacci():
    """ (3) FIBONACCI GENERATOR(Yield) TEST
      - REFER HERE : https://goo.gl/J2EzIY
      - SOURCE: https://stackoverflow.com/
        ..questions/494594/how-to-write-the-fibonacci-sequence-in-python
    """
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1,(0 + 1)
# print(fibonacci())   # <generator object fibonacci at 0x02250690>
# print(type(fibonacci()))    # <class 'generator'>

def show_fibonacci_repeatation(until_times=10):
    for index, fibonacci_number in enumerate(fibonacci()):
        print('{i:3}: {f:.>10,}'.format(i=index, f=fibonacci_number))
        if index == until_times:
            break
# show_fibonacci_repeatation(30)

def test_graph_turtle():
    import turtle

    def turtle_go(go, left=0, right=0):
        turtle.forward(go)
        turtle.left(left)
        turtle.right(right)

    turtle.shape('turtle')

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle.forward(100)
    turtle.left(90)

    turtle_go(100, 0, 90)
    turtle_go(50, 0, 90)
    turtle_go(200, 90, 0)
    turtle_go(100, 0, 90)

    turtle.mainloop()
# test_graph_turtle()
