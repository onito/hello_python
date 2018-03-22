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

    def __init__(self, arg_model):
        Car._total_count += 1
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
        print(FORM_INTRO % args)

    def set_speed_up(self):
        if self.attr['speed'] + self.attr['s_able'] <= self.attr['max_speed']:
            self.attr['speed'] += self.attr['s_able']
            return True
        else:
            self.attr['speed'] == self.attr['max_speed']
            return True

    def set_speed_down(self):
        if self.attr['speed'] - self.attr['s_able'] >= 0:
            self.attr['speed'] += self.attr['s_able']
            return True
        else:
            self.attr['speed'] == 0
            return True

    def say_speed(self):
        print("PRESENT SPEED =", self.attr['speed'], "km/h")


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
            'max_speed':   0,
            's_able':   0,
            'speed':   0,
            }



# a = SportCar('PPPPPPPPP')
# a.show_status()
# a.set_speed_up()
# a.say_speed()


if __name__ == '__main__':
    # print(FORM_INTRO %('Porsche','SportCar',300,20,0))
    a = SportCar('PPPPPPPPP')
    a.show_status()
    a.set_speed_up()
    a.say_speed()
