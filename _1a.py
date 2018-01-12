""" NEW YEAR MESSAGE OF 2018 IN VARIOUS WAYS
https://www.google.com/search?q=\
%48%41%50%50%59%20%4e%45%57%20%59%45%41%52%20%32%30%31%38
[72, 65, 80, 80, 89, 32, 78, 69, 87, 32, 89, 69, 65, 82, 32, 50, 48, 49, 56]
HAPPY NEW YEAR 2018

b'\xeb\xac\xb4\xec\x88\xa0\xeb\x85\x84,\xec\x83\x88\xed\x95\xb4\xeb\
\xb3\xb5\xeb\xa7\x8e\xec\x9d\xb4'
무술년,새해복많이
"""
_a = list(map((lambda letter: hex(ord(letter))),(list('HAPPY NEW YEAR 2018'))))
print(_a)

_b = [ord(num) for num in list('HAPPY NEW YEAR 2018')]
print(_b)

for num in _a:
    print(chr(eval(num)), end='')
print()

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

_a = b'\xeb\xac\xb4\xec\x88\xa0\xeb\x85\x84,\xec\x83\x88\xed\x95\xb4\xeb\
\xb3\xb5\xeb\xa7\x8e\xec\x9d\xb4'.decode('utf-8')
print(_a)
