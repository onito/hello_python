import math
""" function calculator """

def get_input_args():           # IN=x / OUT= 2'float', 1'int'
    """ get 3 inpits preventing break due to an Error """
    # When -- NORMAL
    try:
        _arg1 = float(input('a :  '))
        _arg2 = float(input('b :  '))
        _operand = int(input(' What? (1=+, 2= x..)'))
        return _arg1, _arg2, _operand

    # When -- ABNORMAL (ERROR OCCURES)
    except ValueError as e:
        print(e)
        _arg1 = _arg2 = 0
        _operand = 1
        return _arg1, _arg2, _operand

def get_plus_ab(a, b):          # IN= 2'int' / OUT= 1'int'
    """  return a+b while a = int, b = int """
    return a+b

def get_minus_ab(a, b):          # IN= 2'int' / OUT= 1'int'
    """  return a-b while a = int, b = int """
    return a-b


while True:
    # Input function -- called
    _arg1, _arg2, _operand = get_input_args()

    # Error check -- error_flag, on/off
    if _arg1 == 0 and _arg2 == 0 and _operand == 1:
        _error_flag = True
    else:
        _error_flag = False

    # choose operand type
    if _operand == 1:
        c = get_plus_ab(_arg1, _arg2)
        operand ='+'

    elif _operand == 2:
        c = get_minus_ab(_arg1, _arg2)
        operand ='-'

    else:
        _error_flag = True
        print('\n ???? Missing Operand ???? \n\n\n')

    # show result
    if not _error_flag:
        print('\n\t\t{} {} {} = {:,}\n\n'.format(_arg1, operand, _arg2, c))
    else:
        print('\n ???? IndexError ????\n\n\n')
