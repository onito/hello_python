""" 틱택토 게임 만들기(TIC-TEC-TOE) :
인벤트 위드 파이썬(Invent with Python) - 제10장. 틱택토 게임 참조
http://inventwithpython.com/chapter10.html
"""
import os
import random

# board = ["O" if n%3==0 else "x" for n in [random.randint(1, 99) for i in range(13)]]
KIND = ("o", "x", " ")
LETTER = "x"

def get_input_player_letter():
    """ ['', ''] 리스트 값을 반환한다
    # 선공을 누가할 것인지를 정한다. 첫 공격이'x'면 후자는 자동'o'가 선택 됨
    # 리스트를 반환하는데, [0]값이 휴먼 / [1]값이 컴퓨터이다.
    """
    letter = ""

    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        # the first element in the list is the player’s letter,
        # the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def get_random_board_list(kind_list):
    """ 랜덤 보드 값을 리턴한다 """
    return [kind_list[(n%3)] for n in [random.randint(1,999) for i in range(10)]]

def show_board_with(board):
    """ 말 배치 리스트(String[10])를 읽어서 틱택토 보드판에 배치한다
     - board = [0, ... 9]  10개의 리스트
     - 인덱스[0]은 그냥 무시한다 (버리는 값)

     test: show_board_with([str(n) for n in range(10)])
     ------------------------------
        +---+---+---+
        | 1 | 2 | 3 |
        +---+---+---+
        | 4 | 5 | 6 |
        +---+---+---+
        | 7 | 8 | 9 |
        +---+---+---+
    """
    row = 1
    print ("+---+---+---+")
    for n in range(1, 10, 3):
        if row != 3:
            print("| {:} | {:} | {:} |".format(board[n],board[n+1],board[n+2]))
            print ("+---+---+---+")
        else:
            print("| {:} | {:} | {:} |".format(board[n],board[n+1],board[n+2]))
            print ("+---+---+---+")
        row += 1
    print ("\n\n")

def is_stop_playing():
    """ 그만 할것인지 참/거짓 값을 반환한다 / 참 일때 break
    # 스톱 플래잉 = 'n' 를 입력하면 True 를 반환 (break)
    # 엔터를 입력하면 False를 반환한다 (반복실행 한다)
    """
    print("다시 한번 하시겠습니까? ([Y]es=엔터 or [N]o)")
    return input().lower().startswith('n')

def is_winner(board, letter):
    """
    # 빈 칸에 착수를 했을 때, 공격자(letter)가 승리인지 판단한다
    # - board[n] 이 빈칸(" ") 이라면 착수 가능하다.
    # - board.append(n, letter) 로 착수를 한다
    # - 착수한 이후에 승리인지 판단하여 반환한다 (True/False)
    """
    bool_win =(\
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter) or

        (board[7] == letter and board[4] == letter and board[1] == letter) or
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter) or

        (board[7] == letter and board[5] == letter and board[3] == letter) or
        (board[9] == letter and board[5] == letter and board[1] == letter))
    return bool_win

def is_free_space(board, pos):
    """ 보드 포지션 번호가 공백(" ")인지 참/거짓값을 반환한다
    # board = 10 자리 보드 리스트
    # pos = index_number / position_number
    # -----------------------------------
    # 원래하고자 했던 논리식 보다 훨씬, 간단하게 처리할 수 있다.
    # if board[pos] == " ":
    #     return True
    # else:
    #     return False
    """
    return board[pos] == " "



while True:
    # show_board_with([" " for n in range(10)])
    # show_board_with(["X" for n in range(10)])
    # show_board_with(["O" if n%2==0 else "x" for n in range(13)])
    board = get_random_board_list(KIND)
    show_board_with([str(n) for n in range(10)])
    show_board_with(board)

    print("승자 x? = %s"% is_winner(board, "x"))
    print("승자 o? = %s"% is_winner(board, "o"))
    print()

    for n in range(1, 10):
        if is_free_space(board, n):
            available_mark = "("+str(n)+")"
        else:
            available_mark = " - "

        if n%3 != 0:
            print("%-3s"% available_mark, end=" ")
        else:
            print("%-3s"% available_mark, end=" \n")
    print("\n\n")

    if is_stop_playing():
        break

    os.system('cls')
