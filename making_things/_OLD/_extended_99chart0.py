import os
import time

def _a_multiple_b(_a, _b):          #  IN= 2'int' / 'NO' OUT
    print('%2s x %2s = %2s'% (_a, _b, _c))

def _get_a_multiple_b(_a, _b):      # IN= 2'int' / OUT= 3'int'
    return _a, _b, (_a * _b)

def get_a_multiple_b(_a, _b):       # IN= 2'int' / OUT= 1'int' = FUNCTION
    return _a * _b



while True:
    for i in range(1, 100):
        for j in range(1, 20):



            _a = i
            _b = j
            print('',_a, 'x',  _b, '=', _a * _b)






            _a = i
            _b = j
            print('%2s x %2s = %2s'% (_a, _b, (_a * _b)))






            _a = i
            _b = j
            _c = _a * _b
            print('%2s x %2s = %2s'% (_a, _b, _c))







            _a = i
            _b = j
            print('%2s x %2s = %2s'%(
                _a,
                _b,
                _a * _b))






            # # ------------------ [ PAUSE for KEY-IN] ------------------------
            # try:
            #     input('Try Again? [Y="Enter"...]')
            # except:
            #     raise SystemExit
            # # ---------------------------------------------------------------
            # time.sleep(0.2)

            os.system('cls')
