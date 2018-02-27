import os
import sys

# print(os.path.dirname(__file__))                    # present-dir
# print(os.path.dirname(os.path.dirname(__file__)))   # upper-dir
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# for path in list(sys.path):
#     print(path)
import making_things._xmas_tree._xmas_tree3 as xtr

def show_information():
    print(help(xtr))
    print(dir(xtr))
    print(xtr)
# show_information()

xtr.show_stacked_body(0,5,0)
xtr.show_stacked_body(3,7,0)
xtr.show_stacked_body(3,11,0)
xtr.show_stacked_body(5,21,0)
xtr.show_trunk(2)
xtr.show_ground(width=79)
