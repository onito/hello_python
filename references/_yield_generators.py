def test1_show_combi():
    def show_hap(num1, num2):           # 헬퍼1()
        print('{} + {} = {}'
              ''.format(num1, num2, num1 + num2))

    def show_gop(num1, num2):           # 헬퍼2()
        print('{} x {} = {}'
              ''.format(num1, num2, num1 * num2))

    def show_hap_gop(num1, num2):       # 헬퍼1,2()를 이용한 콤비함수
        show_hap(num1, num2)
        show_gop(num1, num2)

    if __name__ == '__main__':
        num1 = 3
        num2 = 4
        show_hap_gop(num1, num2)


test1_show_combi()


def test2_get_combi():
    def get_hap(num1, num2):            # 반환 헬퍼1()
        return num1 + num2

    def get_gop(num1, num2):            # 반환 헬퍼2()
        return num1 * num2

    def get_hap_gop(num1, num2):        # 헬퍼1,2를 할당해서, 콤비반환 함수()
        return get_hap(num1, num2), get_gop(num1, num2)

    if __name__ == '__main__':
        num1 = 3
        num2 = 4
        _a, _b = get_hap_gop(num1, num2)

        print('\n'
              'get_hap({0:},{1:}) = {0:} + {1:} = {2:} \n'
              'get_gop({0:},{1:}) = {0:} x {1:} = {3:} \n'
              '\n'.format(num1, num2, _a, _b))


test2_get_combi()


def number_generator(start_number=0):
    print('Function Start!')

    while start_number < 5:
        # yield(return) start_number to caller every time
        yield start_number
        start_number += 1

    print('Function End!')


# call generator, return value(start_number) as i
for i in number_generator():
    print(i)


# """ 실행결과 :
# 3 + 4 = 7
# 3 x 4 = 12
#
# get_hap(3,4) = 3 + 4 = 7
# get_gop(3,4) = 3 x 4 = 12
#
# generator()로 부터 Yield 값이 소진될때 까지 받아서, 프린트 한다.
# Function Start!
# 0   ......  # 일드 반환!
# 1   ......  # 일드 반환!
# 2   ......  # 일드 반환!
# 3   ......  # 일드 반환!
# 4   ......  # 일드 반환.종료(끝)!
# Function End!
