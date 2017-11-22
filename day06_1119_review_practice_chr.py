import os
import sys
import time

import _script_run_utf8
""" This will help Script-RUN-package to run in UTF-8 encoding properly
in WINDOWS os system (between cp494 and utf-8).
: to set STDOUT & STDERR Unicode encoding, UTF-8 """
_script_run_utf8.main()

SEPARATOR = '\n' + '__'*30 + '\n\n'
NUM_ARR = [
    [
    '.ooooo.',
    'oo..oo.',
    'oo..oo.',
    'oo..oo.',
    'ooooo..',],
    [
    '..oo...',
    'oooo...',
    '..oo...',
    '..oo...',
    'oooooo.',],
    [
    '.ooooo.',
    'o...oo.',
    '..ooo..',
    'ooo....',
    'oooooo.',],
    [
    '.ooooo.',
    '....oo.',
    '.oooo..',
    '...ooo.',
    'ooooo..',],
    [
    '...oo..',
    '.oo.o..',
    'oo..o..',
    'oooooo.',
    '....o..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    'oo..oo.',
    '.oooo..',],
    [
    'oooooo.',
    'o...oo.',
    '...oo..',
    '..oo...',
    '.oo....',],
    [
    '.ooooo.',
    'oo..oo.',
    '.oooo..',
    'oo..oo.',
    '.oooo..',],
    [
    '.ooooo.',
    'oo...o.',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    ]


def show_number(number):
    """ show DIGIT being converted by Uniocde Symbols '■','∴' """
    for n in range(5):
        print(NUM_ARR[number][n].replace('o','■').replace('.','∴'))
        sys.stdout.flush()
# show_number(7)

def test1_count_down():
    """ COUNT DOWN : Using func. show_number() """
    for n in range(9,-1,-1):
        print('\n\n\n\n\n\n\n')
        show_number(n)
        time.sleep(0.5)
        os.system('cls')
test1_count_down()

""" Multi-line 'str'-type data """
_a =  '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..'''

_b =  '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..'''

def test2():
    _a_arr = _a.strip().split('\n')
    _b_arr = _b.strip().split('\n')

    print(_a_arr)
    print(_b_arr)

    _c_arr = []
    for n in range(5):
        _c_arr.append(_a_arr[n].strip() + _b_arr[n].strip())

    print(_c_arr)

    print('\n\n\n\n')
    for n in range(5):
        print(_c_arr[n].replace('o','■').replace('.','∴'))
# test2()

""" 'list' type data is much more effective to handle with """
_a = [
    ['.ooooo.', 'oo..oo.', 'oo..oo.', 'oo..oo.', 'ooooo..'],['.ooooo.',
    'oo...o.', 'oooooo.', '....oo.', 'ooooo..'], ['.ooooo..ooooo.', 'oo..oo.oo...o.',
    'oo..oo.oooooo.', 'oo..oo.....oo.','ooooo..ooooo..'],]

_b = [
    [
    '.ooooo.',
    'oo..oo.',
    'oo..oo.',
    'oo..oo.',
    'ooooo..'],
    [
    '.ooooo.',
    'oo...o.',
    'oooooo.',
    '....oo.',
    'ooooo..'],
    [
    '.ooooo..ooooo.',
    'oo..oo.oo...o.',
    'oo..oo.oooooo.',
    'oo..oo.....oo.',
    'ooooo..ooooo..']]

def show_nth_list(pos, change_flag=0):
    for n in range(5):
        if change_flag == 0:
            print(NUM_ARR[pos][n])
        else:
            print(NUM_ARR[pos][n].replace('o','■').replace('.','∴'))
    print(SEPARATOR)
# show_nth_list(0, change_flag=1)
# show_nth_list(1, change_flag=0)
# show_nth_list(2, change_flag=1)

def test3_show_3kind_lists():
    for n in range(3):
        print(_a[n])
    print(SEPARATOR)

    for n in range(5):
        print(_a[0][n])
    print(SEPARATOR)

    for n in range(5):
        print(_a[1][n])
    print(SEPARATOR)

    for n in range(5):
        print(_a[2][n])
    print(SEPARATOR)
# test3_show_3kind_lists()

def show_unicode_table_by_every_5000():
    # print(chr(97))
    # print(ord('a'))
    help(chr)
    print('{:,}'.format(0x10ffff))

    counter = 0
    for n in range(1, 1114111):
        counter += 1
        if counter <= 5000:
            pass
        else:
            time.sleep(10)
            counter = 0
        print('%3s:%s'%(n,chr(n)), '\t', end='')
# show_unicode_table_by_every_5000()


def test1_chr_ord():
    """ ASCii keyboard = 32 ~ 125
     - function CHR('int') <--> ORD('str')
    """
    print('a =', ord('a'))              # 97
    print('A =', ord('A'), SEPERATOR)   # 65

    print('chr(97) =', chr(97))
    print('chr(65) =', chr(65), SEPERATOR)
# test1_chr_ord()

def test2_ascii_table_1_to_n1(n1):
    counter = 0
    coulumn = 9
    for n in range(1, n1):
        counter += 1
        if 7 <= n <= 13 :
            if counter == coulumn:
                counter = 0
                print('%3s: %s\t' %(n,'..'), end='\n')
            else:
                print('%3s: %s\t' %(n,'..'), end='')
        else:
            if counter == coulumn:
                counter = 0
                print('%3s: %s\t' %(n,chr(n)), end='\n')
            else:
                print('%3s: %s\t' %(n,chr(n)), end='')
# test2_ascii_table_1_to_n1(411)

def show_menu_pan_just_test():
    """ MAKING MENU_PAN in YOUR RESTAURANT """

    MENU_DICT = {
        1 : ['BACK_NOODLE', 5000],
        2 : ['RED_NOODLE', 7000],
        3 : ['TTUK-BOK-KI', 3000],
        4 : ['SPRITE', 1000],
        5 : ['BOTTLED_WATER', 1000],
        }


    MENU_PAN_FORMAT = """
---------------------------------------
   MENU-PAN  / Onito's Restautant
---------------------------------------
%s
---------------------------------------"""

    # MENU_PAN_FORMAT = ""                            +\
    #     "---------------------------------------\n" +\
    #     "   MENU-PAN  / Onito's Restautant      \n" +\
    #     "---------------------------------------\n" +\
    #     "%s\n"                                      +\
    #     "---------------------------------------\n"

    MENU_STRING = ''
    for key in MENU_DICT.keys():
        # MENU_STRING += '%2s. %-15s ... %4s won' %(
        #     key,
        #     MENU_DICT[key][0],
        #     MENU_DICT[key][1]) + '\n'

        MENU_STRING += '{:>2}. {:<14} {:.^10} {:5,} won'.format(
            key,
            MENU_DICT[key][0],
            '.',
            MENU_DICT[key][1]) + '\n'

    print(MENU_STRING, SEPARATOR)

    print(MENU_PAN_FORMAT %MENU_STRING)
# show_menu_pan_just_test()
