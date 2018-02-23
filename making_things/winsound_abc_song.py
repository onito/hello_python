""" 화일 독스트링 : 윈도우사운드 모듈사용 소리 발성하기
 - 미션.1 = ABC송 연주
 - 미션.2 = Au de claire .. 연주
"""
import math
import time
import winsound as wins

def 야_씨피구사구_스크립트에한글좀쓰자():
    """ 아톰 스크립트런 패지키에서 한글 깨지는 문제 해결을, 대한히 한국적으로 해결!
     - 스크립트런 모듈을 작성해 놓은 곳이, 부모 디렉토리 인 문제 발생
     - os.path.dirname(__file__) = 화일이 있는 위치의 path 정보
     - dirname 을 *중복*해서 사용할때 마다, 부모 디렉토리 path로 한칸씩 올라간다.
     - 다른 방법도 있지만, 아무~~!! 생각없이 쓰기 좋다.
      (이거 알아내기 위해서 깃헙와 스택오버플로 좀 많이 뒤졌다, 이게 제일 낫다)
     - 미친 듯한 반복사용은 좀 없어 보이니 두단계 이상은 쓰지말자.. (더좋은 방법있다)
    """
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    import _script_run_utf8
    _script_run_utf8.main()
야_씨피구사구_스크립트에한글좀쓰자()

def 발성연습_마이크테스트_아아():
    """ 파이썬3 은 유니코드를 지원, 한글변수,매소드명 작명가능(추천하지 않음)
     - 피씨구사구 = 윈도우 한글코드
     - 발성연습_마이크테스트_아아() = 주파수와 길이를 사용하여, Beep()함수로
     - PC스피커에 소리를 만들어내는 함수.
    """
    hrz = 37
    tempo = 200
    for i in range(1, 11):
        wins.Beep(hrz, tempo)
        time.sleep(0.3)
        print("{:2} 번째 발성이 끝났습니다-->  {:3} Hrz, {:} tempo.".format(
            i, hrz, tempo),
            flush=True)
        hrz += 50
# 발성연습_마이크테스트_아아()

# ---- 고난이도 연주 (1)ABC / (2)오드클레..
def song_abc():
    """ -------------- Window beep sound :: Play DO-RE-MI Song :
      refer to : Gist.github - https://goo.gl/7BzDDy
      reference blog : http://freeprog.tistory.com/353
    """
    TEMPO = 1000    # playing speed = 1000
    # DICT_NOTE = do, re, mi, pa, sol, ra, ti --->  Hz
    DICT_NOTE = {
        'do':261, 're':293, 'mi':329, 'pa':349, 'sol':391, 'ra':440, 'ti':493,
        'DO':530, 'RE':590, }

    A_NOTES = [
        [['do', 'mi', 'mi', 'mi', 'sol', 'sol', 're', 'pa', 'pa', 'ra', 'ti', 'ti'],
         [4, 4, 2, 4, 4, 2, 4, 4, 2, 4, 4, 2]],

        [['sol', 'do', 'ra', 'pa', 'mi', 'do', 're'],
         [1, 1, 1, 1, 1, 1, 0.5]],

        [['sol', 'do', 'ra', 'ti', 'DO', 'RE', 'DO']+['end'],
         [1, 1, 1, 1, 1, 1, 0.5]+[0]],
        ]
        # print(len(A_NOTES))         # n = 3
        # print(len(A_NOTES[0]))      # n = 2
        # print(len(A_NOTES[0][0]))   # n = 12

    def show_a_score(a_notes):  # Score of note
        print('__'*40)
        print('PLAYING NOTES for DO-RE-MI')
        print('..'*40)
        for num in  range(len(a_notes)):
            print(a_notes[num][0])        # ['do', 're', 'me', ...]
        print()
        print('__'*40)

    def get_ziped_music(a_notes): # IN= 'list' / OUT= ZIP_OBJ
        note = []
        hrzs = []
        for num in range(len(a_notes)):   # n=3
            note += a_notes[num][0]
            hrzs += a_notes[num][1]
        return zip(note, hrzs)

    def get_play_sound(zip_music):      #IN= ZIP_OBJECT
        for key, duration in list(zip_music):
            if key != 'end':
                wins.Beep(DICT_NOTE[key], int(TEMPO/duration))
            else:
                pass
                # return False  # play once ...
        return True             # play repeatedly ...

    if __name__ == '__main__':
        # print(A_NOTES[1][0])
        # print(len(A_NOTES))

        show_a_score(A_NOTES) # play 2 times
        for i in range(2):
            zip_music = get_ziped_music(A_NOTES)
            get_play_sound(zip_music)

def song_au_clair():
    """ -------------- Window beep sound :: calculating Hz :
      refer to : stack overflow .com = 440 Hz is A4.
      reference blog : https://goo.gl/k89nFG
       - FRENCH SONG: "au clair de la lune"!! 'r' is a rest
    """
    import time
    import math

    LABELS = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']

    # the PERIOD expressed in second, computed from a tempo in bpm
    PERIOD = lambda tempo: 1/(tempo/60)
    NAME = lambda n: LABELS[n%len(LABELS)] + str(int((n+(9+4*12))/12))
    FREQUENCY = lambda n: int(440*(math.pow(2, 1/12)**n))
    NOTES = {NAME(n): FREQUENCY(n) for n in range(-42, 60)}

    # play each note in sequence through the PC speaker at the given tempo
    def play(song, tempo):
        for note in song.lower().split():
            if note in NOTES.keys():
                wins.Beep(NOTES[note], int(PERIOD(tempo)*1000))
            else:
                time.sleep(PERIOD(tempo))

    def show_notes_hrz():
        column_count = 1
        for key, value in zip(NOTES.keys(), NOTES.values()):
            print('%3s:%6s' %(key, value), end="   ")
            column_count += 1

            if column_count == 6:
                print()
                column_count = 0


    def main_au_clair():
        show_notes_hrz()

        for i in range(2):
            play(('c4 c4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
                  'c4 C4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '
                  'd4 d4 d4 d4 a3 r a3 r d4 c4 B3 a3 g3 r r r '
                  'c4 c4 c4 d4 e4 r d4 r c4 e4 d4 d4 c4 r r r '), 180)
            # tempo = 180 bpm...

    if __name__ == '__main__':
        main_au_clair()    # play 2 times

if __name__ == '__main__':
    song_abc()
    song_au_clair()
