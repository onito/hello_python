''' 일기를 추가할 때는 '아래' 템플릿을 이용합니다.(이미 있는 날짜는 기록 안 됨)
add_dict_one = {
2018_03_15:
""" 드디어, 축구시즌 개막!
축구리그가 개막 되었습니다.
새로운 시즌에 대한 기대만발!!
""",
}
'''

# 아래 딕셔너리를 추가하고 실행 시키면, '피클'에 추가 됩니다.
add_dict_one = {
}

add_dict_many = {
2000_0101:
"""(예시) 제목/내용
기본내용은
이렇게 적습니다.
""",

2018_0303:
"""축구시즌이 시작되었습니다.
축구리그 개막전이 어제 시작되었습니다.
올 시즌에는 좋은 성적을 거둬야 할텐데
""",

2018_0305:
"""일기장 마무리 되어감
화일2개로 와리가리 하느라 헷갈린다.
누가, 누구를 참조하는 것인지
리모트에서 일기를 추가하는 기능을 만들자
내용을 전부 보여주고, 추가여부를 묻는 것
하자..
""",

2018_0307:
"""아.. 헷갈린다
누가, 누굴 참조하는 것인지..
결국 if __name__ = '__main__'이
중요한 역할을 하게 되는 것을...
백업 '피클'도 만들어 놓자..
많은 데이터가 한꺼번에 날라간다면?
아아... 생각하기에도 끔찍하다.
""",

2018_0308:
"""'피클'데이터는 수정불가
내용은 보이지만 직관적이지 않다.
결국 데이터 백업기능을 넣어야 할까..
많은 데이터가 한방에... 숑~!!
으으으...
""",

}


# 이미 기록 된 날짜는 '중복저장'이 되지 않습니다.
if __name__ == '__main__':
    # 상위 DIR의 모듈을 실행하기 위한 코드 (3단계 상위)
    import sys
    from os.path import dirname
    root_dir = dirname(dirname(dirname(__file__)))
    sys.path.append(root_dir)

    # 전체 보기로 내용을 확인한 후에..
    import _pickled_diary as d
    d.show_diary_all_by(add_dict_many)

    FILE_NAME_WITH_DIR = './wimpy_diary_dict.pck'

    # '피클'에 저장 할 것인지를 물어본다..
    _input = input('피클에 추가할 까요? (y/NO=Ent)  : \n')
    if _input.strip().lower().startswith('y'):
        # 맨 처음 실행되면, '픽클' 값을 먼저 채워보자.. 없으면 초기값으로 채워짐.
        DIARY_DICT = d.get_dict_from_pickle(FILE_NAME_WITH_DIR)

        # DIARY_DICT 에 내용을 추가 해 보자 - 데이터: temp_dict_one, temp_dict_many
        print(" - single add   = %s "% bool(add_dict_one))
        print(" - multiple add = %s \n"% bool(add_dict_many))

        if add_dict_one:
            _result = d.add_one_to_diary_dict(add_dict_one, DIARY_DICT)
            print(_result)

        if add_dict_many:
            _result = d.add_many_to_diary_dict(add_dict_many, DIARY_DICT)
            print(_result)

        # 피클을 저장(write)하고 끝낸다.
        if add_dict_one or add_dict_many:
            d.finish_after_update_pickle(FILE_NAME_WITH_DIR, DIARY_DICT, mode=1)

        d.main(DIARY_DICT)
