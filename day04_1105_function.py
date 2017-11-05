import math
""" function calculator """

def get_input_args():       # IN=X / OUT= 2'float', 1'int'
    """ return 2'float', 1'int' """
    # WHEN -- NORMAL
    try:
        _arg1 = float(input('a :  '))
        _arg2 = float(input('b :  '))
        _kind = int(input(' What? (1=+, 2= x..)'))
        return _arg1, _arg2, _kind
    # WHEN -- ABNORMAL (ERROR)
    except ValueError as e:
        print(e)
        _arg1 = _arg2 = _kind = 1
        return _arg1, _arg2, _kind

def get_plus_ab(a, b):          # IN= 2'int' / OUT= 1'foat'
    """ a = float, b = float / retrun a, b, a+b """
    return float(a+b)

def get_minus_ab(a, b):          # IN= 2'int' / OUT= 1'foat'
    """ a = float, b = float / retrun a, b, a-b """
    return float(a-b)

def get_multiple_ab(a, b):          # IN= 2'int' / OUT= 1'foat'
    """ a = float, b = float / retrun a, b, a*b """
    return float(a*b)

def get_divide_ab(a, b):          # IN= 2'int' / OUT= 1'foat'
    """ a = float, b = float / retrun a, b, a/b """
    return float(a/b)


while True:
    _num1, _num2, _kind = get_input_args()

    if _kind == 1:                              # plus mode
        answer = get_plus_ab(_num1, _num2)
        doc = get_plus_ab.__doc__
        operator ='+'

    elif _kind == 2:                              # minus mode
        answer = get_minus_ab(_num1, _num2)
        doc = get_minus_ab.__doc__
        operator ='-'

    elif _kind == 3:                              # multiple mode
        answer = get_multiple_ab(_num1, _num2)
        doc = get_multiple_ab.__doc__
        operator ='x'

    elif _kind == 4:                              # divide mode
        answer = get_divide_ab(_num1, _num2)
        doc = get_divide_ab.__doc__
        operator ='/'

    print('explanation :', doc)
    print('\n\t\t{:,} {} {:,} = {:,.3f}'.format(
                _num1, operator, _num2, answer,))
