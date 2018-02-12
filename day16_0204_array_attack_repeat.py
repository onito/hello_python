"""
화일 독스트링 : 화일의 설명 - 가위.바위.보 -모듈(블랙박스)
"""
import os
import random

""" 스크립트런(shift-ctrl-B)에서 한글출력이 가능하게 """
import _script_run_utf8
_script_run_utf8.main()

NUMBER_ATTACKS = 20                     # 게임횟수 20회
DECO_SEPARATOR = "=+" * 15
DRAW = ["-", "가위", "바위", "보ㅡ"]     # POS = 1,2,3 , POS'0'은 버린다.
RESULT = { 1: "승", 0: "패", -1 : "무"}  # 키값 = 1, 0, -1 로 호출한다.

def get_me_com_attacks(length=10):      # 기본횟수 = 10회
    """ 가위.바위.보 - 랜덤어택 리스트 갯수'length'만큼을 생성한다.
    # 예: 3개 = [(1,2), (2,3), (1,1)] ... length=3 : 튜플로 반환한다.
    """
    return [(random.randint(1, 3), random.randint(1,3)) for n in range(length)]

def get_result_rock_paper_scissors(me, com):
    """ 가위.바위.보의 승/무/패를 판단(judge)해 준다.
    # INPUT  = 1, 2, 3 중 하나, 가위,바위, 보 = me, com
    # OUTPUT = 1, 0,-1 중 하나 -- 승(True)/무(Except)/패(False)
    """
    eq = me - com       # 판단은 마이너스(나-컴)으로 판단한다
    if eq == 0:
        return -1       # 예외? = 무
    elif eq == 1 or eq == -2:
        return 1        # 1 (Ture) = 승
    elif eq == -1 or eq == 2:
        return 0        # 0 (False) = 패

def get_stack_win_draw_lose_count(judge, win_cnt, draw_cnt, lose_cnt):
    """ 입력: (judge)심판을 받아서, 승-무-패를 누적한다.
    # 승-무-패 카운트를 받아서, +1을 더한 후 다시 반환한다.
    """
    if judge == 1:
        win_cnt += 1
    elif judge == 0:
        lose_cnt += 1
    else:
        draw_cnt += 1
    return win_cnt, draw_cnt, lose_cnt

def is_stop_ok():
    """ Input값을 물어봐서,  'y'로 시작하면 True를 반환한다 / 아니면 False. """
    return input("\n그만 하시겠습니까? (Yes/No=Enter)").lower().startswith("y")



while True:
    """ 카운트 값 초기화 (0) """
    win_cnt, draw_cnt, lose_cnt = 0, 0, 0
    attacks = get_me_com_attacks(NUMBER_ATTACKS)

    """ 어택튜플에서 (me) 와 (com) 으로 숫자를 할당 받는다 """
    for i, (me, com) in enumerate(attacks, 1):
        judge = get_result_rock_paper_scissors(me, com)

        """ 심판(judge)값을 받아서, 승-무-패를 누적한다. """
        win_cnt, draw_cnt, lose_cnt = get_stack_win_draw_lose_count(
            judge, win_cnt, draw_cnt, lose_cnt)

        print("{:2}. {:>2} / {:>2} = {:>1}".format(
            i,              # 숫자
            DRAW[me],       # 가위-바위-보 한글로 보여 주기
            DRAW[com],      # 가위-바위-보 한글로 보여 주기
            RESULT[judge])) # 승/무/패 판정을 한글로 보여 주기

    print("\n" +DECO_SEPARATOR+ "\n{1:}승, {2:}무, {3:}패 --- {0:}전".format(
        i,
        win_cnt,    # 누적 승
        draw_cnt,   # 누적 무
        lose_cnt))  # 누적 패


    if is_stop_ok(): # 그만할까요?가 'y' 면 True를 반환한다.
        break        # 그러면 그만둔다 (빠져나온다)

    os.system('cls') # 화면을 지우고, 다시 시작한다.

# TODO : 리스트s
"""
(1) 파이썬 언어 기능연습
 - 포괄적 리스트 작성연습 / 튜플 언패킹 활용
 - 시퀸스 안에 있나? in / 기타 내장 함수 들
 - for 리스트s 사용규칙 / 논리곱,합 간단하게 쓰기
 - 루프ans 탈출하기 : pass, continue, break
 - PEP8 스타일가이드 및 Static 룰체크=Spyder3

(2) 프로그래밍 실습
 - 매서드의 활용 : 블박화 (모듈 재활용 하기 : _script_run_utf8 )
 - 함수명 동사화 = get_, show_, make_, set/remove_, init_, run_, is_
 - 가위-바위-보 = 연속 이길 확률은 (10번, 20번)
"""

# 내장함수(반제품) = filter(function, itor)
# >>> def positive(x):
#         return x > 0
# >>> list(filter(positive, [1, -3, 2, 0, -5, 6])))
#
# >>> filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])
# <filter object at 0x000002ED60CBFF98>

"""
# (1) 생각 해보기 - 내장함수, filter(), lambda
>>> print(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
<filter object at 0x000002ED60D17F28>

>>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
[1, 2, 6]

>>> lambda x: x > 0, [1, -3, 2, 0, -5, 6]
(<function <lambda> at 0x000002ED60331E18>, [1, -3, 2, 0, -5, 6])

>>> map(lambda x: x > 0, [1, -3, 2, 0, -5, 6])
<map object at 0x000002ED60D17EB8>

>>> list(map(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
[True, False, True, False, False, True]

>>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
[1, 2, 6]
"""
