""" 객체(Object)의 속성(Attributes)과 기능:메소드(Methods)
 (1) 종합적(포괄적)리스트 작성법, *args, **kwargs, enumerate() 이용하기
   - 시퀸스(반복자)를 만들어 내는 법

 (2) 객채(Object)의 생성 = id(), type(), 속성(고유값)과 기능(함수)을 자동부여
   - 메모리상의 고유주소 = id()
   - 객체의 타입 = type()
   - 객체의 속성(값)= help()
   - 객체의 기능(매서드) = dir()

 (3) 리스트 객체함수 : use dir()
   - clear(), append(), pop(), count(), remove(), sort(), reverse().....

 (4) 딕트 객체함수 : use dir()
   - clear(), get(), items(), keys(), values(), pop().....
"""

import _script_run_utf8
_script_run_utf8.main()

def show_id(_a, _b, _c):
    """ 함수의 인자 = 파라미터 / 파라미터 --> 내부변수에 전달 (지역변수)
      - 파라미터와 내부변수는 다르다 / 함수가 닫히면 내부변수(지역변수)는 사라진다.
    """
    print()
    # print('_a =', id(_a), '-->', _a)
    print('_a = {} --> {}'.format(id(_a), _a))
    print('_b = {} --> {}'.format(id(_b), _b))
    print('_c = {} --> {}'.format(id(_c), _c))


def show_method(*args):         # 튜플 파라매터(*args), 딕트 파라매터(**kwargs)
    """ 별표1개 (*)  = 한개 이상의 파라미터를 (튜플)형대로 반환한다
    #   별표2개 (**) = 한개 이상의 파라미터를 {딕트}형태로 반환한다
    #
    # 문제3. '리스트' 객체와 '튜플' 객체의 메소드 중 언더바를 제외한 매소드만
    #      출력하는 함수를 작성하시오 (*args 또는 **kwargs 를 사용)
    """
    for arg in args:
        print('\n\n')
        print('--- %s---' % type(arg))
        for command in dir(arg):
            if command[0] != '_':
                print(command)


def show_help():
    import day14_0121_id_type_dir_help
    print(help(day14_0121_id_type_dir_help))


def test1():
    """ # 숫자는 불변객체, : 내용이 같으면, 같은 주소(id)를 갖는다
    #
    # 문제1. '숫자'객체가 '이뮤터블' 함을 증명하세요 ... 설명
    #  - '이뮤터블'한 객체는 고유의 id를 갖습니다.
    #  - 각각의 변수가 포인터가 옮겨가는 과정을 재현하시오
    """
    a = 100         # 각자 고유주소
    b = 200         # 각자 고유주소
    c = a               # 같은 주소를 포인팅 함.

    show_id(a, b, c)


def test2():
    """ # 리스트 객체 테스트 : 내용은 같아도, 각자 다른 주소(id)를 받는다
    #
    # 문제2. '리스트' 객체가 copy()를 써서 복사해야 되는 과정을 쓰세요 ... 설명
    #  - 동일한 '객체'를 할당 했을때 '변경된 결과값'이 적용되는 과정
    """
    d = [1, 2, 3, 4]    # 다른주소
    e = [1, 2, 3, 4]    # 다른주소
    f = d               # 같은 객체를 포인팅 (같은주소) - 카피아님
    f = d.copy()        # 카피함수로 완전 다른객체로 카피한다
    d.append(7)         # 서로 다른 객체라서 내용을 바꿔도, 영향없음

    show_id(d, e, f)


def test3_tuple_unpacking():
    """ # 튜플 언페킹 기법으로 변수를 한꺼번에 할당 한다
    # 잘못된 언패킹 방법 : 한꺼번에 할당 된다.
    # (_a, _b, _c) = (100, 200, _a)  # ERROR = _a is not defined : 튜플 언패킹
    """
    (_a, _b, _c) = (100, 100, 200)
    show_id(_a, _b, _c)


def test4_dir_method_comparison():
    _d = [1, 2]         # (리스트)(튜플)객체가 달라서, 매소드도 각자 다르다.
    _e = (1, 2)         # (튜플)객체는 명령(메소드)가 몇개 안된다.
    show_method(_d, _e)


