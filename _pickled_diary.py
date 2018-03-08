""" 피클을 이용한 화일 read(=load) & dump(=write)
  - pickle.load(f) : 객체(f)를 읽어서 올린다.
  - pickle.dump(data, f) : 객체(f)에 데이터(data)를 덤프한다.
 """
import os
import sys
import time
import datetime
import pickle

FILE_NAME_WITH_DIR = './_static/_pickle/wimpy_diary_dict.pck'

def write_pickle(file_name_with_dir, diary_dict):
    with open(file_name_with_dir, 'wb') as f:
        pickle.dump(diary_dict, f)

def read_pickle(file_name_with_dir):
    try:
        with open(file_name_with_dir, 'rb') as f:
            return pickle.load(f)                   # 값 존재 = 성공
    except FileNotFoundError:
        # print('ERROR : 화일이 없어 읽을수가 없네요...')
        return 0                                    # 실패'0'을 반환한다.

def get_dict_from_pickle(file_name_with_dir):
    # DIARY_DICT 에 내용을 '피클'화일에서 읽어오자..
    init_dict = { 2000_0101:
    """(예시) 제목/내용
    기본내용은
    이렇게 적습니다.
    """}
    if not read_pickle(file_name_with_dir):
        # 피클화일이 없으면 일단, 기본내용을 쓰고 읽어오자.
        write_pickle(file_name_with_dir, init_dict)
    return read_pickle(file_name_with_dir)

def finish_after_update_pickle(file_name_with_dir, diary_dict, mode=0):
    write_pickle(file_name_with_dir, diary_dict)
    # print("\n\n\n", DIARY_DICT)
    print("\n\n\n")
    print("... 변경 된 dict를 '피클' 저장하고 종료합니다... \n\n")
    # sys.exit()            # 또는 내장함수 quit()를 사용한다.
    if not mode:
        quit()

def get_ymd_weekday_by(int_digits_8, language=1):
    key_str = str(int_digits_8)
    year, month, day = key_str[:4], key_str[4:6], key_str[6:]
    weeks = [('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'),
             ('월', '화', '수', '목', '금', '토', '일')]
    week_num = datetime.date(int(year),int(month),int(day)).weekday()
    return year, month, day, weeks[language][week_num]       # '월'~ '일'

def show_diary_number(key, diary_dict):
    year, month, day, weekday = get_ymd_weekday_by(int_digits_8=key, language=1)
    date = "%s년 %s월 %s일 (%s요일)"% (year, month, day, weekday)

    contents = diary_dict[key].strip().split('\n')  # 내용을 리스트로 만듬
    print('--'*20)                                  # -------
    print(date)
    print('--'*20)                                  # -------
    print(contents[0])                              # 제목
    print('^^'*15)                                  # .......
    for content in contents[1:]:                    # 나머지 내용들
        print(content)
    print('--'*20 + '\n\n')                         # -------

def show_diary_all_by(diary_dict, line_by=0):
    # 모든 키값을 다 읽어보자...
    keys = list(diary_dict.keys())
    keys.sort(reverse=True)
    print('모든 키값으로 읽어오기 모드 :\n', "총 자료 (%d 건)\n" % len(keys), keys )
    for key in keys:
        show_diary_number(key, diary_dict)

def show_diary_title_by(diary_dict, line_by=0, instruction=':키값 입력:'):
    print("총'%s 건'이 있습니다.."% len(diary_dict))
    keys = list(diary_dict.keys())
    keys.sort(reverse=True)
    # print(keys)
    print('--'*25)
    print('번호..[.날짜.]........[.......제......목.......]')
    print('--'*25)

    for i, key in enumerate(keys, 1):
        year, month, day, weekday = get_ymd_weekday_by(key, 1)
        title = diary_dict[key].strip().split('\n')[0]
        print("%2s. %s.%s/%s (%s) - %-20s"% (
            i, year, month, day, weekday, title))
    print('--'*25)
    return input(instruction+'\n\n').strip()

def add_one_to_diary_dict(add_dict, diary_dict):
    # DIARY_DICT 에, 1개 일기(temp_dict_one)를 추가해 보자
    key = list(add_dict.keys())[0]
    value = list(add_dict.values())[0]

    if key in list(diary_dict.keys()):  #키 값이 겹치나?
        print("*** ERROR: 변경하려는 키값('%d')이 중복 됩니다. ***\n" % key)
        return 0

    else:
        diary_dict[key] = value
        print("... DIARY_DICT('%d')를 업데이트 하였습니다...\n" % key)
        return 1

def add_many_to_diary_dict(add_dicts, diary_dict):
    # DIARY_DICT 에, 여러개의 일기(temp_dict_many)를 추가해 보자
    for key in add_dicts:      # 순차적으로 키값을 읽어온다
        _dict = dict()
        _dict[key] = add_dicts[key]
        _result = add_one_to_diary_dict(_dict, diary_dict)
    return _result

def main(diary_dict):
    while True:
        # 몇 개의 일기가 있나, 확인해 보자
        instruction = ':키값 입력: (V)iew / (A)ll / (M)od / (D)el / (Q)uit\n'
        _input = show_diary_title_by(diary_dict, instruction=instruction)
        time.sleep(1)
        os.system('cls')

        # 특정 키값(날짜)로 DIARY 내용을 읽어보자..
        mode = _input[:1]        # V, A, M, D

        if mode.upper().startswith('V'):
            key_int = int(_input[2:])         # 날짜 8자리 'int'
            show_diary_number(key_int, diary_dict)

        elif mode.upper().startswith('A'):
            show_diary_all_by(diary_dict)

        elif mode.upper().startswith('Q'):
            # 변경된 dict를 '피클'에 기록하고, 종료해 보자
            finish_after_update_pickle(FILE_NAME_WITH_DIR, diary_dict)

        else:
            print('...알 수 없는 코맨드 입니다..', flush=True)
            time.sleep(1)
            os.system('cls')
            continue




if __name__ == '__main__':
    # 맨 처음 실행되면, '픽클' 값을 먼저 채워보자.. 없으면 초기값으로 채워짐.
    DIARY_DICT = get_dict_from_pickle(FILE_NAME_WITH_DIR)

    def add_one_n_many_dict_from_separated_module():
        from _static._pickle.pickle_add_data import add_dict_one
        from _static._pickle.pickle_add_data import add_dict_many
        print(" - single add   = %s "% bool(add_dict_one))
        print(" - multiple add = %s \n"% bool(add_dict_many))

        if add_dict_one:
            add_one_to_diary_dict(add_dict_one, DIARY_DICT)

        if add_dict_many:
            add_many_to_diary_dict(add_dict_many, DIARY_DICT)
    # DIARY_DICT 에 내용을 추가 해 보자 - 데이터: temp_dict_one, temp_dict_many
    # add_one_n_many_dict_from_separated_module()

    main(diary_dict=DIARY_DICT)
