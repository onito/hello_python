#! python
import os
import sys
import datetime
""" file-docs : OPEN A RESTAURANT : Making Order System
  (1) to Show MENU_PAN = MENU_PAN (changeable)
  (2) to Input order = by Item index & quantity
  (3) to Calculate the Bills = Including (Tax= 6.5%, Tip= 10%)

 * Release Note : correct sorting version
    - Dict can not be ordered / arrange 'list' first.
    - Question : _arr.sort() = None. sorted(_arr) = 'list' O.K
    - I don't know the differences btw .sort() & sorted()
"""
TAX_RATE = 0.065        # 6.5 %
TIP_RATE = 0.11         # 11.0 %
SEPARATOR = '__'*24
MENU_DICT = {
    1 : ['BLACK_NOODLE', 5500],
    2 : ['RED_NOODLE', 6500],
    3 : ['ROLLED_RICE', 3500],
    4 : ['TTUK-RA-MYEON', 4500],
    5 : ['TTUK-BOK-KI', 3500],
    6 : ['FISHCAKE_SOUP', 2500],
    7 : ['FRIED_DUMPLINGS', 3500],
    8 : ['TOAST_SANDWITCH', 3000],
    9 : ['SPRITE(7-UP)', 1000],
    10 : ['BOTTLED_WATER', 500],
    }
MENU_PAN_FORMAT = ""                                +\
    "-------------------------------------------\n" +\
    "     MENU-PAN  / ONITO's RERSTAURANT        \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
BILL_FORMAT = ""                                    +\
    "--"*24 +\
    "\n     $$$ BILL / ONITO's RERSTAURANT $$$     \n" +\
    "--"*24 #+\
    # "%s"                                            +\
    # "-------------------------------------------\n"
TIME_PRINT = datetime.datetime.now()
TIME_PRINT_STR = TIME_PRINT.strftime('%p %I:%M:%S - %b.%d(%a), %Y')

def show_menu_pan():
    """ MAKING MENU_PAN of Your RESTAURANT
      - print(MENU_PAN_FORMAT % MENU_STRING)
      - make MENU_STRING from MENU_DICT
    """
    MENU_STRING = ''
    for key in MENU_DICT.keys():            # use .keys() .values() .items()
        MENU_STRING += '{:>2}. {:<16} {:.^10} {:5,} won'.format(
            key,
            MENU_DICT[key][0],
            '.',
            MENU_DICT[key][1]) + '\n'
    print(MENU_PAN_FORMAT %MENU_STRING)

def get_input_str():
    input_message = '' +\
        'Please, order menu by index-quantity & space\n' +\
        '(Ex: 1-2 2-1 3-2... just once for each index):\n'
    menu_order_str = input(input_message)
    return menu_order_str
# menu_order_str = get_input_str()   # class 'str'


menu_order_str='7-5 6-5 3-3 4-2 5-2 2-3 1-5'

""" HOW TO MAKE ORDER_ARR BEING SORTED
  - .sort() = 'NoneType' object is not subscriptable Error
  - sorted() = Function properly!! (O.K)
"""
# order_arr = menu_order_str.strip().split()       # 'list' = ['7-2', '6-3'..]
# order_arr = menu_order_str.strip().split().sort()# ERROR
order_arr = sorted(menu_order_str.strip().split()) # 'list' = ['1-2', '2-3'..]

# print(order_arr[0])            # 'str' = '1-2'
# print(order_arr[1])            # 'str' = '2-3'
# print(order_arr[2])            # 'str' = '3-4'

_a_arr = order_arr[0].strip().split('-')    # 'list' = [ '1', '2']
# print(_a_arr)
#
# print(_a_arr[0])                # 'str' = '1'
# print(_a_arr[1])                # 'str' = '2'
#
#
ORDER_DICT = {}
#
# _key = _a_arr[0]                # 'str' = '1'
# _value = _a_arr[1]              # 'str' = '2'
#
# ORDER_DICT[_key] = _value
# print(ORDER_DICT)               # {'1': '2'}


for order in order_arr:
    # print(order)
    _key = int(order.strip().split('-')[0])
    _value = int(order.strip().split('-')[1])
    ORDER_DICT[_key] = _value
    # print( _key, _value)
    # _a_arr = order_arr[0].strip().split('-')    # 'list' = [ '1', '2']

show_menu_pan()

print(menu_order_str)
print(ORDER_DICT, end='\n\n\n\n\n\n')

print(BILL_FORMAT)
menu_total = 0
for i, key in enumerate(ORDER_DICT.keys(), 1):
    _item = MENU_DICT[key][0]         # name
    _price = MENU_DICT[key][1]        # price
    _quantity = ORDER_DICT[key]       # quantity
    _total = _price * _quantity
    menu_total += _total
    print('{:2}.{:<15} {:.^3} {:6,} x{:2} = {:7,} won'.format(
        i,
        _item,
        '.',
        _price,
        _quantity,
        _total))

