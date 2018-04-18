""" DIRS + [tab] = 스니펫 설정하기
 -  DIRS, ifn, . for [python]
"""
import os
import sys

DIRS = os.path.dirname(__file__).partition("hello_python")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)
sys.path.append(os.path.join(ROOT , "_static", "module_custom", ""))

# --- 스크립트런에서 한글사용 커스텀모듈 --------------------
import _script_run_utf8
_script_run_utf8.main()

# -----플레이 오브젝트에 대한 모듈을 사전에 정의 -------------
from game_character import Character
from game_player import Player, Warrior, Magician
from game_monster import Monster, FireMonster, IceMonster


def status_obj_creation():
    print("\n\n")
    print("총 오브젝트=", Character._total_count)
    print("=========================")
    print("플레이어  =", Player._total_count)
    print("--------------")
    print(" 전 투 병 =", Warrior._total_count)
    print(" 마 법 사 =", Magician._total_count, "\n")

    print("몬스터괴물 =", Monster._total_count)
    print("--------------")
    print("  불꽃괴물 =", FireMonster._total_count)
    print("  얼음괴물 =", IceMonster._total_count)



if __name__ == '__main__':
    a = Warrior()
    b = Magician()
    c = FireMonster()
    d = IceMonster()
    e = IceMonster()

    status_obj_creation()

""" Artificial Intelligent
  - AWS 소개 동영상
  - 아마존 알렉사 보이스
  - 라즈베이파이 셋업
"""
