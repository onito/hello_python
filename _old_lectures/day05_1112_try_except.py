""" DAY.05 - (05-4) TRY EXCEPT /ELSE /FINALLY
 - Try:    normal condition
 - except: erroneous situation
 - else:   final filtred condition
 - finally:
 """
SEPARATOR = '\n' + '__'*20 + '\n\n\n'

def test1_when_input_string():
    while True:
        _a_str = input('input a string =')
        _b_str = input('input b string =')

        try:
            c = int(_a_str) * int(_b_str)
        except:
            print('Not Number', SEPARATOR)
            continue

        print(c, type(c),SEPARATOR)
# test1_when_input_string()

def test2_when_input_integer():
    while True:
        try:
            _a_int = int(input('input a integer ='))
            _b_int = int(input('input b integer ='))
        except ValueError:
            print('Input number only \n\n')
            continue
        print('SEE ME? O.K..!!\n\n')

        try:
            _answer = _a_int / _b_int
        except ZeroDivisionError:
            print('Cannot divide zero', SEPARATOR)
            continue

        except:
            pass

        else:
            pass

        finally:
            pass

        print('%s / %s = %s' %(_a_int, _b_int, _answer), SEPARATOR)
# test2_when_input_integer()


""" Built-in FUNCTIONS
 - enumerate, zip, map, lambda, chr, ord,
 - enumertate(iterator) = i, iterator
 - map(f(x), iterator)
 - zip(*iterables)
 - lambda = oneline function define w/o func_name
 - chr('int') <--> ord('str')
 - dir(), id(), help(), ..... etc
 """



""" Outter FUNCTIONS (module)
 - random, os, sys, time, datetime, pickle,
 """
