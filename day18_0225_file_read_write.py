import os
import time

FILE_DIR ='./_static/_pdb/'
COUNTING = 0

""" 스크립트런 실행시 한글을 쓸수 있게 해주는 모듈 """
import _script_run_utf8
_script_run_utf8.main()

def test0_practice():
    FILE_DIR ='./_static/_pdb/'
    FILE_NAME = 'test1_file_rw.pdb'
    DATA = '안녕하세요 반갑습니다.\n한번 쯤 뵙고싶었습니다.\n안녕히계세요'

    def test1_write():
        """
        # f = open(FILE_DIR+FILE_NAME, mode='w')
        # f.write(DATA)
        # f.close()
        """
        with open(FILE_DIR+FILE_NAME, mode='w', encoding='utf-8') as f:
            f.write(DATA)

    def test2_readlines(FILE_NAME=FILE_NAME):
        """ 한줄씩 끊어서, 리스트로 반환한다 """
        with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf-8') as f:
            strings = f.readlines()   # 리스트를 반환 한다

        print(strings)
        print('\n\n')

        for string in strings:
            print(string)

    def test3_readline(FILE_NAME=FILE_NAME):
        """ 호출() 할때마다 한줄씩 순서대로 불러온다 """
        with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf-8') as f:
            string1 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
            string2 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
            string3 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
            for string in [string1, string2, string3]:
                print(string)

        """ 특별한 방법 : f 객체를 이용하는 방법 """
        with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line)

    def test4_read(FILE_NAME=FILE_NAME):
        with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf-8') as f:
            bundle_string = f.read()

        print(bundle_string)

    # test1_write()
    # test2_readlines()
    # test4_read('i_have_a_dream.pdb')

    def main():
        with open(FILE_DIR+'i_have_a_dream.pdb', mode='r', encoding='utf8') as f:
            strings = f.readlines()    # 리스트 자료를 'strings'에 할당한다.

        print(strings)
        input()

        for string in strings:
            time.sleep(0.5)
            print(string, flush=True, end='')

    if __name__ == '__main__':
        main()

    pass

def test1_with_open_file_rw():
    """ 화일을 읽고 쓰는 방법, 연습
     - 인코딩에 따라 저장하는 방법이 달라진다. (기본인코딩='None')
     - 기타 : 함수 밖의 변수를 수정할 때, 글로벌 선언!
       : 글로벌 선언 시, 상수는 외곽에 있어야 한다.
     """
    FILE_NAME = FILE_DIR + 'test_rw_file.pdb'
    NEW_STRING = """첫번째: 안녕하세요~ 반갑습니다."""
    ADD_LINE = """저는 아무개 입니다."""

    def write_file_with_mode(string, mode, file_name=FILE_NAME):
        global COUNTING
        with open(file=file_name, mode=mode, encoding='utf8') as f:
            f.write(string)
        COUNTING += 1
        print("%s. ___ The writing is done! ..."% COUNTING)

    def show_read_file(file_name):
        with open(file_name, 'r', encoding='utf8') as f:
            contents = f.read()
            print(contents)

    def show_readlines_file(file_name):     # copy
        with open(file_name, 'r', encoding='utf8') as f:
            contents = f.readlines()
            print(contents)


    if __name__ == '__main__':
        write_file_with_mode(NEW_STRING, 'w',  FILE_NAME)
        write_file_with_mode(ADD_LINE, 'a',  FILE_NAME)
        write_file_with_mode('\n' + NEW_STRING + ADD_LINE, 'a',  FILE_NAME)

        show_read_file(FILE_NAME)
        # show_readlines_file(FILE_NAME)

def test2_i_have_a_dream():
    """ 흑인인권, 마틴루터킹 목사 연설
      (1) 객체(f)에서 하나씩 불러오기
      (2) 객체(f)를 리스트로 만들어 하나씩 불러오기
    """
    FILE_NAME = FILE_DIR + 'i_have_a_dream.pdb'

    def show_readlines_file(file_name):     # copy - helper()
        with open(file_name, 'r', encoding='utf8') as f:
            return f.readlines()

    def using_object_to_list():
        """ (1) f 객체를 리스트로 전환, 이용하는 방법 """
        lines = show_readlines_file(FILE_NAME)
        lines.remove('\n')

        for line in lines:
            time.sleep(0.3)
            print(line, end='', flush=True)

    def using_object_itself():
        """ (2) f 객체, 자체를 이용하는 방법 """
        with open(FILE_NAME, 'r', encoding='utf8') as f:
            for line in f:
                time.sleep(0.3)
                print(line, end='', flush=True)


    if __name__ == '__main__':
        using_object_to_list()
        # using_object_itself()

def is_file_exist(file_name):
    """ file exist(), file remove()
     - os.path.exists(file_dir) : dir 이 존재하나?
     - os.path.isfile(filename) : file 이 존재하나?
     - os.remove(file_name) : 화일을 삭제한다.
    """
    file_name_with_dir = FILE_DIR + file_name

    if os.path.isfile(file_name_with_dir):
        return True
    else:
        return False

def set_remove_file(file_name):
    file_name_with_dir = FILE_DIR + file_name

    if os.path.exists(file_name_with_dir):
        os.remove(file_name_with_dir)
        print("\n\n...'%s' 화일을 삭제하였습니다.."% file_name)
    else:
        print("\n\n...'%s'을 찾을수 없습니다. 삭제불능.."% file_name_with_dir)


if __name__ == '__main__':
    # test1_with_open_file_rw()
    test2_i_have_a_dream()

    file_name = 'test_rw_file.pdb'

    if is_file_exist(file_name):
        print("...'%s' 화일이 이미 있습니다."% file_name, flush=True)
    else:
        print("...'%s'을 찾을수 없습니다..."% file_name, flush=True)

    # time.sleep(2)
    # set_remove_file(file_name)
    # print(" '%s' 화일이 남아있는가? : "% file_name, is_file_exist(file_name))
    # pass




# TODO :
"""
(1) 인덱싱과 슬라이싱 : POS 번호 - enumerate()
(2) 스파게티 코드
"""
