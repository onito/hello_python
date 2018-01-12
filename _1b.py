import _script_run_utf8
_script_run_utf8.main()

SEPARATOR = '_'*25

def test01_score():
    # _c_arr = input('국영수 성적을 입력하시오. 예) 56, 67, 78 : \n')
    # 테스트용 인풋 데이터
    _c_title = ['국어', '영어', '수학', '사회', '과학', '미술']
    _c_arr = '98,  95,78,100, 87, 99'
    striped_data = _c_arr.replace(' ','')
    striped_int_data = [int(data) for data in striped_data.split(',')]

    print('입력된 값 = %s\n\n'% striped_int_data)
    print('총 과목 수 ({} 건)'.format(len(_c_title)))
    print(SEPARATOR)
    for i, title in enumerate(_c_title):
        print(' {:}.{}: {:3} 점'.format(i+1, title, striped_int_data[i]))
    print(SEPARATOR)

    total = 0
    for n in range(len(_c_title)):
        total += striped_int_data[n]

    print('  총 점 : {:6.2f} 점'.format(float(total)))
    print('  평 균 : {:6.2f} 점'.format(total/len(_c_title)))
# test01_score()
