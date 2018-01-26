""" 가위-바위-보 : 알고리즘은?
 # - 가위 < 바위 < 보 = 0 < 1 < 2
 # -  0 < 1 < 2 < 3 (%3=0) < 4(%3=1) < 5(%3=2)
 # - 여러가지 승리판단의 가설을 세워서 경우의 수를 입증 해 본다
 \ 승리 판단 알고리즘 (경우의 수: 3x3=9)
  (1) 가설 : 큰 수가 이긴다, 예외: 0 - 2
  ----------------
  0 - 0 = 비:  0
  1 - 0 = 앞:  1
  2 - 0 = 뒤:  2

  0 - 1 = 뒤: -1
  1 - 1 = 비:  0
  2 - 1 = 앞:  1

  0 - 2 = 앞: -2
  1 - 2 = 뒤: -1
  2 - 2 = 비:  0
  ----------------
  (2) 확인 된 가설
    - 숫자가 같으면 (0 이면) 비긴 다 (확인 완료!)
    - (+)면 앞, (-)면 뒤가 이긴다... 예외: 2칸이 벌어지면 예외사항이 발생한다.
    - (-)면 앞, (+)면 뒤가 이긴다... (예외: 격차가 2일 경우)

  (3) 게임 룰 전환: 묵찌빠
   - 이긴 사람이 공략한다 : 이긴 사람과 같이면, 이긴다.
   - 같지 않으면 승자(공격자)를 판단 한다...승자(공격자)를 바꾼다.

  Day15 - 배울 것 2가지
 # (1) 튜플 언패킹 기법
 # (2) 포괄적 리스트 기법
 """
import os
import random
import numpy as np
import _script_run_utf8
_script_run_utf8.main()

def get_computer_array(times):
    return [random.randint(0, 2) for n in range(times)]

def is_same_size(my_array, computer_array):
    return len(my_array) == len(computer_array)

def get_change_to_String_array(number_array):
    """ 0,1,2 넘버 리스트를 가위,바위,보 스트링 리스트로 변환
    # 포괄적 리스트 기법을 3번 중첩 적용시키면, 코드가 짧아진다.
    # 가위, 바위, 보 3가지 변환을 하므로 3번 중첩시킨다.
    """
    _kawis = ["가위" if attack == 0 else attack for attack in number_array]
    _bawis = ["바위" if attack == 1 else attack for attack in _kawis]
    return ["보" if attack == 2 else attack for attack in _bawis] # string_array

def get_change_to_String_array_old(number_array):
    """ 원래 방식대로 짜보자..  (포괄적 리스트와 비교 차원에서)
    # elif 분기를 3번 해야 하므로 아무리 짧게 줄여도 9-라인 코딩이 필요 함
    # 3 중첩 포괄적 리스트를 쓰면 3-라인 코딩으로 가능하다.
    """
    string_array = []
    for number in number_array:
        if number == 0:
            string_array.append("가위")
        elif number == 1:
            string_array.append("바위")
        else:
            string_array.append("보")
    return string_array

def get_who_is_win(my_array, computer_array):
    """ 한번 공격은 '리스트' 타입으로 한번 입력한다
    # 결과 반환은 '리스트' 타입으로 반환 한다.
    # 승=1(True), 패=0(False) 공격자 기준, '숫자 리스트'로 결과를 반환한다.
    # 무승부일 경우 오류케이스(?)로 처리 -1
    # 예) judge_array = [-1,1,0,1,0,1,0,1,1,1]  :6승1무3패
    """
    judge_array = []
    for i in range(len(my_array)):
        judge = my_array[i] - computer_array[i]
        if judge != 0:
            if abs(judge) != 2:
                if judge > 0:   judge_array.append(1)
                else: judge_array.append(0)
            else:
                if judge > 0:   judge_array.append(0)
                else: judge_array.append(1)
        else:
            judge_array.append(-1)
    return judge_array

def function_final_test():
    MY_ATTACKS = [0, 1, 1, 2, 0, 1, 0, 2, 1, 0]
    COMPUTER_ATTACKS = get_computer_array(10)

    print("횟수는 동일하다 : %s .... O.K"%is_same_size(MY_ATTACKS, COMPUTER_ATTACKS))

    print(get_change_to_String_array(MY_ATTACKS))
    print(get_change_to_String_array_old(COMPUTER_ATTACKS))

    # print(MY_ATTACKS)
    # print(COMPUTER_ATTACKS)

    judges = get_who_is_win(MY_ATTACKS, COMPUTER_ATTACKS)
    print(np.array(MY_ATTACKS) - np.array(COMPUTER_ATTACKS))
    # 이것이 judges 결과동일

    # 3단 분류, 포괄적 리스트를 또! 써보자...
    _judges1 = ["승" if judge == 1 else judge for judge in judges]
    _judges2 = ["무" if judge == -1 else judge for judge in _judges1]
    _judges3 = ["패" if judge == 0 else judge for judge in _judges2] # string_array
    print(_judges3)


