# bookmark script for learning
# author - cycl0pz
import sys
from datetime import datetime

# cycl0pz@debian -> python3 bookmark.py [page number]
def log_file(page_number):
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(current_time + " ~> " + page_number + " written [+]")
    with open("bookmark.md", "a") as bookmark:
        bookmark.write("\n" + current_time + " ~> " + page_number + " ")


if __name__ == '__main__':
    arg_length = len(sys.argv)
    for i in range(1, arg_length):
        log_file(sys.argv[i])

