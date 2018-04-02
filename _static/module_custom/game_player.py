from game_character import Character


class Player(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        # 오브젝트(인스턴스) 속성값을 오버라이드
        Player._total_count += 1
        self.hp = 100
        self.attack_power = 20

    def __str__(self):
        return "--- 이것은 ('%s')캐릭터 입니다 ---" % self.__class__.__name__

    def attack(self, other_obj):
        return other_obj.set_demage(self.attack_power)

    def set_demage(self, attack_power):       # 핼퍼()  ... attack()에서 사용.
        if self.hp:
            if self.hp > attack_power:
                self.hp -= attack_power
                return True         # 생존성공
            else:
                self.hp = 0
                return False        # 체력바닥 & 생존실퍠
        else:
            print("... 이미 죽었습니다 ...")
            return None



class Warrior(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        # 오브젝트(인스턴스) 속성값을 오버라이드
        Warrior._total_count += 1
        self.hp = 300
        self.attack_power = 70



class Magician(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        # 오브젝트(인스턴스) 속성값을 오버라이드
        Magician._total_count += 1
        self.hp = 100
        self.attack_power = 50




if __name__ == '__main__':
    print(__doc__)

    b = Magician()     # 객체선언 a = 오브젝트(인스턴스)
    a = Warrior()
    print('b=',b)            # 객체를 'print' 하면 __str__() 또는 __repr__ 값 표시.

    while a.hp > 0:
        if b.attack(a):             # True = 생존성공!
            print('b.hp=', b.hp)
            print('a.hp=', a.hp, '\n')
        else:                       # False = 생존실패! (hp=0)
            print(b.attack(a))      # hp=0에서 한번 더 공격 = 메시지 출력
            print('a.hp=', a.hp, '\n')

    print('객체합계=',Character._total_count)
    print('플레이어=',Player._total_count)
    print('전투사=', Warrior._total_count)
    print('마법사=', Magician._total_count)
