import os
import time
import random

while True:
    message = input("흔들고 싶은 '짧은' 인사말을 넣으세요 : \n")
    if len(message) == 0:
        # 만약 '입력값'이 없다면, 기본으로 'HELLO WORLD!' 선택한다.
        message = "HELLO WORLD!"

    for i in range(random.randint(5, 30)):
        # 흔드는 횟수는 5~30회, 랜덤으로 선택한다.
        os.system('cls')
        for n in range(45):
            #트리의 높이는 45개로 제한한다.
            print(" "*random.randint(1,15)+ message.center(40))
            # 흔드는 중심축은 41(1+40) ~ 60(20+40) 규모로 흔든다.
        time.sleep(0.1)

    print("\n\nBeing Shaken %s times...."% i)
    if input("STOP? (Y/N)").lower().startswith('y'):
        break
    os.system('cls')
