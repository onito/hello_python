""" 암호화 문구 : 키보드의 상하좌우 배치를 기준으로 '방향 쉬프트' 한다.
 - 첫번째 : 왼쪽으로 시프트(암호화) --> 오른쪽으로 시프트(복호화)
 - 두번째 : 반대 방향으로 실행체크
 - 세번째 : 위로 시프트 (암호화) --> 아래로 시프트(복호화)
 - 네번째 : 반대 방향으로 실행체크
"""
# 키보드 배열에 대한 2차원 '리스트'
keys = [
        ['1','q','a','z'],
        ['2','w','s','x'],
        ['3','e','d','c'],
        ['4','r','f','v'],
        ['5','t','g','b'],
        ['6','y','h','n'],
        ['7','u','j','m'],
        ['8','i','k',','],
        ['9','o','l','.'],
        ['0','p',';','/'],
        ['-','[',"'",'shift-1'],
        ['=',']','enter','shift-2'],
        [' ','sp1','sp2','sp3'],
    ]
string = 'moon light took me by surprise, ligkt coming from your eyes.' # O.K
string = 'come over here at once!'      # 특수기호 '!' 문제해결 필요
string = 'I have a Dream..'             # 대문자 사라짐 -
string = "'when the morning come', [i'll be out for work]"      # O.K

def get_shift_left(string):
    lefted_list = []
    for letter in string:
        for key in keys:
            if letter in key:
                num1 = keys.index(key)      # 첫번째 [인덱스]
                num2 = key.index(letter)    # 두번째 [인덱스]
                lefted_list.append(keys[num1-1][num2])

    encrypted_word = ""
    for letter in lefted_list:
        encrypted_word += letter

    return encrypted_word

def get_shift_right(string):
    righted_list = []
    for letter in string:
        for key in keys:
            if letter in key:
                num1 = keys.index(key)      # 첫번째 [인덱스]
                num2 = key.index(letter)    # 두번째 [인덱스]
                righted_list.append(keys[num1+1][num2])

    encrypted_word = ""
    for letter in righted_list:
        # print(letter)
        encrypted_word += letter

    # Replace special key -- d[2='q', d[3='a'. d[4='z'
    encrypted_word = encrypted_word.replace('d[2','q')
    encrypted_word = encrypted_word.replace('d[3','a')
    encrypted_word = encrypted_word.replace('d[4','z')

    return encrypted_word

# left --> right
print(string)
print(get_shift_left(string))
print(get_shift_right(get_shift_left(string)))



# right --> left : Error
# print(get_shift_right(string))
# print(get_shift_left(get_shift_right(string)))



# [0]을 기준으로 '종'으로 이동 -- 1열 증가
# print(keys[0][0])
# print(keys[1][0])
# print(keys[2][0])
# print(keys[-1][0])

# [0]을 기준으로 '횡'으로 이동 -- 2열 증가
# print(keys[0][-4])          # [0]
# print(keys[0][-3])
# print(keys[0][-2])
# print(keys[0][-1])
# print(keys[0][0])
# print(keys[0][1])
# print(keys[0][2])
# print(keys[0][3])

# for letter in string:
#     for key in keys:
#         if letter in key:
#             num1 = keys.index(key)      # 첫번째 [인덱스]
#             num2 = key.index(letter)    # 두번째 [인덱스]
#             print("%s = [%2s] [%2s] / shift_left = [%2s][%2s] = %s" % (
#                 letter,
#
#                 num1,
#                 num2,
#
#                 num1-1,
#                 num2,
#
#                 keys[num1-1][num2]
#                 ))
