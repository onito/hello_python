""" 피클을 이용한 화일 read(=load) & dump(=write)
  - diary_dict = pickle.load(f) : 객체(f)를 읽어서 올린다.
  - pickle.dump(diary_dict, f) : 객체(f)에 데이터(dict)를 덤프한다.
"""
import os
import pickle

FILE_DIR = './_static/_pickle/'
FILE_NAME = 'wimpy_diary_dict.pck'
FILE_NAME_WITH_DIR = FILE_DIR + FILE_NAME


def get_dict_read_pickle(file_name_with_dir):
    with open(file_name_with_dir, 'rb') as f:
        return pickle.load(f)

def write_init_pickle_file(file_name_with_dir):
    """ 만약 화일이 존재하지 않으면, 기본 화일(dict)을 만든다 """
    if os.path.isfile(file_name_with_dir):
        print("...이미 피클화일이 존재합니다...", flush=True)

    else:
        diary_dict = {
            0: ['날짜포맷(yyyy-mm-dd)',
                '제목 한줄..',
                '내용은 간단히 씁니다..'], }
        with open(file_name_with_dir, 'wb') as f:
            pickle.dump(diary_dict, f)

        print('...기본 피클화일을 새로 만들었습니다.', flush=True)

def show_loaded_diary_dict(diary_dict):
    for key in diary_dict:
        print('____________________')
        for line in diary_dict[key]:
            print(line)

def add_dict_pickle(diary_dict, add_list):
    add_key = max(diary_dict.keys()) + 1
    diary_dict[add_key] = add_list
    print("add_list 가 추가되었습니다.")

from _static._pickle import pickle_data_add1 as pda



write_init_pickle_file(FILE_NAME_WITH_DIR)
diary_dict = get_dict_read_pickle(FILE_NAME_WITH_DIR)

while True:
    for add_list in pda.add_lists:
        add_dict_pickle(diary_dict, add_list)

    show_loaded_diary_dict(diary_dict)

    if input('\n\n한번 더 반복기록?(y=Enter/n)').lower().startswith('n'):
        with open(FILE_NAME_WITH_DIR, 'wb') as f:
            pickle.dump(diary_dict, f)
            print('... 피클이 성공적으로 업데이트 되었습니다 ...')
            print('... 실행을 종료합니다. ...')
        break

    print('... 다이어리를 다시 한번 중복해서 기록합니다 ...')
