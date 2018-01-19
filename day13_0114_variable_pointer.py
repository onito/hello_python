""" 파이썬 베이직 :: 복습02 - 변수와 객체 :: 변수 할당 원리
 (1) 자료(데이터의 종류)
  - 문자: str(스트링), chr(캐릭터) <=> ord(아스키번호)
  - 숫자: int(인테저=정수), float(플로트=실수), complex(허수)
  - 데이터: list(리스트)와 dict(사전) - tuple

 (2) 데이터 포맷 / 인덱싱과 슬라이싱
  - 스트링 포맷 '%s %s'%(p1, p2),
  - 고급 포맷함수 '{} {}'.format(p1, p2)
  - 인덱싱 = 객체[pos], 객체[pos][pos][pos]...
  - 슬라이싱 = 객체[pos:pos]  객체[-1:-pos]

 (3) 객체(오브젝트)의 특성 (오브젝트 고유의 값과 기능을 가진다)
   -  값 : 속성 (Attributes)- 변수의 형태로 저장되어 있음
   - 기능: 메소드 (Methods) - 함수의 형태로 정의되어 있음
 """

def immutable_object():
    """ immutable(불변) 과 mutable(가변) 의 개념
     (1) 변수는 할당하는 것이 아니라, 객체를 가르키는 것(포인팅)
     (2) 불변:이뮤터블(immutable)과 가변:뮤터블(mutable)의 정의
        - 불변객체, 동일하면 같은 id값을 갖는다.
        - 가변객체, 동일해도 다른 id값을 갖는다.
     (3) 객체의 특징 - 속성(attributes)과 기능(Methods)
        - 고유 메소드는 dir()로 조회할 수 있다.
        - 객체의 메모리 주소는 id()로 조회할 수 있다.
        - 객체의 종류(타입)은 type()으로 조회할 수 있다.
     """
    def show_id(_a, _b, _c):
        print()
        print('_a =', id(_a), '-->', _a, end='\n')
        print('_b =', id(_b), '-->', _b, end='\n')
        print('_c =', id(_c), '-->', _c, end='\n')

    def test01_immutable_object_pointing():
        """ immutable object (불변객체 : 실수,정수, 튜플 등)
         - int 객체는 이뮤터블(immutable), 불변이다
         - 불변이기 때문에, 오브젝트를 생성할 때마다 새로 생성한다
         - 동일 오브젝트가 있으면 모든 변수가 한개 오브젝트를 포인팅한다.
        """
        _a = 100    # id.01 (같은 오브젝트)
        _b = 100    # id.01 (같은 오브젝트)
        _c = 200    # id.02 (다른 오브젝트)
        show_id(_a, _b, _c)

        _b = _c     # _b 가 id.02를 포인팅 한다 (id.02를 포인팅 한다 - 주소변경)
        show_id(_a, _b, _c)

        _c = _a     # _a, _c = id.01를 동시에 가르킨다.
        show_id(_a, _b, _c)

        _b = _c     # _a, _b, _c 가 동시에 id.01 (100)을 가르킨다.
        show_id(_a, _b, _c)

    def test02_mutable_object_pointing():
        _aa = [1,2,3,4]
        _bb = [1,2,3,4]
        _cc = [1,2,3,4]
        # _aa, _bb, _cc 는 Id_01, id_02, id_03 각자 다른 오브젝트를 포인팅한다
        # 뮤터블 오브젝트는 변할수 있어, 달라지므로.... 매번 오브젝트를 새로 생성한다.
        show_id(_aa, _bb, _cc)

        _bb = _aa       # _bb에 _aa를 할당한다 (_aa, _bb는 같은 오브젝트를 포인팅한다)
        show_id(_aa, _bb, _cc)

        _aa.remove(3)
        _aa.remove(4)   # _aa에서 3,4를 제거하면, 같은곳을 가르키던 _bb도 같이변경된다.
        show_id(_aa, _bb, _cc)

    def test03_string_object_pointing():
        _aaa = "Hello World~! This is the real world of python, Welcome!"
        _bbb = "Hello World~! This is the real world of python, Welcome!"
        _ccc = "Hello World~! This is the real world of python, Welcome!"
        show_id(_aaa, _bbb, _ccc)

        _ccc = "I'm chanig object"
        show_id(_aaa, _bbb, _ccc)

        _bbb = "I'm chanig object"
        show_id(_aaa, _bbb, _ccc)

    if __name__ == '__main__':
        test01_immutable_object_pointing()
        test02_mutable_object_pointing()
        test03_string_object_pointing()
immutable_object()
