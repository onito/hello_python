""" THE LEAST SURPRISE LAW : Don't use weired thing too much.
 - Substitution for docstring, not forced usage, similar to SCALA.
 - refer below : Python 3에서 함수의 키워드 인자 강제와 주석문
 http://blog.hannal.com/2015/03/keyword-only-arguments_and_annotations_for_python3/
 - '애노테이션'활용 : 인자에 '주석'을 달거나, 타입을 강제(@deco)할 수 있다.
"""
def ohms_law(I:'Current'=10, R:'Resistance'=50) -> 'Voltage':
    """ ASSIGN ANNOTATIONS AS DICT.
    {'I': 'Current', 'R': 'Resistance', 'return': 'Voltage'}
    """
    return I * R


def ohms_law_test():
    print(ohms_law.__annotations__)         # dict type
    # {'I': 'Current', 'R': 'Resistance', 'return': 'Voltage'}
    print(list(ohms_law.__annotations__.keys()))
    print(list(ohms_law.__annotations__.values()))

    I, R = 20, 30   # voltage = 600 v
    print("Voltage: {:} x {:} = {:,} v".format(
        I,
        R,
        ohms_law(I,R),
        ))          # 기본값 I=10, R=50
ohms_law_test()




def check_argument_type(func):
    """ '데코레이터'를 사용하여, 인자형식을 검사한다. """
    def wrapper(*args):
        # 첫번째, '속성(attr)'가 없거나, '애노테이션'이 없으면 그냥 실행(노말).
        if not hasattr(func, '__annotations__') \
                or len(func.__annotations__) == 0:
            return func(*args)

        # '일립시스'(생략부호) 있으면, 위치를 찾아서 'check_index'에 기록
        try:
            check_index = func.__annotations__['args'].index(Ellipsis)

        # '일립시스'가 없으면, '어노테이션' 갯수를 하나 삭제(?)
        except ValueError:
            check_index = len(func.__annotations__['args']) - 1

        # args[0] ~ args[check_index] : 위치인자 = 튜플에 기록
        print('ANNO: ', args[:check_index] )

        # 어노테이션 = {'args': (<class 'int'>, <class 'int'>, Ellipsis)}
        print(func.__annotations__)
        print(func.__annotations__['args'][1])          # <class 'int'>
        print(func.__annotations__['args'][0])          # <class 'int'>
        print(func.__annotations__['args'][0].__name__) # 'int'

        for _i, _arg in enumerate(args[:check_index]):
            _arg_type = func.__annotations__['args'][_i]

            # '어노테이션'에 기록 된 <클래스타입> 소속인가?: / True = 계속비교
            if isinstance(_arg, _arg_type):
                continue

            # '어노테이션' 기록된 타입이 아닐경우, 에러 발생시킴
            raise TypeError(
                "The type of '{}' does not match '{}' type".format(
                    _arg, _arg_type.__name__))
        return func(*args)                      # 래퍼()는 받은 함수를 '반환'
    return wrapper                              # 데코()는 '래퍼 바디'를 '반환'


# 첫번째, 두번째 인자만 검색하고, 나머지는 생략한다.
@check_argument_type
def hello_func(*args: (int, int, ...)):
    print(*args)


# hello_func(1, 2, '3', 'a')      # O.K.
# hello_func(1, '2', '3', 'a')    # N.G. ... 'TypeError' 발생시킴
