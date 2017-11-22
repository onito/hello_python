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
SEPARATOR = '__'*22
MENU_DICT = {
    1 : ['BACK_NOODLE', 5500],
    2 : ['RED_NOODLE', 6500],
    3 : ['ROLLED_RICE', 3500],
    4 : ['TTUK-BOK-KI', 3500],
    5 : ['FRIED_DUMPLINGS', 3000],
    6 : ['SPRITE(7-UP)', 1000],
    7 : ['BOTTLED_WATER', 500],}
MENU_PAN_FORMAT = ""                                +\
    "-------------------------------------------\n" +\
    "     MENU-PAN  / Onito's Restautant        \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"
BILL_FORMAT = ""                                    +\
    "-------------------------------------------\n" +\
    "     $$$ BILL / Onito's Restautant $$$     \n" +\
    "-------------------------------------------\n" +\
    "%s"                                            +\
    "-------------------------------------------\n"

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

def get_input_order_string():
    """ get _order_arr=['1-1', '2-3', '3-1', '4-3'] from input_string """
    _order = input(
        'Please, order menu by index-quantity & space \n' +\
        '(Ex: 1-2 2-1 3-2... just once for each index)  :  \n')
    _order_arr = _order.strip().split()
    return sorted(_order_arr)

def get_order_dict_from_arr(_order_arr):
    """ get order_dict= {1:1, 2:3, 3:1, 4:3} from _order_arr
     WHY? key:value have to be 'int'? -- for using it directly
      (1) only split('-') = 'str' .... {1:'1', 2:'3', 3:'1', 4:'3'}
      (2) forced 'int'    = 'int' .... {1:1, 2:3, 3:1, 4:3} """
    order_dict = {}
    for strip in _order_arr:
        _key = int(strip.strip().split('-')[0])
        _val = int(strip.strip().split('-')[1])
        order_dict[_key] = _val
    return order_dict

def is_play_again():
    """ This function returns True if the player wants to play again, with 'y'
    otherwise it returns False. / using .startswith('str')
    """
    print('\n\nDo you want to check bill of other table? (yes or no)')
    return input().lower().startswith('y')

def main():
    show_menu_pan()

    _order_arr = get_input_order_string()
    # t0 make 'list' ['1-1', '2-3', '3-1', '4-3'] fron input_string

    _order_dict = get_order_dict_from_arr(_order_arr)
    # to make 'dict' {1:1, 2:3, 3:1, 4:3} from oder_arr

    print('\n'*5, 'YOUR ORDER = ', _order_dict)
    print(SEPARATOR,'\n')      # { 1:3, 2:1, 3:1, 4:3}


    menu_price = 0
    calculate_detail_arr = []

    for i, key in enumerate(_order_dict.keys(), 1):
        quantity = _order_dict[key]
        item = MENU_DICT[key][0]
        price = MENU_DICT[key][1]

        calculate_detail_arr.append('{}. {:<15} {:6,} x{:2} = {:>6,} won'.format(
            i,
            item,
            price,
            quantity,
            price*quantity))

        menu_price += (quantity * price)


    for calculate in calculate_detail_arr:
        print(calculate)
    print(SEPARATOR)

    rate_tax = 6.5/100
    tax = int(menu_price * rate_tax)

    rate_tip = 10.0/100
    tip = int(rate_tip * (menu_price * (1 + rate_tax)))

    print(' Menu price  {:.<15} {:6,} won'.format('.', menu_price))
    print(' TAX({:4}%)  {:.<15} {:6,} won'.format(rate_tax*100,'.', tax))
    print(' TIP({:4}%)  {:.<15} {:6,} won'.format(rate_tip*100,'.', tip))

    print(SEPARATOR)
    total_price = menu_price + tax + tip
    print(' TOTAL price {:.<15} {:6,} won'.format('.', total_price))
    print(' PAY AMOUNT  {:.<15} {:6,} won (deprive 10 digit)'.format('.', 100 * int(total_price/100)))


if __name__ == '__main__':
    while True:
        main()

        if is_play_again():
            os.system('cls')
            continue
        else:
            break