DRAW = ["-", "주먹", "가위", "보"] # [0, 1, 2, 3]

def get_judge_string(na, com):
    equ = na - com
    if equ == -1 or equ == 2:
        return "승자:{:>4} - 내가 이겼습니다.\n".format(DRAW[na])
    elif equ == 0:
        return "___비겼습니다___\n"
    else:
        return "승자:{:>4} - 컴이 이겼습니다\n".format(DRAW[com])

def simple_rock_scissors_paper():
    """
    화일 독스트링 : 화일의 설명 - 가위.바위.보 -모듈(블랙박스)
    # >>> RESULT
    # {1: '승', 0: '패', -1: '무'}
    # >>> RESULT[1]
    # '승'
    # >>> RESULT[-1]
    # '무'
    # >>> RESULT[0]
    # '패'
    # >>>
    """
    import random

    DECO_SEPARATOR = "=+" * 15
    DRAW = ["-", "가위", "바위", "보"]         # POS = 1,2,3 , POS'0'은 버린다.
    RESULT = { 1: "승", 0: "패", -1 : "무"}    # 키값 = 1, 0, -1 로 호출한다.

    def test1_comprehensive_list():
        """ 포괄적 리스트 - 예제 (Comprehensive list) """
        numbers = [n for n in range(1,11)]
        yes5 = ["YES" for n in range(5)]
        yes5_if = [ "YES" for n in range(10) if n%2 == 0 ]
        yes_no_10 = ["YES" if n%2 == 0 else "NO" for n in range(1, 11)]

        yes_vari = 10 if yes_no_10[0] == "YES" else "WHAT?"

        print(numbers)
        print(yes5)
        print(yes5_if)
        print(yes_no_10)
        print()
        print(yes_vari)

        """ 포괄적 리스트의 결과정리
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # ['YES', 'YES', 'YES', 'YES', 'YES']
        # ['YES', 'YES', 'YES', 'YES', 'YES']
        # ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
        # WHAT?
        """

    def is_stop_ok():
        """
        # 그만하겠는지? 물어보고 yes/no 를 입력받는다.
        # yes = True, 참/거짓을 반환한다
        """
        if input().lower().startswith('y'):
            return True
        else:
            return False

    def get_result_rock_paper_scissors(me, com):
        """ 가위.바위.보 승무패를 판단해 준다.
        # IN = 1,2,3 중 하나, 가위,바위, 보
        # OUT = 1,0,-1 중 하나 -- 승무패
        """
        eq = me - com
        if eq == 0:
            return -1       # ? = 무
        elif eq == 1 or eq == -2:
            return 1        # 1, Ture = 승
        elif eq == -1 or eq == 2:
            return 0        # 0, False = 패

    def get_stack_win_draw_lose_count(judge, win_cnt, draw_cnt, lose_cnt):
        """ 모듈로 대체하는 구문
        # if judge == 1:
        #     win_count += 1
        # elif judge == 0:
        #     lose_count += 1
        # else:
        #     draw_count += 1
        """
        if judge == 1:
            win_cnt += 1
        elif judge == 0:
            lose_cnt += 1
        else:
            draw_cnt += 1
        return judge, win_cnt, draw_cnt, lose_cnt


    win_count, draw_count, lose_count, attempt = 0, 0, 0, 0
    print("가위-바위-보 게임\n" +DECO_SEPARATOR+ "\n")

    while True:
        me = int(input('당신의 선택은? (가위=1, 바위=2, 보=3) : '))
        com = random.randint(1, 3)

        judge = get_result_rock_paper_scissors(me, com)

        print("{} vs {} = {}".format(
            DRAW[me],
            DRAW[com],
            RESULT[judge]))

        _, win_count, draw_count, lose_count = get_stack_win_draw_lose_count(
            judge, win_count, draw_count, lose_count)

        attempt += 1

        print("그만 하시겠습니까? (y/n)")
        if is_stop_ok():
            print(DECO_SEPARATOR)
            break

        print(DECO_SEPARATOR)

    # print('\n'*8+'You did %d games.. Winnig Rate : %.3f' % (atmpt, win_count/atmpt))
    print("\n\n")
    print("게임통계..\n{}\n시도:{}회 .... {}승/{}무/{}패 \n승률:{:5.2f}%".format(
        DECO_SEPARATOR,
        attempt,
        win_count,
        draw_count,
        lose_count,
        100*win_count/attempt))         # (%)백분율 계산
    print(DECO_SEPARATOR)


function_final_test()

if __name__ == '__main__':
    fights = [(na, com) for na in range(1, 4) for com in range(1, 4)]
    print(fights, "\n\n")

    for fight in fights:
        na, com = fight

        judge = get_judge_string(na, com)
        print("{:>4} vs.{:>4} ... {:30}".format(DRAW[na], DRAW[com], judge))
