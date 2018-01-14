""" BUBBLE SORT & DISPLAYS BARS
  - 바-챠트가 원하는 형상이 나올때 까지, 반복해서 섞는다 (랜덤.셔플)
  - 원하는 바-챠트 형상이 나오면, 버블정렬을 시작 할 수 있다.
"""
import os                   # 화면을 지우기 위한 모듈
import time                 # 딜레이를 만들기 위한 모듈
import random               # 무작위로 숫자를 섞기(셔플링)하기 위한 모듈

def display_bars(numbers, changing=-1, now_bar='=', other_bar='%'):
    for i in range(len(numbers)):
        if i == changing:
            print('{:2}: {}'.format(numbers[i], now_bar*numbers[i]), flush=True)
        else:
            print('{:2}: {}'.format(numbers[i], other_bar*numbers[i]), flush=True)

def show_shuffled_bars_before_after(quantity):
    """ 랜덤.셔플을 섞기 전(정열), 섞은 후(셔플드)를 바-챠트로 보여준다.
     - 최초의 '리스트'는 'Apprehenshive list'로 자동 작성 한다.
     - 파라매터(quantity)는 '리스트'의 숫자 갯수(크기)
     - 섞은(셔플)상태가 맘에 안 들면, 맘에 들때까지 '엔터'를 눌러 반복 섞는다
     - 버블정렬을 시작하려면, 아무 키 + '엔터'조합을 누르면, 정렬 스타트...
    """
    continue_flag = True        # '참'일 경우 무한 반복루프, '거짓'이면 탈출!

    while continue_flag:
        # 랜덤 셔플링, 섞기 전 '리스트' 바-차트
        numbers = [n for n in range(1, quantity+1)]
        display_bars(numbers, other_bar=chr(127))
        print('\n\n')

        random.shuffle(numbers)

        # 랜덤 셔플링, 섞은 후 '리스트' 바-차트
        display_bars(numbers, other_bar=chr(127))
        print('\n\n')

        # 계속-플래그를 거짓으로 바꾸고 셔플된 값을 리턴,
        # - While True - 무한루프에서 빠져나오는 방법
        # - 리턴을 하면 함수가 닫히기 때문에 While 플래그(깃발) 바꾸는 방법 사용
        print("숫자를 다시 섞으시겠습니까?")
        print("(Yes='Enter' / No='other+Enter')")
        answer = input()

        if answer != '':
            continue_flag = False
            return numbers
        os.system('cls')

# (1) 섞은 상태를 보여주고, 셔플 된 숫자 리스트를 생성(Return) 한다.
shuffled_numbers = show_shuffled_bars_before_after(quantity=20)

# (2) 밀어내기 마지막 라인을 n-1 에서 1 까지, 계속 줄여나간다.
last_number = len(shuffled_numbers)-1
while last_number >= 1:
    for n in range(last_number):
        os.system('cls')            # 화면을 지운다 (초기화)
        if shuffled_numbers[n] > shuffled_numbers[n+1]:
            (shuffled_numbers[n], shuffled_numbers[n+1]) = (
                shuffled_numbers[n+1], shuffled_numbers[n])

        if n < 0 or n == last_number-1:
            # changing = -1 : 바꾸고 있는 위치 보여주기 기능 비활성화
            #  - ASCII 번호 127 = 1 바이트 크기의 작은 사각형 '박스'
            display_bars(shuffled_numbers, changing=-1, other_bar=chr(127))
        else:
            # 현재 카운트+1 위치에서 바꾸고 있는 상태 보여주기
            display_bars(shuffled_numbers, changing=n+1, other_bar=chr(127))
        time.sleep(0.4)             # 0.4 초를 지연 시킨다. (delay)
    last_number -= 1                # 한번 순환 할 때 마다 '1'씩 줄여 나간다

# (3) 최종 정렬이 끝난 '리스트'를 보여준다
print('\n\nfinished', shuffled_numbers)
