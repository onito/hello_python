#! python
import datetime

MENU_DICT = {
            'BACK_NOODLE': 5000,
            'RED_NOODLE': 7000,
            'FRIED_DUMPLINGS': 3000,
            'ROLLED_RICE': 4000,
            'TTUK-BOK-KI': 3000,
            'SPRITE': 1000,
            'BOTTLED_WATER' : 500,
            }

MENU_PAN_FORMAT = """
 ---------------------------------------
    MENU-PAN  / Onito's Restautant
 ---------------------------------------
 %s
 ---------------------------------------"""

BILL_FORMAT ="""
 --------------------------------------
       $$$ BILL $$$
 --------------------------------------
  MEAL = %s $
  TAX  = %s $ (%s %%)
  TIP  = %s $
 -----------
    TOTAL = %s $
    DATE : %s
 --------------------------------------"""   # BILL_FORMAT Needs '5' args

MENU_PAN_STRING = ''
for i, key in enumerate(MENU_DICT.keys(), 1):
    if i == 1:
        MENU_PAN_STRING += ' {}. {:18s} ... {:6,} won'.format(
                        i,
                        key,
                        MENU_DICT[key]) + '\n'
    else:
        MENU_PAN_STRING += '  {}. {:18s} ... {:6,} won'.format(
                        i,
                        key,
                        MENU_DICT[key]) + '\n'

print(MENU_PAN_FORMAT% MENU_PAN_STRING)
print('\n\n\n\n')

def test2_in_person():
    MEAL = 44.5                 # Dollars $
    TAX_RATE = 0.0675		# 6.75%
    TIP = 0.15					# 15%

    TOTAL = MEAL + MEAL*TAX_RATE + TIP
    date_string = datetime.datetime.now().strftime("\'%y %b.%dth(%a)-%p %I:%M")


    print(BILL_FORMAT% (
                    MEAL,
                    MEAL * TAX_RATE, TAX_RATE*100,
                    TIP,
                    TOTAL,
                    date_string))
test2_in_person()
