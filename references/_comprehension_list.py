def test1_comp_list():
    """ If-state only, place at the end /or SyntaxError  """
    # [0, 2, 4, 6, 8, 10] len=5
    _a = [n for n in range(11) if n%2 == 0 ]
    print(_a)

    """ If-state has 'else', place first /or SyntaxError """
    # [0, '?', 2, '?', 4, '?', 6, '?', 8, '?', 10] len=10
    _a = [n if n%2 == 0 else '?' for n in range(11)]
    print(_a)

    # [0, 1, 2, 3, 4, '?', '?', '?', '?', '?', '?'] len=10
    _a = [n if n < 5 else '?' for n in range(11)]
    print(_a)
# test1_comp_list()


def test2_lambda():
    _a_arr = [n for n in range(10)]
    print('_a_arr orig = %s'% _a_arr)

    _combin = [2**n for n in _a_arr]
    print('_combined = %s'% _combin)

    _bmap_arr = list(map(lambda n: 2**n, _a_arr))
    print('_lambda_map = %s'% _bmap_arr)
# test2_lambda()