def test5_guidos_famous_quote():
    import _script_run_utf8
    _script_run_utf8.main()

    quote = """
귀도 반 로섬 '어록': http://www.azquotes.com/author/46455-Guido_van_Rossum
 : 파이썬 프로젝트는 개발자에게 어느정도 '자유도'가 필요한가? 에 대한 실험이다.
   너무 많은 '자유도'가 주어지면, 아무도 다른사람의 '코드'를 읽지 않는다.
   너무 적은 '자유도'가 제공되면 (엄격하면) 풍부한 표현력이 위협 받는다.
"""
    print(quote)


def song_99_beers():
    """ 문제3. IF 분기 문제 - 99병의 맥주 ( 변경: 맥주 -> ?? )
    미국과 캐나다 등에서 자주 불리는 권주가(勸酒歌). 벽장에 있는 99개의 맥주병을
    하나씩 꺼내면서 수가 줄어드는 걸 노래하고 있다. 가사는 긴 주제에 무지무지 외우기가
    쉽기 때문에 주로 긴 여행길에서 할 일 없을 때 부르거나 하는 노래다.

    - 99병의 맥주들이 벽에 있네~, 99병의 맥주들이 벽에 있네~
    - 이제 한 병을 내려 마셨네~,  98병의 맥주들이 벽에 있네~
    - -----------------------
    - 1병의 맥주(들이x)가 벽에 있네~, 1병의 맥주가 벽에 있네~
    - 이제 한 병을 내려 마셨네~,         ..........
    - -----------------------
    - 더 이상 벽에는 맥주가 없네~, 더 이상 벽에는 맥주가 없네~
    - 더 하시겠 습니까? (Yes=Enter / No=Space+Enter )?
    - -----------------------

    - 더 이상 벽에는 맥주가 없네~, 더 이상 벽에는 맥주가 없네~
    - 가게에 나가서 맥주를 사왔네, 99병의 맥주들이 벽에 있네~
    - -----------------------
    - (반복)
    타잔 빤쓰와 비슷하지만 복수<->단수, 가사변경을 오가며 바뀌는 것이
    IF문을 연습하기 좋아서 HELLO WORLD 만큼 유명한 문제.
    """
    import time

    beer = 9

    def is_stop_playing():
        """ 그만 할것인지 참/거짓 값을 반환한다 / 참 일때 break
        # 스톱 플래잉 = 'n' 를 입력하면 True 를 반환 (break)
        # 엔터를 입력하면 False를 반환한다 (반복실행 한다)
        """
        print("\n\n다시 한번 하시겠습니까? ([Y]es=엔터 or [N]o)\n\n\n")
        return input().lower().startswith('n')

    def show_song_repeated(beer, beer_after):
        repeated_song = "--------------------------" +\
            "\n{:2} 병의 맥주들이 벽에 있네~  {:2} 병의 맥주들이 벽에 있네~" +\
            "\n이제 한 병을 내려 마셨네~    {:2} 병의 맥주들이 벽에 있네~\n"
        print(repeated_song.format(beer, beer, beer_after), flush=True)

    def show_song_last_one():
        the_last_song = "--------------------------" +\
            "\n한 병의 맥주가 벽에 있네~    한 병의 맥주가 벽에 있네~" +\
            "\n이제 한 병을 내려 마셨네~    ............    \n" +\
            "\n--------------------------" +\
            "\n더 이상 벽에는 맥주가 없네~  더 이상 벽에는 맥주가 없네~\n"
        print(the_last_song, flush=True)

    def show_song_reset_beer():
        the_reset_song = "--------------------------" +\
            "\n가게에 나가서 맥주를 사왔네     또, 10병의 맥주들이 벽에 있네~\n"
        print(the_reset_song, flush=True)

    while True:
        if beer > 1:
            show_song_repeated(beer, beer - 1)
        else:
            show_song_last_one()
            if is_stop_playing():
                break
            else:
                beer = 10
                show_song_reset_beer()
        beer -= 1


song_99_beers()
