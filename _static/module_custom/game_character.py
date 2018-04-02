"""OOP.4 - 다형성 (폴리모피즘 : polymorphism)
----------------------------------------------
  모든 캐릭터의 베이스가 되는 클래스 Character()
   - self.val= hp, attack_power
   - self.func= attack, set demage, __str__
   - 모든 것의 정의(def)는 나중으로 미룬다.
"""

class Character(object):
    _total_count = 0

    def __init__(self):
        print("['%-12s'] 가 생성되었습니다.." % self.__class__.__name__)
        Character._total_count += 1
        self.hp = 0
        self.attack_power = 0

    def __str__(self):
        return "--- 이것은 모든 캐릭터의 부모가 되는 템플리트(추상화객체)입니다 ---"

    def attack(self, other_obj):
        pass

    def set_demage(self, attack_power):       # 핼퍼()  ... attack()에서 사용.
        pass







if __name__ == '__main__':
    print(__doc__)
