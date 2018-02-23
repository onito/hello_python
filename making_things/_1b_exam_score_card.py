""" 임의의 과목 (총점/평균) 성적표 만들기

  - 리스트로 입력받음 "국어.영어.수학.사회.과학.미술" - 점으로 구분함
  - 리스트로 입력받음 "98 95 78     100 87 99" - 스페이스, 실수할수도 있음.

  - 출력된 결과
 ----------
  입력된 값 = [98, 95, 78, 100, 87, 99]


  총 과목 수 (6 건)
  _________________________
  1.국어 :  98 점
  2.영어 :  95 점
  3.수학 :  78 점
  4.사회 : 100 점
  5.과학 :  87 점
  6.미술 :  99 점
  _________________________
    총 점 : 557.00 점
    평 균 :  92.83 점
"""

import _script_run_utf8
_script_run_utf8.main()

SEPARATOR = '_'*25

def is_play_again():
    return input("\nplay again? (y/[N])?\n").startswith('y')

def test01_score():
    # subjects = input("과목을 입력해 주세요 / '.'으로 구분 : ").strip().split(".")
    # scores = input("{:} ".format(len(subjects))+"과목에 대한 점수를 입력하세요"+
    #     "/ 공백으로 구분 : ").strip().split()
    # 테스트용 인풋 데이터
    subjects = "국어.영어.수학.사회.과학.미술".strip().split(".")
    scores = "98 95 78     100 87 99".split()
    splited_scores = [int(score) for score in scores]

    print('입력된 값 = %s\n\n'% splited_scores)
    print('총 과목 수 ({} 건)'.format(len(subjects)))
    print(SEPARATOR)
    for i, title in enumerate(subjects):
        print(' {:}.{}: {:3} 점'.format(i+1, title, splited_scores[i]))
    print(SEPARATOR)

    total = 0
    for n in range(len(subjects)):
        total += splited_scores[n]

    print('  총 점 : {:6.2f} 점'.format(float(total)))
    print('  평 균 : {:6.2f} 점'.format(total/len(subjects)))

while True:
    test01_score()
    if not is_play_again():
        break
