""" '피클'드 게시판 글쓰기
  - pickle.load(f) : 객체(f)를 읽어서 올린다.
  - pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
  - week_num = datetime.date(2018, 06, 12).weekday() : 요일

모듈 컨트롤 : 스크립트런으로 ../ ./ 제어가 되지 않음.
os.path.dirname(__file__) = 현재 폴더명
dirname(dirname(__file__)) = 한 단계 상위 폴더명
sys.path.append(폴더명,) = 시스템폴더에 PATH 추가
os.path.isfile(finame)
os.path.isdir(path)
"""
import time
import datetime
import pickle

import _script_run_utf8
_script_run_utf8.main()

FILENAME_WITH_DIR = "./_static/_pickle/pickled_dict.pck"

def write_pickle(filename_with_dir, data):
    with open(filename_with_dir, 'wb') as f:
        pickle.dump(data, f)

def read_pickle(filename_with_dir):
    while True:
        try:
            with open(filename_with_dir, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("ERROR:화일이 없습니다..")
            _data = { 1000_01_01:
            """ (예시)제목/내용
            본문 작성요령은
            이렇게 작성합니다.
            """,
            }
            write_pickle(filename_with_dir, _data)
            print('... 기본 화일을 작성하였습니다 ...')
            continue

def add_dict_to_dict(dict_a, dict_b):           # [OUT]: dict_a, overwrapped
    overwrapped = 0
    for key in dict_b:
        if key in dict_a.keys():
            overwrapped += 1
        else:
            dict_a[key] = dict_b[key]
    return dict_a, overwrapped

def get_year_month_day_Week_with(int_digits_8):
    key = str(int_digits_8)
    year, month, day = key[:4], key[4:6], key[6:]
    week_num = datetime.date(int(year), int(month), int(day)).weekday()
    week_id = [
        '월화수목금토일',
        ('Mon','Tue','Wed','Thu','Fri','Sat','Sun'),]
    print(week_id[1][week_num])
# get_year_month_day_Week_with(20140312)


#  맨 처음 '피클'을 읽어와서 'BOARD_DICT'에 저장한다
BOARD_DICT = read_pickle(FILENAME_WITH_DIR)

from _static._pickle.pickle_add_data import add_dict_many
BOARD_DICT, repeat = add_dict_to_dict(BOARD_DICT, add_dict_many)
print("중복데이터 : ('%s건')" % repeat )

INSTRUCTION = "(V)eiw / (A)dd / (Q)uit"

print('----------------------------------------------\n'
      '번호....날짜......[제.....목]...............\n'
      '----------------------------------------------')
board_idx = dict()
for i, key in enumerate(BOARD_DICT, 1):
    board_idx[i] = key
    title = BOARD_DICT[key].strip().split("\n")[0]
    print("%2s. [%s] - %s" % (i, key, title))

print('----------------------------------------------\n'
      ':입력 키값: %s\n' % INSTRUCTION )
_input = input()

if _input.upper().startswith('V'):
    key_num = int(_input.strip().split('_')[1])         # board_idx.values()
    if key_num in board_idx.keys():
        print(BOARD_DICT[board_idx[key_num]])
    else:
        print('... 게시물이 존재하지 않습니다 ...')

elif _input.upper().startswith('Q'):
    write_pickle(FILENAME_WITH_DIR, data=BOARD_DICT)
    print('\n\n\n...피클저장을 완료하였습니다...')

else:
    print('... 알 수 없는 명령어 ...')




def lecture_today():
    """ '피클'드 게시판 글쓰기
      - pickle.load(f) : 객체(f)를 읽어서 올린다.
      - pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
      - week_num = datetime.date(2018, 06, 12).weekday() : 요일
     """
    import os
    import time
    import datetime
    import pickle

    """ 스크립트런에 한글을 쓰기위한 모듈 """
    import _script_run_utf8
    _script_run_utf8.main()

    FILENAME_WITH_DIR = "./_static/_pickle/pickled_board.pck"

    def write_pickle(filename_with_dir, data):
        """ 끝나기 전에 저장한다. """
        with open(filename_with_dir, 'wb') as f:
            pickle.dump(data, f)

    def get_read_pickle(filename_with_dir):
        """ 시작 할 때 제일먼저 실행한다 """
        with open(filename_with_dir, 'rb') as f:
            return pickle.load(f)

    def show_board_list(board_dict):
        print("총 데이터: ('%s건')"% len(board_dict))
        print("----------------------------------------------")
        print("번호....날짜......[제.....목]...............")
        print("----------------------------------------------")

        for i, key in enumerate(board_dict ,1):
            # print(i, BOARD_DICT[key].split('\n')[0])
            title = board_dict[key].split('\n')[0]
            print("%s. [%s] - %s"% (
                i,
                key,
                title,
            ))
        print("----------------------------------------------")
        print(":입력 키값: (V)eiw / (A)dd / (Q)uit")

    def show_detail_view(board_dict, key):
        key_str = str(key)
        year, month, day = key_str[:4], key_str[4:6], key_str[6:]
        title = board_dict[key].split('\n')[0]
        content = board_dict[key].replace( title+'\n', '')

        print("%s (%s.%s.%s)" % (title, year, month, day))
        print("-------------------------------------")
        print("%s"% content)
        print("-------------------------------------")
        input("돌아가기=엔터")
        os.system('cls')
        show_board_list(board_dict)

    # del (BOARD_DICT[20180308])
    # del (BOARD_DICT[20180307])
    # del (BOARD_DICT[20180305])
    # show_detail_view(BOARD_DICT, 20180308)

    BOARD_DICT = get_read_pickle(FILENAME_WITH_DIR) # (함수) 피클를 불어와 저장한다.
    show_board_list(BOARD_DICT)                     # (함수)게시글 목록을 보여준다.

    while True:
        order = input('명령을 입력하세요 V_날짜형식') # str = 'v_20180308'

        if order[0].upper().startswith('V'):            # VIEW
            key = int(order.split('_')[1])
            os.system('cls')
            show_detail_view(BOARD_DICT, key)

        elif order[0].upper().startswith('D'):          # DELETE
            print(".. 아직 'DEL' 명령어가 없습니다..")
            pass

        elif order[0].upper().startswith('A'):          # ADD
            print(".. 아직 'ADD' 명령어가 없습니다..")
            pass

        elif order[0].upper().startswith('Q'):          # SAVE & QUIT
            print("\n\n\n.. 화일을 저장하고 종료합니다 ..")
            write_pickle(FILENAME_WITH_DIR, BOARD_DICT)
            quit()

        else:
            print('.. 주인님, 명령어를 이해하지 못했습니다 ..')
            os.system('cls')
            show_board_list(BOARD_DICT)
