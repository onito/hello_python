import os
import time

def show_a_multiple_b(_a, _b):      #  IN= 2'int' / Out= None.. just show
    """ Typical Method """
    print('%2s x %2s = %2s'% (_a, _b, (_a*_b)))

def _get_a_multiple_b(_a, _b):      # IN= 2'int' / OUT= 3'int'
    """ Typical function, returns 'OUTPUT'  """
    return _a, _b, (_a * _b)

def get_a_multiple_b(_a, _b):       # IN= 2'int' / OUT= 1'int'
    """ Typical function : doc-string describes roll, variables """
    return _a * _b

def get_comma_num(num):             # In='int'_num / Out='str'_num
    """ Take w/i 10**12, insert commas in it, returns 'str'value """
    if num <= 999:
        num_comma = str(num)

    elif num > 999 and num <= 999_999:
        num_comma = str(num)[:-3] + ',' + str(num)[-3:]

    elif num > 999_999 and num <= 999_999_999:
        num_comma = str(num)[-9:-6] + ',' +\
             str(num)[-6:-3] + ',' +\
             str(num)[-3:]

    elif num > 999_999_999 and num <= 999_999_999_999:
        num_comma = str(num)[-12:-9] + ',' +\
             str(num)[-9:-6] + ',' +\
             str(num)[-6:-3] + ',' +\
             str(num)[-3:]
    return num_comma

while True:
    for _a in range(100, 90000, 777):
        for _b in range(876543, 900000, 777):

            print(_a, 'x',  _b, '=', _a * _b)
            print('%2s x %2s = %2s'% (_a, _b, (_a * _b)))
            print('%2s x %2s = %2s'%(
                            _a,
                            _b,
                            _a * _b))

            show_a_multiple_b(_a, _b)

            _c = _get_a_multiple_b(_a, _b)
            print('?????.... %2s x %2s = %2s'% (_a, _b, _c))
            # unwanted result

            _c = _get_a_multiple_b(_a, _b)
            print('correct.. %2s x %2s = %2s'% (_c[0], _c[1], _c[2]))
            # correction - bothersome!!

            """
            ?????.... 100 x 876543 = (100, 876543, 87654300)
            correct.. 100 x 876543 = 87654300
            """

            _c = get_a_multiple_b(_a, _b)
            print('%2s x %2s = %2s'% (_a, _b, _c))


            """ Insert digit-comma, using str.format() """
            _c = (_a * _b)
            print('{:,} x {:,} = {:,}'.format(_a, _b, _c))



            """ Insert digit-comma, manually like below """
            _c = (_a * _b)
            # if _c <= 999:
            #     _c = str(_c)
            #
            # elif _c > 999 and _c <= 999_999:
            #     _c = str(_c)[:-3] + ',' + str(_c)[-3:]
            #
            # elif _c > 999_999 and _c <= 999_999_999:
            #     _c = str(_c)[-9:-6] + ',' +\
            #          str(_c)[-6:-3] + ',' +\
            #          str(_c)[-3:]
            #
            # elif _c > 999_999_999 and _c <= 999_999_999_999:
            #     _c = str(_c)[-12:-9] + ',' +\
            #          str(_c)[-9:-6] + ',' +\
            #          str(_c)[-6:-3] + ',' +\
            #          str(_c)[-3:]

            _c_comma = get_comma_num(_c)
            print('%s x %s = %s'%( _a, _b, _c_comma))

            # # ------------------ [ PAUSE for KEY-IN] ------------------------
            # try:
            #     input('Try Again? [Y="Enter"...]')
            # except:
            #     raise SystemExit
            # # ---------------------------------------------------------------
            # time.sleep(0.2)

            os.system('cls')
