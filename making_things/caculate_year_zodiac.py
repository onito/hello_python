"""
    calculate year zodiac
"""
import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
DIRS = os.path.dirname(__file__).partition("hello_python\\")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)

import _script_run_utf8
_script_run_utf8.main()

THIS_YEAR = 2008        # 무자년(쥐띠해) = 2008년 -- 기준년으로 계산용
TARGET_YEAR = 1592      # 임진년(용띠해) = 1592년 --> 확인용

_answer = THIS_YEAR - TARGET_YEAR


_zodiac = '자축인묘진사오미신유술해'  # 12개
_year = '갑을병정무기경신임계'        # 10개
_number = '4567890123'              # 10개

gap = dict(zip(_number, _year))
print(gap)          # show dict
print(_zodiac + str(_answer))      # 421

# print(len(_year))
# print(len(_zodiac))

_f = _answer%12         # rest = 1
_g = _answer//12        # value = 35
# print('_answer %% 12 = %s : go backward'%_f)   # 1

_key_gap = str(TARGET_YEAR)[-1]

_key_zod = 12-_f

if _key_zod == 12:
    _key_zod = 0

print('\n\n' + gap[_key_gap] + _zodiac[_key_zod] + '년')
