""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
  ** 함수형 프로그래밍 / 객체지향 프로그래밍 = 파이썬 특징의 2축!
  : 클래스 객체 = 흔히 붕어빵 틀(클래스) <--> 붕어빵(인스턴스)에 비유한다.
  :   붕어빵 틀은 1개 인데, 팥-붕어빵, 크림-붕어빵, 다양한 변종을 찍어낸다.
  :   찍어 낸 (인스턴스)는 독립적으로 작동 한다(self)

 1.클래스명 작명 = 파스칼 케이스 (ThisIsPascalCase)
 - 클래스 함수(매서드)의 첫번째 인자 = 인스턴스 자신(Self)
 - 클래스간 띄어쓰기는 2칸 / 함수(매서드)는 1칸 이다.

 2.오브젝트(객체)의 특징! : 클래스 오브젝트 <--> 인스턴스
 - (1) 값 (field) = 클래스변수 or 인스턴스 변수
 - (2) 기능 (method) = 매서드, 매직매서드, 더블언더스코어

 3.클래스만의 매우 특별한 기능
  * 상속 (Inherit) = 부모(Parent) - 자식(Child)
  * 중복 (Override) = 덮어쓰기 / 겹쳐쓰기

 4.'매직 매서드' = '더블 언더스코어' __무엇__ ... '매직' + '매서드' = 뭔가 특별한.
  * 자주쓰는 '매직'
  - __init__ (생성자)  <-->  __del__ (소멸자)
  - __repr__, __str__  : 스트링을 '리턴'
  - __add__, __sub__ ... '연산자'
"""
import _script_run_utf8
_script_run_utf8.main()

""" 만 들려는 매서드, 클래스변수, 인스턴스변수(self)
값 = 클래스변수(성격), 인스턴스변수(이름, 개인비밀)
기능 = 생성자, 소멸자, 연산자
"""

class Human(object):   # (T)his(I)s(H)uman = 파스칼타입
    total_count = 0    # 클래스 변수 = 전체적용
    icon = '무던함'     # icon (성격)

    def __init__(self, name):       # 매직매서드(생성자)
        Human.total_count += 1
        self.name = name

    def __add__(self, other_obj):
        print("'{}'와 '{}'는 결혼했습니다.".format(self.name, other_obj.name))

    def __sub__(self, other_obj):
        print("'{}'와 '{}'는 이혼했습니다.".format(self.name, other_obj.name))

    def __del__(self):
        print("'{}'는 죽었습니다.".format(self.name))

    def say_hello(self, other_obj):        # 기능을 함수(매서드)
        print("안녕하세요 '{}'님, 저는 '{}'".format(other_obj.name, self.name))

    def say_status(self):       #
        print("'{}' 님의 성격은 '{}' 입니다.".format(self.name, self.icon))


class ManOne(Human):
    pass


def show_shortened_life_story_with(obj1, obj2):
    print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
          '\n--------------------'.format(obj1.name, obj2.name))
    obj1 + obj2       # __add__() 매직매서드 실행
    obj1 - obj2       # __Sub__() 매직매서드 실행
    obj1.__del__()    # del().. __del__ 매직매서드 실행

def practice_02():
    kim = ManOne('김철수')
    kim.icon = '영리함'

    shin = ManOne('신영희')
    shin.icon = '난폭함'

    kim.say_status()        # '김철수' 님의 성격은 '영리함' 입니다.
    shin.say_status()       # '신영희' 님의 성격은 '난폭함' 입니다.

    kim.say_hello(shin)     # 안녕하세요 '신영희'님, 저는 '김철수'
    shin.say_hello(kim)     # '신영희' 님의 성격은 '난폭함' 입니다.


    show_shortened_life_story_with(kim, shin)
    """
    '김철수'와 '신영희'의 짧은 인생스토리~ 시작!!..
    --------------------
    '김철수'와 '신영희'는 결혼했습니다.
    '김철수'와 '신영희'는 이혼했습니다.
    '김철수'는 죽었습니다.
    """
practice_02()

def practice_01():
    h0 = Human('기본')
    hu = Human('무던한인간')            # 인스턴스 선언! (인스턴스 생성)

    hu1 = Human('난폭한인간')
    hu1.icon = '난폭함'

    hu2 = Human('사랑스러운인간')
    hu2.icon = '사랑스러움'


    print("COUNT: ", hu.total_count)   # 선언된 인스턴스. 값 또는 기능() 으로 호출
    print("성격: ", hu.icon)
    hu.say_hello(h0)
    hu.say_status()
    print('\n\n')


    print("COUNT: ", hu1.total_count)   # 선언된 인스턴스. 값 또는 기능() 으로 호출
    print("성격: ", hu1.icon)

    hu1.say_hello(hu)
    hu1.say_status()
    print('\n\n')


    print("COUNT: ", hu2.total_count)   # 선언된 인스턴스. 값 또는 기능() 으로 호출
    print("성격: ", hu2.icon)

    hu2.say_hello(hu1)
    hu2.say_status()
    print('\n\n')










""" day21 :
 - Old lectures: 01~14 폴더 정리 = _old_lectures
 - _pop_quiz 폴더설치 = 팝 퀴즈 이동정리
 - style sheet 에서 코맨트 색상변경(녹색) '스니펫' 추가
 - 추가 atom package 설치 = terminal, beautify, IDE... etc.
"""
