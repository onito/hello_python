import sys
import time
"""
Python's standard out is buffered (meaning that it collects some of the data
"written" to standard out before it writes it to the terminal).
Calling sys.stdout.flush() forces it to "flush" the buffer, meaning that it
will write everything in the buffer to the terminal,
even if normally it would wait before doing so.

Here's some good information about (un)buffered I/O and why it's useful:
http://en.wikipedia.org/wiki/Data_buffer
Buffered vs unbuffered IO
"""
for n in range(100):
    print('1 ', end='')
    sys.stdout.flush()
    time.sleep(0.1)

# for n in range(100):
#     sys.stdout.write('1 ')
#     sys.stdout.flush()
#     __import__("time").sleep(0.5)
