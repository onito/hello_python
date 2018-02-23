""" 화일 - 독스트링
기능 : 메서드 (함수정의)
  (1) 책목록 보여주기 (List)
  (2) 책 빌리기 (Borrow)
  (3) 책 반납하기 (Return)
  (4) 시스템에서 나가기(Q)
"""
# import random

BOOK_LIST = ["흑집사", "국어사전", "타임즈"]

def get_show_menu_list():
    """ 함수 : 독스트링 (Doc-String)
      - 메뉴를 보여주고, 매뉴입력값을 반환한다.
    """
    print("\n\n")
    print("----------------------")
    print("1. 대출 가능한 리스트")
    print("2. 대출하기")
    print("3. 반납하기")
    print("4. 시스템에서 나가기(Q)")
    print("----------------------")
    return input("메뉴의 번호를 선택해 주세요 : \n").strip()

def show_book_list():
    """ 대출가능한 북 리스트를 보여준다.
      - (예) p1 = 너 이름을 적는다.
      - (예) p2 = 너의 애인 이름을 적는다.
    """
    print("=== 대출가능한 책리스트 ===")
    for i, book_name in enumerate(BOOK_LIST, 1):
        print("{}. {}".format(i, book_name))
    print()

def return_book():
    returned_book = input("반납할 책 제목을 입력하세요 :\n").strip()
    BOOK_LIST.append(returned_book)
    print("'{}'이 반납됬습니다. 감사합니다...\n\n".format(returned_book))

def borrow_book():
    borrowed_book = input("빌려갈 책 제목을 입력하세요 :\n").strip()
    if borrowed_book in BOOK_LIST:
        BOOK_LIST.remove(borrow_book)
        print("'{}'이 반납됬습니다. 감사합니다...\n\n".format(borrowed_book))
    else:
        print("죄송합니다.'{}'란 책은 없습니다....\n\n".format(borrowed_book))


def main():
    print("... 도서관 시스템에 접속하였습니다 ...")
    while True:
        answer = int(get_show_menu_list())

        if answer == 1:
            show_book_list()

        elif answer == 2:
            borrow_book()

        elif answer == 3:
            return_book()

        else:
            break

    print("\n\n이용해 주셔서 감사합니다...")
#
if __name__ == '__main__':
    main()
    # import library_list_add_remove
    # help(library_list_add_remove)
