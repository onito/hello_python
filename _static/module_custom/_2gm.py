from _1gc import Character


class Monster(Character):
    _total_count = 0

    def __init__(self):
        super().__init__()
        Monster._total_count += 1


class FireMonster(Monster):
    _total_count = 0

    def __init__(self):
        super().__init__()
        FireMonster._total_count += 1
        print("['%-17s'] object is created..."% self.__class__.__name__)


class IceMonster(Monster):

    def __init__(self):
        super().__init__()
        IceMonster._total_count += 1
        print("['%-17s'] object is created..."% self.__class__.__name__)




if __name__ == '__main__':
    a = FireMonster()
    b = IceMonster()

    print("Number of Characters =", Character._total_count)
    print("Number of Monsters   =", Monster._total_count)
