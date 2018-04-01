""" CAR INFORM """

FORM_INTRO = '''\
=================================
\tVEHICLE INFORMATION
---------------------------------
1. MODEL     : %s (%s)
2. MAX SPEED :      %d km/h
3. ACCELARAT :   +_ %d kmh
4. STATUS    :      %d kmh
---------------------------------\n\n\n'''


class Car(object):
    _total_count = 0
    _kind = '일반용'
    _car_dict = dict()

    def __init__(self, arg_model):
        Car._total_count += 1
        Car._car_dict[Car._total_count] = [arg_model, self._kind]
        self.speed = 0
        print("['%-8s']!! A NEW CAR!! has come  ...  total: (%s)" %
              (arg_model, Car._total_count))
        self.attr = {
            'model':  arg_model,
            'kind':   self._kind,
            'max_speed':   110,
            's_able':   2,
            'speed':   self.speed,
            }

    def show_status(self):
        args = tuple(self.attr.values())
        print('---------------------------------')
        for key, value in self._car_dict.items():
            print(key, value)

        print(FORM_INTRO % args)

    def set_speed_up(self):
        if self.attr['speed'] + self.attr['s_able'] <= self.attr['max_speed']:
            self.attr['speed'] += self.attr['s_able']
            return True         # 정상가속
        else:
            self.attr['speed'] == self.attr['max_speed']
            return False        # 최고점 도달

    def set_speed_down(self):
        if self.attr['speed'] - self.attr['s_able'] >= 0:
            self.attr['speed'] -= self.attr['s_able']
            return True         # 정상감속
        else:
            self.attr['speed'] == 0
            return False        # 최저점 도달

    def say_speed(self, bool):
        if bool:
            print("PRESENT SPEED =", self.attr['speed'], "km/h")
        else:
            if self.attr['speed'] == 0:
                print(" ---- 차가 정지 했습니다 ---- ")
            else:
                print(" ==== 최고속도(%s km/h)입니다. ==== "%self.attr['max_speed'])


class SportCar(Car):
    _total_count = 0
    _kind = '스포츠'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        SportCar._total_count += 1
        self.attr = {
            'model':  arg_model,
            'kind':   self._kind,
            'max_speed':   350,
            's_able':   50,
            'speed':   0,
            }


class TruckCar(Car):
    _total_count = 0
    _kind = '업소용'

    def __init__(self, arg_model):
        super().__init__(arg_model)
        TruckCar._total_count += 1
        self.attr = {
            'model':  arg_model,
            'kind':   self._kind,
            'max_speed':   110,
            's_able':   5,
            'speed':   0,
            }


def speed_up_down(obj):
    while obj.attr['speed'] < obj.attr['max_speed']:
        obj.say_speed(obj.set_speed_up())
    obj.say_speed(obj.set_speed_up())

    while obj.attr['speed'] > 0:
        obj.say_speed(obj.set_speed_down())
    obj.say_speed(obj.set_speed_down())



# 경계선 아래는 외부에서 부를수 없다.
if __name__ == '__main__':
    a = TruckCar('T')
    b = TruckCar('BONGO')
    c = SportCar('PORSCHE')

    # 나(self) 만 바꿀 수 있다
    c.attr['max_speed'] = 200
    c.attr['s_able'] = 50

    c.show_status()

    speed_up_down(c)
    speed_up_down(b)

    # 차 사전의 접근권한(공용) = 클래스/인스턴스 모두 가능
    # print(Car._car_dict)
    # print(a._car_dict)
