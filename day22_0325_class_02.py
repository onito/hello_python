""" 클래스 객체/오브젝트 : (객체 지향 프로그래밍 - OOP: Obj. Oriented Progmng)
클래스변수 / 인스턴스변수는, 변수의 접근 권한(소유권)에 관한 문제
  - '클래스 객체'를 독립시키려면, 접근권한, 소유권, 상호관계를 명확히 해야 함

@staticmethod = 클래스 객체와 상관없지만 끼워넣은 매서드
@classmethod = 인스턴스로 접근해서 클래스변수를 변경시키는 매서드
"""
import _script_run_utf8
_script_run_utf8.main()


SEPERATOR = "--"*20 +"\n"

class Human(object):       # (T)his(I)s(H)uman = 파스칼타입
    total_count = 0             # 클래스 변수 = 전체적용
    __icon = '무던함'            # __icon (성격)

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
        print("안녕하세요 '{}'님, 저는 '{}'입니다".format(other_obj.name, self.name))

    def say_status(self):       # 성격(__icon)을 알려줍니다.
        print("'{}' 님의 성격은 '{}' 입니다.".format(self.name, self.__icon))

    def set_name(self, modified_name):
        print("'{}'님의 이름이 '{}'으로 변경 되었습니다".format(self.name, modified_name))
        self.name = modified_name

    """ 클래스 매서드는, 인스턴스 명으로 클래스변수에 접근할 방법을 열어준다."""
    @classmethod
    def set_icon(cls, modified_icon):
        print("'{}' ---> '{}' 변경!!".format(cls.__icon, modified_icon))
        cls.__icon = modified_icon

    """ 스테틱 매서드는, 객체기능과 상관없지만 그림(편의)상 포함시켜야 할 때"""
    @staticmethod
    def show_shortened_life_story_with(obj1, obj2):
        print("\n\n'{}'와 '{}'의 짧은 인생스토리~ 시작!!.."
              "\n--------------------".format(obj1.name, obj2.name))
        obj1 + obj2       # __add__() 매직매서드 실행
        obj1 - obj2       # __Sub__() 매직매서드 실행
        obj1.__del__()    # del().. __del__ 매직매서드 실행


class ManOne(Human):
    def __init__(self, name):
        super().__init__(name)
        print("'{}'님이 추가 되었습니다. 총 {}명".format(self.name, self.total_count))



kim = ManOne('김철수')
kim.__icon = '영리함'        # 사유화가 되었다 = 'self.__icon'이 추가 되었다
# kim.set_icon('영리함')     # ManOne의 '빵틀'이 변경되었다.

shin = ManOne('신영희')
shin.__icon = '난폭함'       # 사유화가 되었다 = 'self.__icon'이 추가 되었다
# shin.set_icon('난폭함')    # ManOne의  '빵틀'이 변경 되었다.

# kim.set_name('김철철철철철')   # '빵'이 변경 되었다
# kim.name = '김철철철철철'   # '빵'이 변경 되었다
print(SEPERATOR)

# kim.__icon= '--- 좀비스러움 ---'   # '빵'이 변경 되었습니다.
kim.set_icon('--- 좀비스러움 ---')    # ManOne의 '빵틀'이 변경되었다.
# print('[Human]======', Human._Human_icon)
# print('[ManOne]=====', ManOne._ManOne_icon)


kim.say_status()        # '김철수' 님의 성격은 '영리함' 입니다.
kim.say_hello(shin)     # 안녕하세요 '신영희'님, 저는 '김철수'
print(SEPERATOR)

shin.say_status()       # '신영희' 님의 성격은 '난폭함' 입니다.
shin.say_hello(kim)     # '신영희' 님의 성격은 '난폭함' 입니다.
print(SEPERATOR)


kim.show_shortened_life_story_with(kim, shin)
# shin.show_shortened_life_story_with(kim, shin)
# Human.show_shortened_life_story_with(kim, shin)
# ManOne.show_shortened_life_story_with(kim, shin)
print(SEPERATOR)
"""
'김철수'와 '신영희'의 짧은 인생스토리~ 시작!!..
--------------------
'김철수'와 '신영희'는 결혼했습니다.
'김철수'와 '신영희'는 이혼했습니다.
'김철수'는 죽었습니다.
"""



hu = ManOne('무던한인간')            # 인스턴스 선언! (인스턴스 생성)

hu1 = ManOne('난폭한인간')
hu1.__icon = '난폭함'                  # self.__icon 이 추가됨

hu2 = ManOne('사랑스러운인간')
hu2.__icon = '사랑스러움'              # self.__icon 이 추가됨
print(SEPERATOR)


hu.say_status()
hu.say_hello(hu1)
print(SEPERATOR)


hu1.say_status()
hu1.say_hello(hu2)
print(SEPERATOR)


print("COUNT: ", hu.total_count)   # 선언된 인스턴스. 값 또는 기능() 으로 호출
print("성격: ", hu2.__icon)
hu2.say_status()
hu2.say_hello(hu)
print(SEPERATOR)
