import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import _script_run_utf8
_script_run_utf8.main()

""" 문제. 1 ~ 30 까지 출력하는 프로그램
# 3의 배수에서는 "에취!!!" / 5의 배수에서는 "쿨럭~~~"을 출력한다(for-loop:사용금지)
# 3과 5의 배수에서는 "딸꾹!딸꾹!"을 출력한다. / 시간지연=0.2초
# [OUT] : 숫자 하나씩 아래로 출력한다
"""
def test_acho_hicop():
    import time
    to_number = 30
    count = 0

    while count < 30:
        count += 1
        if count%3 == 0 and count%5 == 0:
            print("딸꾹!딸꾹!", flush=True)
        elif count%3 == 0:
            print("에취!!!", flush=True)
        elif count%5 == 0:
            print("쿨럭~~~", flush=True)
        else:
            print(count, flush=True)
        time.sleep(0.5)
test_acho_hicop()


""" 문제. A-1 편의점 물건을 계산하라
# 편의점 카운터에서 물건코드를 숫자(int)을 입력받은 후 최종가격을 알려주는 SW
# 가격DB는 3개만 딕셔너리 / 손님은 'item-갯수' 1-1 2-1 3-1 spc구분으로 입력
# 가장 심플한 영수증을 출력한다. (단, input구문은 테스트 CASE로 처리할 것!)
# input_str = input("번호-수량(공백)으로 입력 :")
# input_str = "1-1 2-2 3-1"
    빵ㅡ   : 1 x 1,000 = 1,000
    우유   : 4 x 2,000 = 8,000
    계란   : 1 x   500 =   500
    ------------ 합계: 9,500원
"""
PRICE_DICT = {
    1: ("빵ㅡ", 1000),
    2: ("우유", 2000),
    3: ("계란", 500)}
def test_convinient_store():
    # input_str = input("번호-수량(공백)으로 입력하세요 :/n) # 원래 입력값 할당
    input_str = "1-1 2-4 3-1"                              # 테스트용 변수할당.
    input_arr = input_str.strip().split()
    total_sum = 0
    for bundle in input_arr:
        item_price_tup = bundle.split('-')
        key = int(item_price_tup[0])
        quantity = int(item_price_tup[1])

        print("{0:4s} :{2:2d} x {1:5,} = {3:5,}".format(
            PRICE_DICT[key][0],                 # 이름 = '빵'
            PRICE_DICT[key][1],                 # 가격 = 1000
            quantity,                           # 갯수 = 1
            quantity * PRICE_DICT[key][1])      # 합계 = 1000
            )
        total_sum += quantity * PRICE_DICT[key][1]
    print("------------ 합계: {:5,}원".format(total_sum))
# test_convinient_store()


""" 문제. A-2 (1+1)할인 기간을 반영하라 (할인모드1)
# 평상 시에는 일반적인 편의점 계산 영수증 --> (A-1 코드 '복+붙' 후 수정)
# sale_mode = 1 일때는, 2개 사면 1개 더 주는 이벤트 모드 돌입 (2+1)
# 영수증 가격 옆에 (+'n'개 더!)만 추가로 반영한다. / 항목에 index번호도 추가(!)
    1.빵ㅡ   : 1 x 1,000 = 1,000
    2.우유   : 4 x 2,000 = 8,000 (+2개 더!)
    3.계란   : 1 x   500 =   500
    ------------ 합계: 9,500원
    * 2+1 이벤트 기간 중 입니다.
"""
def test_convinient_store_on_sale(sale_mode=0):
    """ 다른 방법으로, 좀 더 가독성 높은 언패킹을 사용해 보자!
    """
    # input_str = input("번호-수량(공백)으로 입력하세요 :/n) # 원래 입력값 할당
    input_str = "1-1 2-4 3-1"                              # 테스트용 변수할당.
    input_arr = input_str.split()
    total_sum = 0

    for i, pack in enumerate(input_arr, 1):
        item_str, quantity_str = pack.split('-')# '1-1'을 문자 둘로 쪼갠다
        key = int(item_str)                     # 첫번째 문자를 숫자로 변경
        quantity = int(quantity_str)            # 두번째 문자를 숫자로 변경

        """ IF, SALE 모드에서는 2+1 이벤트를 시행한다. """
        sale_str, event_notice = ' ', ' '       # 이벤트 변수 초기화 ''
        if sale_mode:
            event_notice = '* 2+1 이벤트 기간 중 입니다.'

            if quantity > 2:
                bonus, _ = divmod(quantity, 2)
                sale_str = '(+{}개 더!)'.format(bonus)

        """ 영수증 출력: POS으로 Args 정렬 사용함! : {POS:} """
        print("{5:}.{0:4s} :{2:2d} x {1:5,} = {3:5,} {4:s}".format(
            PRICE_DICT[key][0],                 # 이름 = '빵'
            PRICE_DICT[key][1],                 # 가격 = 1000
            quantity,                           # 갯수 = 1
            quantity * PRICE_DICT[key][1],      # 합계 = 1000
            sale_str,
            i))

        """ 항목을 찍을 때 마다, total_sum 에 합계를 더 해간다 """
        total_sum += quantity * PRICE_DICT[key][1]
    print("------------ 합계: {:5,}원".format(total_sum))
    print(event_notice)
test_convinient_store_on_sale(sale_mode=True)
# test_convinient_store_on_sale()               # 세일기간이 아닐 때 (초기값)


""" 문제. 낙타형,파스칼형, 상수형 문자를 뱀형으로 바꿔라
# [IN] phrase_arr = ["PascalCaseIsHere", "camelComesHere", "CONSTANT_HERE"]
# [OUT]
# "PascalCaseIsHere"  ... pascal_case_is_here
# "camelComesHere"    ... camel_comes_here
# "CONSTANT_HERE"     ... constant_here
"""
def test_convert_to_snake():
    phrase_arr = [
        "PascalCaseIsHere",
        "camelComesHere",
        "CONSTANT_HERE",
        "------------------",
        "WhiteRabbitJumpingOverTheFox",
        "hereComesTheRainAgain",
        "THIS_IS_THE_EXPRESSION_FOR_CONSTANT",
        "------------------\n",]
    i = 0
    while i < len(phrase_arr):
        input_str = phrase_arr[i]
        i += 1

        word_set = ""
        # """ CASE3 = 첫번째, 두번째 문자가 대문자일때 = 상수타입 """
        if input_str[0].isupper() and input_str[1].isupper():
            for word in input_str:
                if word.isalpha():
                    word = word.lower()
                word_set += word
        else:
            # """ CASE1, CASE2 = 대문자를 만나면 언더바(_)를 넣는다 """
            for word in input_str:
                if word.isupper():
                    word = "_" + word.lower()
                word_set += word

        # """ 처리한 결과 앞에 언더바(_)가 있으면 잘라낸다 """
        if word_set[0] == '_':
            word_set = word_set[1:]

        print(word_set)
test_convert_to_snake()
