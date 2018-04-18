from _1gc import Character


class Player(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Player._total_count += 1


class Warrior(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Warrior._total_count += 1
        print("['%-17s'] 생성되었습니다."% self.__class__.__name__)


class Magician(Player):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Magician._total_count += 1
        print("['%-17s'] 생성되었습니다."% self.__class__.__name__)




if __name__ == '__main__':
    a = Warrior()
    b = Magician()

    print("캐릭터의 갯수=", Character._total_count)
    print("플레이어의 갯수=", Player._total_count)
    print("전투사의 갯수=", Warrior._total_count)
    print("마법사의 갯수=", Magician._total_count)
