def test1_comp_list_if_only():
    """ If-state only, place at the end /or SyntaxError  """
    # [0, 2, 4, 6, 8, 10] len=5
    _a = [n for n in range(11) if n%2 == 0 ]
    print(_a)
# test1_comp_list_if_only()

def test1_comp_list_if_else():
    """ If-state has 'else', place first /or SyntaxError """
    # [0, '?', 2, '?', 4, '?', 6, '?', 8, '?', 10] len=10
    _a = [n if n%2 == 0 else '?' for n in range(11)]
    print(_a)

    # [0, 1, 2, 3, 4, '?', '?', '?', '?', '?', '?'] len=10
    _a = [n if n < 5 else '?' for n in range(11)]
    print(_a)
# test1_comp_list_if_else()

def test2_lambda():
    """ lambda uses for a nameless oneline-function definition """
    _a_arr = [n for n in range(10)]
    print('_a_arr orig = %s'% _a_arr)

    _combin = [2**n for n in _a_arr]
    print('_combined = %s'% _combin)

    _bmap_arr = list(map(lambda n: 2**n, _a_arr))
    print('_lambda_map = %s'% _bmap_arr)
# test2_lambda()

def test3_lambda_normal():
    a = (lambda x, y: x**2 + y**2)(223, 223)
    print(a)                        # 66458

    b = (lambda x, y: x**2 + y**2)
    print(b(77, 77))                # 11858
    print(b(88, 88))                # 15488

    a_map = map(lambda x, y: x**2 + y**2,
                [22,33,44,55,66,77],
                [22,33,44,55,66,77],)
    print(list(a_map))
# test3_lambda_normal()

# quadratic = (lambda a, b, c, d: (-b +d*(math.sqrt(b**2-4*a*c)))/(2*a))
quadratic = (lambda a, b, c, d: (-b +d*(b**2-4*a*c)**0.5)/(2*a))
quadratic_arr = (lambda a, b, c: [quadratic(a,b,c,-1), quadratic(a,b,c,+1)])

print(quadratic_arr(1,1,-1))  #
print(quadratic_arr(2,1,1))   # if use math -- ValueError: math domain
