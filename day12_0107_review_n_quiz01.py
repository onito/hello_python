""" 파이썬 베이직 :: 복습 - 프린트 포맷
 (1) 자료(데이터의 종류)
  - 문자: str(스트링), chr(캐릭터) <=> ord(아스키번호)
  - 숫자: int(인테저=정수), float(플로트=실수), complex(허수)
  - 데이터: list(리스트)와 dict(사전) - tuple

 (2) 데이터 포맷 / 인덱싱과 슬라이싱
  - 스트링포맷 '%s'%(p), 포맷함수 '{}'.format(p)
  - 인덱싱 = 객체[pos], 객체[pos][pos][pos]...
  - 슬라이싱 = 객체[pos:pos]  객체[-1:-pos]
  """
  # (3) 리스트 객체함수 : use dir()
  #  - clear, append, pop, count, remove, sort, reverse..
  #
  # (4) 딕트 객체함수 : use dir()
  #  - clear, get, items, keys, values, pop..

import _script_run_utf8
_script_run_utf8.main()

# for command in dir([1,2,3]):
#     print(command)

SEPARATOR = '-'*30

def test01_score_calculation():
    korean = int(input('국어점수을 입력하시오 :'))
    english = int(input('영어점수을 입력하시오 :'))
    math = int(input('수학점수을 입력하시오 :'))
    # 테스트용 변수설정(!) :
    # korean, english, math = 78, 98, 98

    print('\n\n' + SEPARATOR)
    print('  국어점수 : {} \n  영어점수 : {} \n  수학점수 : {}'.format(
        korean, english, math)
        )
    print(SEPARATOR)
    total = korean + english + math
    print('  총점 : {:3}'.format(total))
    print('  평균 : {:6.2f}'.format(total / 3))
    print(SEPARATOR)
# test01_score_calculation()

def test02_calculate_circle():
    radius = int(input('반지름을 입력하세요 :'))
    pi = 3.141592
    area = pi * radius**2
    length = 2 * pi * radius
    print('입력 된 반지름 : {}'.format(radius))
    print(SEPARATOR)
    print('원의 둘레 :{:15,.3f}'.format(length))
    print('원의 면적 :{:15,.3f}'.format(area))
    print(SEPARATOR)
# test02_calculate_circle()

def test03_divide_digit_5():
    _a = '0123456789'
    _b = '영일이삼사오육칠팔구'
    num_sound_dict = { int(num):sound for num, sound in zip(_a, _b)}
    # {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육',
    # 7: '칠', 8: '팔', 9: '구'}

    while True:
        value = int(input('양의 정수 5자리를 입력하시오 :'))
        # 테스트용 변수설정 :
        # value = 59824

        n_01 = (value//10**4)%10
        n_02 = (value//10**3)%10
        n_03 = (value//10**2)%10
        n_04 = (value//10**1)%10
        n_05 = (value//10**0)%10

        print('다섯자리 수는.. {},{},{},{},{}'.format(n_01, n_02, n_03, n_04, n_05))
        print('입력하신 숫자는... \n\n')
        print('{}만{}천{}백{}십{}... 입니다'.format(
            num_sound_dict[n_01],
            num_sound_dict[n_02],
            num_sound_dict[n_03],
            num_sound_dict[n_04],
            num_sound_dict[n_05]))

        again = input('계속 더 하시겠습니까? (Y/n)... \n\n\n')
        if again != '':
            quit()
# test03_divide_digit_5()

def extra01_random_multiple():
    for n in range(11180, 112000, 113):
        for i in range(1000, 1808800, 13817):
            print('{:7,} x {:9,} = {:14,}'.format(n, i, n*i))
# extra01_random_multiple()



def show_dict_method():
    print('=== 딕셔너리 매쏘드(펑션), 명령어 ===')
    for i, command in enumerate(dir({1:'a'}), -28):
        if command[0:2] != '__':
            print('  {:2}. {}'.format(i,command))
        # else:
        #     print('  {:2}. {}'.format(i,command))
# show_dict_method()

def show_ascii():
    """ (참조)아스키 테이블 : http://defindit.com/ascii.html
     ASCII = American Standard Code for Information Interchange
    """
    count = 0
    for i, n in enumerate(range(1, 128, 1), 1):
        count += 1
        if count >= 8:
            print('{:3}: {}'.format(i, chr(n)), end='  \n')
            count = 0
        else:
            print('{:3}: {}'.format(i, chr(n)), end='  ')
# show_ascii()

"""
1.변수(Variable)와 상수(Constant)
 - 변수는 대문자로 시작할 수 있다    = 거짓?
 - 변수는 숫자로 시작할 수 있다      = 거짓?
 - 변수는 특수기호로 시작 할 수 있다 = 거짓?
 - 변수는 소문자 뱀타입으로 작성한다
 - 상수는 GLOBAL 이다
 - 상수는 대문자 뱀타입으로 작성한다

2. 낙타타입, 뱀타입, 파스칼 타입
3. 메쏘드(함수)는 동사로 시작 : is, get, show(print), remove, write..
3. 변수(상수)는 명사로 시작

낙타 타입(camel case)   : thisIsTheRealWorld : 허용 안함 / 특별 한 경우에는 써도됨
뱀타입(snake case - 소) : this_is_the_real_world : 변수명(명사), 메쏘드명(동사)
뱀타입(snake case - 대) : THIS_IS_THE_REAL_WORLD : 상수명 (명사)
파스칼타입 : ThisIsTheRealWorld : Pascal case - 클래스객체 = 파스칼타입
"""
