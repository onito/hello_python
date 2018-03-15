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

class  ManOne(Object):
    icon = ''
    pass

class MonTwo(ManOne):
    pass


""" day21 :
 - Old lectures: 01~14 폴더 정리 = _old_lectures
 - _pop_quiz 폴더설치 = 팝 퀴즈 이동정리
 - style sheet 에서 코맨트 색상변경(녹색) '스니펫' 추가
 - 추가 atom package 설치 = terminal, beautify, IDE... etc.
"""
