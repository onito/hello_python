import os
import random

NUM_RANGE = random.randint(10, 100)

def get_answer_input(message):       # OUT='str'
    return str(input(message))

def is_valid_answer(_answer, given_range):   # IN='str', 'int' / OUT='bool'
    """ Check if NUMERIC w/i given range  """
    print()

    if _answer.isnumeric():
        print('CHK=OK numeric!!')

        if int(_answer) >= 1 and int(_answer) <= given_range:
            print('CHK=OK... in range!!')
            return True

        else:
            print('CHK=NG... out of range Error...')
            return False
    else:
        print('CHK=NG... Not a Number Error...')
        return False

def get2_answer_n_checksum():     # OUT= 'int', 'bool'
    while True:
        msg_question = 'I have a number out of 1~%s.. GUESS!   :'% NUM_RANGE
        _answer = get_answer_input(msg_question)
        _checksum = is_valid_answer(_answer, NUM_RANGE)
        print('_____________________')
        print('The Answer is.... ', _answer)
        print('The CHECKSUM is....', _checksum)
        print('\n\n')

        if _checksum:
            return int(_answer), _checksum

def main_loop(_my_number):
    while True:
        _answer, _is_OK = get2_answer_n_checksum()              # get answer
        # print('chk = ', _answer, _is_OK )
        # print()

        if _answer > _my_number:
            print('ooooo')
            print('OOPS!.. The Guess is greater than my number..\n')

        elif _answer == _my_number:
            print('=====')
            print("Huh?.. BULL'S EYE!!!.. My number is... %s\n" %_my_number)
            break

        else:
            print('NO!!.. xxxxx')
            print('The The Guess is smaller than my number..\n')

def try_again_loop(_try_again):
    while True:
        if _try_again.lower() == 'y':
            os.system('cls')
            main()
        else:
            break




def main():
    _my_number = random.randint(1, NUM_RANGE)
    main_loop(_my_number)

    message = '\n\n\n\nTry again (y/n)??'
    _try_again = get_answer_input(message)         # 'str'
    try_again_loop(_try_again)

if __name__ == '__main__':
    main()
