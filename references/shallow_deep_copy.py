""" SHALLOW COPY & DEEP COPY
 - the differences
"""

def generator_01():
    """
    [10]
    [10, 10]
    [10, 10, 10]
    [10, 10, 10, 10]
    [10, 10, 10, 10, 10]
    """
    x = []
    for i in range(5):
        x.append(10)
        yield x[:]

def main_01():
    g = generator_01()      # yield x [:]
    _a = [next(g) for n in range(5)]

    for _n in _a:
        print(_n)           # 'list'
main_01()
print(end='\n\n\n')

def generator_02():
    """
    [10, 10, 10, 10, 10]
    [10, 10, 10, 10, 10]
    [10, 10, 10, 10, 10]
    [10, 10, 10, 10, 10]
    [10, 10, 10, 10, 10]
    """
    x = []
    for i in range(5):
        x.append(10)
        yield x                         #! <--- ONLY THE THING DIFFERENT

def main_02():
    g = generator_02()      # yield x
    _a = [next(g) for n in range(5)]

    for _n in _a:
        print(_n)           # 'list'
main_02()
