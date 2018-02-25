FILE_DIR ='./_static/_pdb/'
FILE_NAME = 'test1_file_rw.pdb'
DATA = '안녕하세요 반갑습니다.\n한번 쯤 뵙고싶었습니다.\n안녕히계세요'

""" 스크립트런 실행시 한글을 쓸수 있게 해주는 모듈 """
import _script_run_utf8
_script_run_utf8.main()

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
    with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8') as f:
        string1 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
        string2 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
        string3 = f.readline()   # 호출 할때마다 한줄씩 순서대로 불러온다
        for string in [string1, string2, string3]:
            print(string)

    """ 특별한 방법 : f객체를 이용하는 방법 """
    with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8') as f:
        for line in f:
            print(line)

def test4_read(FILE_NAME=FILE_NAME):
    with open(FILE_DIR+FILE_NAME, mode='r', encoding='utf8') as f:
        bundle_string = f.read()

    print(bundle_string)


if __name__ == '__main__':
    # test1_write()
    test2_readlines()

    # # test4_read('i_have_a_dream.pdb')
    # with open(FILE_DIR+'i_have_a_dream.pdb', mode='r', encoding='utf8') as f:
    #     strings = f.readlines()    # 리스트 자료를 'strings'에 할당한다.
    #
    # import time
    #
    # # print(strings)
    #
    # for string in strings:
    #     time.sleep(0.2)
    #     print(string, flush=True, end='')
