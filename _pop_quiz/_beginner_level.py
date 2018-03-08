import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import _script_run_utf8
_script_run_utf8.main()

""" 문제. 0 ~ n 까지 input()을 받아서 더해라.
 # [IN]  몇까지 더할까요? : 100
 # [OUT] 정답은 5050 입니다
 """
def test_add_num():
    number = int(input('몇까지 더할까요? :'))
    total = 0
    for num in range(number+1):
        total += num
    print('정답은 {:} 입니다'.format(total))
# test_add_num()

""" 문제. 스윙스 헬로월드
 # 좌우로 0.2초 씩 움직이는 헬로월드를 만들어라
 # [OUT]
    |[HELL0]----------| WORLD!
    |----------[HELL0]| WORLD!
 """
import os
import time

def test_swing_hello():
    SIGN = "[HELLO]"

    def show_screen(start, stop, step):
        for left_num in range(start, stop, step):
            right_num = 10 - left_num

            left = '\n\n|' + '-' * left_num
            right = '-' * right_num + '| WORLD!'
            screen = left + SIGN + right

            print(screen, flush=True)
            time.sleep(0.2)
            os.system('cls')

    while 1:
        show_screen(0, 11, 1)
        show_screen(10,-1,-1)
# test_swing_hello()



def test_swing_hello2():
    kwargs = {
        'sleep' : 0.1,
        'length' : 15,
        'shape' : '.',
        'word' : 'HELLO',}

    args = [0.1, 15, '_', 'HELLO']

    def test2(sleep, length, shape, word):
        while True:
            a = 0
            for n in range(length, 0, -1):
                front = (shape * n)
                back = (shape * a)
                print('|' + front + '[' + word + ']' + back + '|' + ' WORLD!', flush=True)
                print('|' + back + '[' + word + ']' + front + '|' + ' WORLD!', flush=True)
                time.sleep(sleep)
                os.system('cls')
                a += 1
            a = 0
            n = 0

            for n in range(length, 0, -1):
                front = (shape * a)
                back = (shape * n)
                print('|' + front + '[' + word + ']' + back + '|' + ' WORLD!', flush=True)
                print('|' + back + '[' + word + ']' + front + '|' + ' WORLD!', flush=True)
                time.sleep(sleep)
                os.system('cls')
                a += 1

    test2(**kwargs)         # '리스트' 파라매터를 쓸 경우 : test2(*args)
test_swing_hello2()

""" 문제. 자료 3개의 딕셔너리() 키값, 밸류값을 프린트 해라.
 # [IN]  sample_dict = {1:'집', 2:'우산', 3:'자동차'}
 # [OUT]
    키값에는 1, 2, 3 = 3개의 자료가 있습니다.
    형식은 <class 'int'>, <class 'int'>, <class 'int'>, 입니다.

    밸류값에는 집, 우산, 자동차 = 3개의 자료가 있습니다.
    형식은 <class 'str'>, <class 'str'>, <class 'str'>, 입니다.
 """
def test_keys_values_dict():
    sample_dict = {1:'집', 2:'우산', 3:'자동차'}
    keys = list(sample_dict.keys())
    values = list(sample_dict.values())

    print("키값에는 {}, {}, {} = {}개의 자료가 있습니다.\n"
        "형식은 {}, {}, {}, 입니다.\n".format(
            keys[0],
            keys[1],
            keys[2],
            len(keys),
            type(keys[0]),
            type(keys[1]),
            type(keys[2])))

    print("밸류값에는 {}, {}, {} = {}개의 자료가 있습니다.\n"
        "형식은 {}, {}, {}, 입니다.".format(
            values[0],
            values[1],
            values[2],
            len(values),
            type(values[0]),
            type(values[1]),
            type(values[2])))
# test_keys_values_dict()

""" 문제. 포괄적 리스트 (comprehension List)형식 3개를 만들어라
 # 0 ~ 9 까지 int 리스트형 자료를 포괄적 리스트로 만들고 / 프린트
 # 1 ~ 10 까지 int '홀수형' 자료를 포괄적 리스트로 만들고 / 프린트
 # 1 ~ 10 까지 int 홀수만 'NG' str형 자료로 바꾸고 / 프린트
 # [OUT]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 4, 6, 8, 10]
    ['NG', 2, 'NG', 4, 'NG', 6, 'NG', 8, 'NG', 10]
 """
def test_comprehensive_list():
    print([n for n in range(10)])
    print([n for n in range(1, 11) if n%2==0])
    print([n if n%2==0 else 'NG' for n in range(1, 11)])
# test_comprehensive_list()
