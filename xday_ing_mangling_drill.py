import _script_run_utf8
_script_run_utf8.main()
SEPERATOR = "--"*15 +'\n'


class AOne(object):
    icon = '심심한'

    def __init__(self, name):
        self.name = name
        print("'%s'인간(%s)님이 생성 되었습니다.."% (self.icon, self.name))
        print(SEPERATOR)

    @classmethod
    def set_icon(cls, modified_icon):
        cls.icon = modified_icon

ao = AOne('철수')
ao.icon = '열정적인'          # self.icon 이 새로 생성 됨 (인스턴스 변수)
ao.look = '잘생겼다'          # self.look 이 새로 생성 됨 (인스턴스 변수)


a2 = AOne('진수')             # self.look 은 없다, 호출하면 'Error'발생한다.
# a2.look = '진지하다'

a3 = AOne('형철')
# a3.look = '답답하다'

def 인사하기(other_obj):
    # '유니코드'를 지원 하므로 '한글' 함수명도 가능하다 (비추천!!)
    # 남 들이 본다면 '인상'을 찌푸릴 것이다.. 'RULE'대로 가자....
    print("** 모드: (%s)에게 인사하기 **"% other_obj.name)
    print("  '%s'인간님 안녕하세요~~!!" % other_obj.icon)
    print("  '%s' 인간님은 정말로... '%s'... \n" % (other_obj.icon, other_obj.look))

인사하기(ao)
인사하기(a2)
인사하기(a3)
