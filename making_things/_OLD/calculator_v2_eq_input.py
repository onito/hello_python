import math
""" function calculator
 - input modified. """

def get_input_args():           # IN=x / OUT= 3'int
    """ get 3 inpits preventing break due to an Error """
    # When -- NORMAL
    command_arr = input("('num1' [+-*/] 'num2' = ) \n").strip().split()

    try:
        _arg1 = float(command_arr[0])
        _operand = command_arr[1]         # 'str'
        _arg2 = float(command_arr[2])
        return _arg1, _arg2, _operand

    # When -- ABNORMAL (ERROR OCCURES)
    except IndexError as e:
        print(e)
        _arg1 = _arg2 = 0
        _operand = '+'
        return _arg1, _arg2, _operand

def get_plus_ab(a, b):          # IN= 2 num / OUT= 1 num
    """  return a+b while a = int, b = int """
    return a+b

def get_minus_ab(a, b):          # IN= 2 num / OUT= 1 num
    """  return a-b while a = int, b = int """
    return a-b

def get_multi_ab(a, b):          # IN= 2 num / OUT= 1 num
    """  return a*b while a = int, b = int """
    return a*b

def get_divide_ab(a, b):          # IN= 2 num / OUT= 1 num
    """  return a/b while a = int, b = int """
    return a/b

def get_square_ab(a, b):          # IN= 2 num / OUT= 1 num
    """  return a*b while a = int, b = int """
    return a**b

def is_error(_arg1, _arg2, _operand):   # Out= True or False
    """ if exception, values are automatically assigned and return True """
    if _arg1 == 0 and _arg2 == 0 and _operand == '+':
        return True
    else:
        return False


while True:
    print("Input Command String Separate by spaces for each..")
    _arg1, _arg2, _operand = get_input_args()
    _error_flag = is_error(_arg1, _arg2, _operand)

    # print(get_plus_ab.__doc__)

    if _operand == '+':
        c = get_plus_ab(_arg1, _arg2)

    elif _operand == '-':
        c = get_minus_ab(_arg1, _arg2)

    elif _operand == '*':
        c = get_multi_ab(_arg1, _arg2)

    elif _operand == '/':
        c = get_divide_ab(_arg1, _arg2)

    elif _operand == '**':
        c = get_square_ab(_arg1, _arg2)

    else:
        _error_flag = True
        print('\n ???? Missing Operand ???? \n\n\n')

    # show result
    if not _error_flag:
        print('\n\t\t{} {} {} = {:,}\n\n'.format(_arg1, _operand, _arg2, c))
    else:
        print('\n ???? IndexError ????\n\n\n')
