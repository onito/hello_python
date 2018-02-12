""" 문제. winsound 모듈의 beep() 메서드를 이용해서 소리를 내라
 - 미션.1 = beep() 메서드의 인자(파라미터)를 알아내라
 - 미션.2 = 37에서 200에 +50씩 증가하면서 소리를 낸다.
 - 미션.3 = 소리를 낼때마다, "n번째 발성을 하였습니다. 파라미터는 (무엇)입니다."
   * (1) 미지의 모듈 발견!
   * (2) 공식 Documentation 검색 - 이것이 최후의 바이블!
   * (3) 영어가 어려우니, 한글 블로깅
   * (4) 커뮤니티의 도움을 받는다.
    - StackOverFlow.com = 전세계 네임드 해커가 모여있는 갓갓지식인!
    - tutorialspoints.com = Example이 친절히 잘 되어있음 (특정모듈)
"""
import winsound

def test_play_alias():
    sound_names = [
        'SystemAsterisk',
        'SystemExclamation',
        'SystemExit',
        'SystemHand',
        'SystemQuestion']

    i = 0
    while i<len(sound_names):
        print("\n\n{}. {} is playing....".format(
            i+1,
            sound_names[i]),
            flush=True)

        winsound.PlaySound(sound_names[i], winsound.SND_ALIAS)
        i += 1
# test_play_alias()

def test_play_scale():
    # 37 through 32,767
    NOTE_HERTZ = {
        'c0': (37,65,131,262,523,1046.5,2093),
        'cs': (37,69,139,277,554,1109,2217.5),
        'd0': (37,73,147,294,587,1175,2349),
        'ds': (39,78,156,311,622,1244.5,2489),
        'e0': (41,82,165,330,659,1318.5,2637),
        'f0': (44,87,175,349,698.5,1397,2794),
        'fs': (46,92.5,185,370,740,1480,2960),
        'g0': (49,98,196,392,784,1568,3136,),
        'gs': (52,104,208,415,831,1661,3322.5),
        'a0': (55,110,220,440,880,1760,3520),
        'as': (58,116.5,233,466,932,1865,3729),
        'b0': (62,123.5,247,494,988,1975.5,3951),
        'C0': (65,131,262,523,1046.5,2093,4186)}

    keys = NOTE_HERTZ.keys()

    for i in range(7):
    # for i in range(5):
        for key in list(keys):
            hertz = NOTE_HERTZ[key][i]

            if key[1] == '0':
                print(key, hertz, type(hertz))
                winsound.Beep(int(hertz), 500)
# test_play_scale()



""" -------------- Window beep sound :: Play DO-RE-MI Song :
  refer to : Gist.github - https://goo.gl/7BzDDy
  reference blog : http://freeprog.tistory.com/353
"""
import time
import math

TEMPO = 80    # playing speed = 1000

DICT_NOTE = {   # DICT_NOTE = do, re, mi, pa, sol, ra, ti --->  Hz
    'do':261, 're':293, 'mi':329, 'pa':349, 'sol':391, 'ra':440, 'ti':493,
    'DO':530, 'RE':590, }
A_NOTES = [
    'do', 'mi', 'mi', 'mi', 'sol', 'sol', 're', 'pa', 'pa', 'ra', 'ti', 'ti',
    'sol', 'do', 'ra', 'pa', 'mi', 'do', 're',
    'sol', 'do', 'ra', 'ti', 'DO', 'RE', 'DO','end']
A_TEMPOS = [
    4, 2, 6, 4, 2, 6, 4, 2, 6, 4, 2, 8,
    6, 6, 4, 4, 4, 4, 8,
    4, 4, 4, 4, 4, 4, 8, 0]

def play_notes(notes, tempos):
    for note, tempo in list(zip(notes, tempos)):
        if note == 'end':
            break

        print("{:>3} : ({} Hrz.) __ {:4,}".format(
            note,
            DICT_NOTE[note],
            int(tempo*TEMPO)))

        winsound.Beep(DICT_NOTE[note], int(tempo*TEMPO))

def main_abc_song():
    if len(A_NOTES) == len(A_TEMPOS):
        print("...Numbers of Notes & Tempos are all the same!...")

    while True:
        play_notes(A_NOTES, A_TEMPOS)

        if input('\n\n\nSTOP(y/NO)?').lower().startswith('y'):
            break

""" -------------- Window beep sound :: calculating Hz :
#   refer to : stack overflow .com = 440 Hz is A4.
#   reference blog : https://goo.gl/k89nFG
#    - FRENCH SONG: "au clair de la lune"!! 'r' is a rest
"""

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
            winsound.Beep(NOTES[note], int(PERIOD(tempo)*1000))
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
    main_abc_song()    # continueous playing
    # main_au_clair()    # play 2 times



# TODO :
"""
(1) 인덱싱과 슬라이싱 : POS 번호
(2) 스파게티 코드
"""
