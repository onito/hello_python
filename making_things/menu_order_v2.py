#! python
""" Explain about this file and purpose, function etc.. """

MENU_DICT = {
    1 : ['BACK_NOODLE', 5000],
    2 : ['RED_NOODLE', 7000],
    3 : ['FRIED_DUMPLINGS', 3000],
    4 : ['ROLLED_RICE', 4000],
    5 : ['TTUK-BOK-KI', 3000],
    6 : ['SPRITE(7-UP)', 1000],
    7 : ['BOTTLED_WATER', 500],}

MENU_PAN_FORMAT = """
 ---------------------------------------
    MENU-PAN  / Onito's Restautant
 ---------------------------------------
 %s
 ---------------------------------------"""

BILL_FORMAT = """
 --------------------------------------
       $$$ BILL / Onito's Restautant $$$
 --------------------------------------
 %s
 --------------------------------------"""   #

MENU_PAN_STRING = ''
for key in MENU_DICT.keys():
    if key == 1:
        MENU_PAN_STRING += '{}. {:18s} ... {:6,} won'.format(
            key,
            MENU_DICT[key][0],
            MENU_DICT[key][1]) + '\n'
    else:
        MENU_PAN_STRING += ' {}. {:18s} ... {:6,} won'.format(
            key,
            MENU_DICT[key][0],
            MENU_DICT[key][1]) + '\n'

print(MENU_PAN_FORMAT %MENU_PAN_STRING)

_a = input('order menu by index numbers using spaces  : ')
_a_arr = _a.strip().split()

order_arr = []
for strip in _a_arr:
    order_arr.append(strip.strip().split('-'))
    # order_arr.append(
    #     (int(strip.strip().split('-')[0]), int(strip.strip().split('-')[1]))
    #     )
    """ Why Append mode is 'str'?
     (1) only split('-') = 'str' .... [['1', '1'], ['3', '3']]
     (2) forced 'int'    = 'int' .... [[1, 1], [3, 3]]
     """
print(order_arr)
