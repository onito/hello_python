import os
import sys

def decorator(func):
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            work_dir, file_list = kwargs['work_dir'], kwargs['file_list']
        elif len(args) == 1:
            work_dir, file_list = args, kwargs['file_list']
        else:       # len(args) == 2:   error: >3
            work_dir, file_list = args

        print(work_dir)
        print('---------------\n'
              'TOTAL:', len(file_list), 'files\n'
              '---------------')
        func(*args, **kwargs)
        print('---------------')
        # return func(*args, **kwargs)
    return wrapper

def get_dir(upper_step=0):
    while True:
        d = os.path.dirname
        dir_depths =  [
            d(__file__),                # 0     = current dir (work_dir)
            d(d(__file__)),             # -1    = upper 1
            d(d(d(__file__))),          # -2    = upper 2
            d(d(d(d(__file__)))),       # -3    = upper 3
            d(d(d(d(d(__file__))))),    # -4    = upper 4   ... END!
            ]
        try:
            return dir_depths[abs(upper_step)]
        except IndexError:
            print("Error: OUT OF RANGE.. 0 <= upper_step <=-4")

def get_files(work_dir):
    return os.listdir(work_dir)

@decorator
def show_file_list(work_dir, file_list):
    file_list.sort(reverse=True)
    for i, _file in enumerate(file_list, 1):
        print(' %2s:  %s ' % (i, _file))

def main():
    work_dir = get_dir()          # 기본값 = -1 = 현재위치
    show_file_list(work_dir=work_dir, file_list=get_files(work_dir))



""" if __name__ 로 경계를 치면, 외부 모듈호출 때 자체 실행을 방지한다. """
if __name__ == '__main__':

    _="""*** _files_dirs_run 스크립트 용도 :
    -------------------------
     - ATOM '아톰' 에디터와 'CMD'에서 './, ../' 인식이 다름!
     - 모듈실행 = 현재 모듈위치(dirname(__file__)) 장식자 리스트를 보여줌
     - get_dir(upper_step=0)    : 상위스텝의 dir(str)을 반환한다. (0=현재)
     - get_files(work_dir)      : 워킹dir(str)의 화일'list'값을 반환한다
     - show_file_list(work_dir, file_list)
                                : 데코레이트 화일리스트를 보여준다.
    """
    print('\n'+_)
    main()



""" 코드 리팩터링 : 버리고, 간단히 줄였음.
    if upper_step > 0:

    if upper_step == 0:
        return d(__file__)
    elif upper_step == -1:
        return d(d(__file__))
    elif upper_step == -2:
        return d(d(d(__file__)))
    elif upper_step == -3:
        return d(d(d(d(__file__))))
    elif upper_step == -4:
        return d(d(d(d(d(__file__)))))
    elif upper_step == -5:
        return d(d(d(d(d(d(__file__))))))
    else :
        print('... 상위 5스텝까지만 허용가능...')
        return False
"""