print(SEPARATOR)
print('\tMENU TOTAL {:.^16} {:7,} won'.format('.', menu_total))

print('\tTAX( {:>3.1f}%) {:.^16} {:7,} won'.format(
    TAX_RATE*100,
    '.',
    int(menu_total*TAX_RATE)))
print('\tTIP({:>3.1f}%) {:.^16} {:7,} won'.format(
    TIP_RATE*100,
    '.',
    int(menu_total*TIP_RATE)))

TOTAL = menu_total + int(menu_total*TAX_RATE) + int(menu_total*TIP_RATE)
PAY_AMOUNT = int(TOTAL/100) * 100
print(SEPARATOR)
print('Total Price        {:.^16} {:7,} won'.format('.', TOTAL))
print('PAY AMOUNT         {:.^16} {:7,} won'.format('.', PAY_AMOUNT))
print('{:>47}'.format('(deprive 10 at digits)'))
print(SEPARATOR)
print('{:>47}'.format('Order: '+TIME_PRINT_STR))


""" SORTING PROBLEM : HOW TO SORT ON MENU-ORDER
    --> Refer:making_things/order_v3

 -------------------------------------------
         MENU-PAN  / Onito's Restautant
 -------------------------------------------
  1. BLACK_NOODLE     .......... 5,500 won
  2. RED_NOODLE       .......... 6,500 won
  3. ROLLED_RICE      .......... 3,500 won
  4. TTUK-BOK-KI      .......... 3,500 won
  5. FRIED_DUMPLINGS  .......... 3,000 won
  6. SPRITE(7-UP)     .......... 1,000 won
  7. BOTTLED_WATER    ..........   500 won
 -------------------------------------------

 7-1 6-3 3-1 4-1 5-2 1-1
 {7: 1, 6: 3, 3: 1, 4: 1, 5: 2, 1: 1}



 ------------------------------------------------
         $$$ BILL / Onito's Restautant $$$
 ------------------------------------------------
  1.BOTTLED_WATER   ...    500 x  1 =    500 won
  2.SPRITE(7-UP)    ...  1,000 x  3 =  3,000 won
  3.ROLLED_RICE     ...  3,500 x  1 =  3,500 won
  4.TTUK-BOK-KI     ...  3,500 x  1 =  3,500 won
  5.FRIED_DUMPLINGS ...  3,000 x  2 =  6,000 won
  6.BLACK_NOODLE    ...  5,500 x  1 =  5,500 won
 ________________________________________________
     	MENU TOTAL .................  22,000 won
     	TAX( 6.5%) .................   1,430 won
     	TIP(11.0%) .................   2,420 won
 ________________________________________________
 Total Price        ................. 25,850 won
 PAY AMOUNT         ................. 25,800 won
                            (deprive 10 at digits)
 ________________________________________________
              Order: PM 07:59:34 - Nov.29(Wed), 2017
 [Finished in 0.832s] """



""" PROBLEM SOLVED
-------------------------------------------
     MENU-PAN  / ONITO's RERSTAURANT
-------------------------------------------
 1. BLACK_NOODLE     .......... 5,500 won
 2. RED_NOODLE       .......... 6,500 won
 3. ROLLED_RICE      .......... 3,500 won
 4. TTUK-BOK-KI      .......... 3,500 won
 5. FRIED_DUMPLINGS  .......... 3,000 won
 6. SPRITE(7-UP)     .......... 1,000 won
 7. BOTTLED_WATER    ..........   500 won
-------------------------------------------
7-5 6-5 3-3 4-2 5-2 2-3 1-5
{1: 5, 2: 3, 3: 3, 4: 2, 5: 2, 6: 5, 7: 5}





------------------------------------------------
     $$$ BILL / ONITO's RERSTAURANT $$$
------------------------------------------------
 1.BLACK_NOODLE    ...  5,500 x  5 =  27,500 won
 2.RED_NOODLE      ...  6,500 x  3 =  19,500 won
 3.ROLLED_RICE     ...  3,500 x  3 =  10,500 won
 4.TTUK-BOK-KI     ...  3,500 x  2 =   7,000 won
 5.FRIED_DUMPLINGS ...  3,000 x  2 =   6,000 won
 6.SPRITE(7-UP)    ...  1,000 x  5 =   5,000 won
 7.BOTTLED_WATER   ...    500 x  5 =   2,500 won
________________________________________________
    	MENU TOTAL .................  78,000 won
    	TAX( 6.5%) .................   5,070 won
    	TIP(11.0%) .................   8,580 won
________________________________________________
Total Price        .................  91,650 won
PAY AMOUNT         .................  91,600 won
                          (deprive 10 at digits)
________________________________________________
          Order: PM 07:16:14 - Nov.29(Wed), 2017
[Finished in 0.773s]

"""
