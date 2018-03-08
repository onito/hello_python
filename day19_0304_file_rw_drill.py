import _script_run_utf8
_script_run_utf8.main()

TEST_TEXT1 = """*~~블라블브라
*~~오늘은 날씨
*~~오후에는
*~~저녁에는
*~~맛있게
"""

TEST_TEXT2 = "오늘은 일요일 입니다.\n" +\
             "오늘은 날씨가 좋습니다.\n" +\
             "오후에는 나가서 놀아야 합니다.\n" +\
             "저녁에는 밥을 먹습니다.\n" +\
             "맛있게 먹습니다.\n"


# print(TEST_TEXT1)
# print(TEST_TEXT2)

def write():                    # 화일명으로 data를 기록한다.
    """
    f = open('./_static/_pdb/day18-1_text.pdb', 'w', encoding='utf8')
    f.write(TEST_TEXT2)
    f.close()
    """

    with open('./_static/_pdb/day18-1_text.pdb', 'w', encoding='utf8') as f:
        f.write(TEST_TEXT1)

    with open('./_static/_pdb/day18-1_text.pdb', 'a', encoding='utf8') as f:
        f.write(TEST_TEXT2)

write()

def read_lines():               # List 형 자료를 반환한다
    pass

def read():                     # 한묶음의 전체 스트링을 반환한다.
    pass

def read_line():                # 첫번째 줄을 반환하고, 삭제한다.
    pass
