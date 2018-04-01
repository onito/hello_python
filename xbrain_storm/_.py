""" 루트 디렉토리를 생성 ('스크립트런'에서 발생하는 문제점 해결)
  - '../' './' '\\', 절대경로, 상대경로 인식에서 '스트링'에러발생
  - 매서드를 이용해서, 절대경로, 상대경로를 인식 시켜 줌.
    (윈도우 command 창과 Script-run 실행결과가 동일해 짐 )
"""
import os
import time

DIRS = os.path.dirname(__file__).partition("hello_python\\")
ROOT = DIRS[0] + DIRS[1]
# print(ROOT); quit()       # 테스트용.

filename_with_dir = os.path.join(ROOT, '_static', '_pdb', "i_have_a_dream.pdb")
# filename_with_dir = os.path.join(ROOT, '_static', '_pdb', "you_have_a_dream.pdb")

try:
    for line in open(filename_with_dir, 'r').readlines():
        print(line, end='', flush=True)
        time.sleep(0.2)

except FileNotFoundError:
    print("** ERROR: Filename missing *** :\n %s" % filename_with_dir, flush=True)
