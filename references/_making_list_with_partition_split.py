""" 상위/하위 패쓰 지정, 파티션(), 스플릿()의 차이
os.path.dirname(__file__) = 현재 화일이 위치한 워킹 DIR.
os.path.append(PATH) = 시스템 패쓰에, 새로운 DIR-PATH를 추가한다.

# 리스트를 만들때 ROOT_DIR 를 리스트 맴버로 포함하느냐, 빼느냐의 문제
# 포함할때 = 파티션()
# 제외할대 = 스플릿()
"""
import os
import sys

WORK_DIR = os.path.dirname(__file__)
ROOT_WORD = 'k_mooc_reboot'                 # root directory
ROOT_DIR = WORK_DIR.partition(ROOT_WORD)[0] + WORK_DIR.partition(ROOT_WORD)[1]
PICKLE_WITH_DIR = ROOT_DIR + '\\_static\\_log\\'

print("WORK_DIR = ", WORK_DIR)
print("ROOT_DIR = ", ROOT_DIR)

print("partition(ROOT_WORD)=", WORK_DIR.partition(ROOT_WORD))
print("split(ROOT_WORD)=", WORK_DIR.partition(ROOT_WORD))
