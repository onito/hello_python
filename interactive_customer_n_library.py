"""
# class function definition
# Library class = show available / lend book / restore book
# Customer class = borrow book / return book /
# : https://www.udemy.com/python-oops-beginners/learn/v4/t/lecture/7359328
"""
import os
import sys
import pickle

BOOK_LIST_FILE = 'book_list_v00.pdb'
BOOK_LIST = ['도라에몽', '나루토', '진격의거인', '공각기동대', '페트레이버',
             '포켓몬스터', '케모노프렌즈']

""" MAKE 3 CONSTANTS
# (1) FILE_DIR
# (2) DESTIN_DIR = _log dir.    # destination directory
# (3) FILENAME_WITH_DIR = DESTIN_DIR + BOOK_LIST_FILE
"""
FILE_DIR = os.path.dirname(__file__)
ROOT_WORD = 'hello_python'            # root directory
if ROOT_WORD in FILE_DIR:
    DESTIN_DIR = FILE_DIR.strip().split(ROOT_WORD)[0] + \
                ROOT_WORD + '\\_static\\_log\\'
else:
    print("*** ROOT_WORD IS MISSING ***")
    quit()

FILENAME_WITH_DIR = DESTIN_DIR + BOOK_LIST_FILE

print('(1) log_dir  = %s'% DESTIN_DIR)    # D:\My Documents\GitHub-2\hello_python
print('(2) file_dir = %s'%FILE_DIR)    # D:\My Documents\GitHub-2\hello_python


class Library(object):
    def __init__(self, available_book_list):
        self.available_book_list = available_book_list

    def show_available_books(self):
        print('\n\nAvailable books - 현재, 대출 가능목록.\n', '=='*20)
        for index, book in enumerate(self.available_book_list, 1):
            print('{:2}.{}'.format(index, book))

    def lend_book(self, request_book):
        self.request_book = request_book
        if self.request_book in self.available_book_list:
            print("O.K!.. '%s' is lended.. thank you!"% request_book)
            self.available_book_list.remove(request_book)
        else:
            print("Sorry, '%s' is not available at this moment! "% request_book)

    def restore_book(self, returned_book):
        self.returned_book = returned_book
        if self.returned_book not in self.available_book_list:
            print("O.K.. '%s' is successfully returned!.. Thank you!"% returned_book)
            self.available_book_list.append(self.returned_book)
        else:
            print("Sorry.. '%s' is already on the shelves.. double check.pls"% returned_book)

    def is_exist_file(self):
        pass

    def get_read_file_from_pickle(file_name_with_dir):
        if os.path.exists(file_name_with_dir):
            with open(file_name_with_dir, mode='rb') as f:
                # IPORTANT(!) : f = _io.BufferReader, not "file_name_with_dir"
                loaded_data = pickle.load(f)
            return loaded_data
        else:
            print("SORRY!! ... pickle file doesn't exists ...", flush=True)

    def write_new_booklist(self, available_book_list, file_name_With_dir):
        """ if data file is not exist, write available_book_list on a new file
        # - if it isn't exists, write a pickle file and show "it is done!"
        # - if it is, show "It already exists on a file"
        """
        if not os.path.exists(file_name_With_dir):
            with open(file_name_With_dir, mode='wb') as f:
                pickle.dump(available_book_list, f)
            print("*** A NEW WRITE PROCESS HAS BEEN DONE ***", flush=True)
        else:
            print("IT'S O.K!! ...IT ALREADY EXISTS! ...", flush=True)



library = Library(BOOK_LIST)
library.write_new_booklist(BOOK_LIST, FILENAME_WITH_DIR)



# class Customer(object):
#     def borrow_book(self):
#         self.lend_book = input('...Enter book title you want to borrow :\n')
#         return self.lend_book
#
#     def return_book(self):
#         self.returned_book = input('...Enter tilte of return book? :\n')
#         return self.returned_book
#
#
#
# library = Library(BOOK_LIST)
# customer = Customer()
#
# while True:
#     print('\n\n\nLIBRARY MENU\n', '=='*20)
#     print(' 1 - show available book list')
#     print(' 2 - lend book')
#     print(' 3 - return book')
#     print(' 4 - quit menu')
#
#     try:
#         customers_choice = int(input())
#     except:
#         os.system('cls')
#         continue
#
#     if customers_choice is 1:
#         library.show_available_books()
#
#     elif customers_choice is 2:
#         request_book = customer.borrow_book()
#         library.lend_book(request_book)
#
#     elif customers_choice is 3:
#         return_book = customer.return_book()
#         library.restore_book(return_book)
#
#     else:
#         quit()
