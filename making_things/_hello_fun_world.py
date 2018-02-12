import os
import time
import random

while True:
    message = input("input short words you want to make being shaken : \n")
    if len(message) == 0:
        message = "HELLO WORLD!"

    for i in range(random.randint(5, 30)):
        os.system('cls')
        for n in range(50):
            print(" "*random.randint(1,20)+ message.center(40))
        # time.sleep(0.02)

    if input("\n\nSTOP? (Y/N)").lower().startswith('y'):
        break
    os.system('cls')
