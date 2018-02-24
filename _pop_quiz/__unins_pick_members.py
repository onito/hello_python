import os
import time
import random

SELECT_NUM = 7              # select 'num' out of 'MERCY_LIST'
MERCY_LIST = [
    'Vassili', 'Phantom', 'Redeye', 'Aimee', 'Proxy', 'Bushwhacker',
    'Fletcher', 'Turtle', 'Skyhammer', 'Arty', 'Kira', 'Stoker',
    'Javelin', 'Sawbonez', 'Aura', 'Sparks', 'Phoenix', 'Guardian',
    'Fragger', 'Nader', 'Rhino', 'Thunder',
    ]

def get_members_name():
    return MERCY_LIST[random.randint(0, len(MERCY_LIST)-1)]


input('press enter to start ')
while True:
    mercy_choices = []

    while len(mercy_choices) < SELECT_NUM:
        name = get_members_name()

        if name not in mercy_choices:
            mercy_choices.append(name)

            os.system('cls')
            print(mercy_choices)
            time.sleep(0.5)

    if input('\n\nSTOP(y/NO)?').lower().startswith('y'):
        break
    os.system('cls')
