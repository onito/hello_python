import os
import time

def test_1():
    plus_until = int(input("몇까지 더할까요?: "))
    base_number = 0

    for i in range(plus_until):
        base_number += i + 1
    print(base_number)
# test_1()

def test_2():
    while True:
        for i in range(10):
            value_A = 0 + i
            value_B = 10 - i
            os.system('cls')
            print('|%s[HELL0]%s| WORLD!' %('-' * value_A,'-' * value_B))
            time.sleep(0.01)

        for i in range(10):
            value_A = 0 + i
            value_B = 10 - i
            os.system('cls')
            print('|%s[HELL0]%s| WORLD!' %('-' * value_B,'-' * value_A))
            time.sleep(0.01)
# test_2()

def test_3():
    sample_dict = {1:'집', 2:'우산', 3:'자동차'}
    key_list = list(sample_dict.keys())
    value_list = list(sample_dict.values())

    print('키값에는 %s' %(key_list[0]), end='')
    for i in range(len(key_list) - 1):
        print(',', key_list[i + 1], end='')
    print(' = %s개의 자료가 있습니다.' %(len(key_list)))

    print('형식은 ', (type(key_list[0])), end='')
    for i in range(len(key_list) - 1):
        print(',',type(key_list[i + 1]), end='')
    print(' 입니다.\n')

    print('밸류값에는 %s' %(value_list[0]), end='')
    for i in range(len(value_list) - 1):
        print(',', value_list[i + 1], end='')
    print(' = %s개의 자료가 있습니다.' %(len(value_list)))

    print('형식은 ', (type(value_list[0])), end='')
    for i in range(len(value_list) - 1):
        print(',',type(value_list[i + 1]), end='')
    print(' 입니다.')
# test_3()

def test_4():
    number_list = []
    even_number = []
    odd_num_ng = []

    for i in range(11):
        number_list.append(i)

    print(number_list)

    for i in range(len(number_list)):
        if number_list[i]%2 != 0 or number_list[i] == 0: continue
        even_number.append(number_list[i])
    print(even_number)

    for i in range(len(number_list)):
        if number_list[i]%2 != 0 or number_list[i] == 0:
            odd_num_ng.append('NG')
        else:
            odd_num_ng.append(number_list[i])

    print(odd_num_ng)
test_4()
