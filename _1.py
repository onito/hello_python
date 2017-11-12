RUN_IMAGE = [
 '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..''',
 '''
 ..oo...
 oooo...
 ..oo...
 ..oo...
 oooooo.''',
 '''
 .ooooo.
 o...oo.
 ..ooo..
 ooo....
 oooooo.''',
 '''
 .ooooo.
 ....oo.
 .oooo..
 ...ooo.
 ooooo..''',
 '''
 ...oo..
 .oo.o..
 oo..o..
 oooooo.
 ....o..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 ....oo.
 ooooo..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 oo..oo.
 .oooo..''',
 '''
 oooooo.
 o...oo.
 ...oo..
 ..oo...
 .oo....''',
 '''
 .ooooo.
 oo..oo.
 .oooo..
 oo..oo.
 .oooo..''',
 '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..''',
 ]

def test1():
    import os
    import time

    while True:
        for n in range(9,-1,-1):
            print('\n\n\n\n\n\n\n')
            print(RUN_IMAGE[n])
            time.sleep(0.5)
            os.system('cls')


_a =  '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..'''


_b =  '''
  .ooooo.
  oo...o.
  oooooo.
  ....oo.
  ooooo..'''

_a_arr = _a.strip().split('\n')
_b_arr = _b.strip().split('\n')


print(_a_arr)
print(_b_arr)

_c_arr = []
for n in range(5):
    if n == 0:
        _c_arr.append(' '+_a_arr[n] + '  ' + _b_arr[n])
    else:
        _c_arr.append(_a_arr[n] + _b_arr[n])


print(_c_arr)

print('\n\n\n\n')
for n in range(5):
    print(_c_arr[n])
