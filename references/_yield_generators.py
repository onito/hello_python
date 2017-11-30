def test1_show_combi():
    def show_hap(num1, num2):
        print('{} + {} = {}'.format(num1, num2, num1+num2))

    def show_gop(num1, num2):
        print('{} x {} = {}'.format(num1, num2, num1*num2))

    def show_hap_gop(num1, num2):
        show_hap(num1, num2)
        show_gop(num1, num2)

    num1 = 3
    num2 = 4
    show_hap_gop(num1, num2)
# test1_show_combi()

def test2_get_combi():
    def get_hap(num1, num2):
        return (num1 + num2)

    def get_gop(num1, num2):
        return (num1 * num2)

    def get_hap_gop(num1, num2):
        _a = get_hap(num1, num2)
        _b = get_gop(num1, num2)
        return (_a, _b)

    num1 = 3
    num2 = 4
    _a, _b = get_hap_gop(num1, num2)
    print('get_hap({0:},{1:}) = {0:} + {1:} = {2:} \nget_gop({0:},{1:}) = {0:} x {1:} = {3:}'.format(num1, num2, _a, _b))
# test2_get_combi()

# show_gop(4,5)
# _a = get_hap(4,5)

def number_generator(start_number=0):
    """
    Function Start!
    0
    1
    2
    3
    4
    Function End!
    """
    print('Function Start!')
    while start_number < 5:
        # yield(return) start_number to caller every time
        yield start_number
        start_number += 1
    print('Function End!')

for i in number_generator():
    # call generator, return value(start_number) as i
    print(i)
