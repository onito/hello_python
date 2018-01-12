""" 파이썬 베이직 :: 복습02 - 변수와 객체 :: 변수할당 원리
 (1) 자료(데이터의 종류)
  - 문자: str(스트링), chr(캐릭터) <=> ord(아스키번호)
  - 숫자: int(인테저=정수), float(플로트=실수), complex(허수)
  - 데이터: list(리스트)와 dict(사전) - tuple
 (2) 데이터 포맷 / 인덱싱과 슬라이싱
  - 스트링 포맷 '%s'%(para),
  - 고급 포맷함수 '{}'.format(para)
  - 인덱싱 = 객체[pos], 객체[pos][pos][pos]...
  - 슬라이싱 = 객체[pos:pos]  객체[-1:-pos]
 (3) 리스트 객체함수 : use dir()
   - clear, append, pop, count, remove, sort, reverse..
 (4) 딕트 객체함수 : use dir()
   - clear, get, items, keys, values, pop..
 """

# '스크립트런' 에서 UTF-8 한글을 표시해주기 위한 (자체제작)모듈
# import _script_run_utf8
# _script_run_utf8.main()


""" immutable(불변) 과 mutable(가변) 의 개념
 (1) 변수는 할당하는 것이 아니라, 객체를 가르키는 것(포인팅)
 (2) 불변:이뮤터블(immutable)과 가변:뮤터블(mutable)의 정의
    - 변수가 여러개 - 이뮤터블 객체는 동일 객체를 가르킴
    - 변수가 여려개 - 뮤터블 객체는
 (3) 객체의 특징 - 속성(attributes)과 기능(Methods)
 (4)
"""

_dict = [1, 2, 3, 4]
_dict_a = _dict

print('\n',id(_dict),'\n', id(_dict_a))
