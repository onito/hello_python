""" 기본: 클래스 Car()
 - name(kind), current_speed, max_speed, acceleration
   기본: Car()  --> 상속: SportCar(), TruckCar()
 """

# NG = No Good
import _static.module_custom.class_car as cc

# class_car.py 일 경우
# from _static.module_custom import class_car as cc

# class_car.py의 필요한 기능만 불러 올 경우
# from _static.module_custom.class_car import SportCar, TruckCar

# 시스템 'PATH'로 지정 된 경우
# import class_car as cc

a = cc.SportCar('PORSCHE')
b = cc.TruckCar('BONGO')
c = cc.TruckCar('TCAR')

a.show_status()
b.show_status()

# 나(self) 만 바꿀 수 있다
c.attr['max_speed'] = 300
c.show_status()
