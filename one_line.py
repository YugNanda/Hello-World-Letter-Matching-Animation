# Python Guide + 99 Projects: https://resources.legitpython.com/python-ebook-download

import time
import string
import shutil
import os
import sys

letters = list(string.ascii_lowercase + string.ascii_uppercase + '!,\' ')
target = "If you found this video helpful, don't forget to like and share it with your friends!"

current_str = ""

while current_str != target:
    for letter in letters:
        new_str = current_str + letter
        terminal_width = shutil.get_terminal_size().columns
        wrapped_text = '\n'.join([new_str[i:i + terminal_width] for i in range(0, len(new_str), terminal_width)])

        sys.stdout.write("\033[H\033[J")
        sys.stdout.write(wrapped_text)
        sys.stdout.flush()

        time.sleep(0.007)

        if new_str == target[:len(new_str)]:
            current_str = new_str
            break

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')  
wrapped_target = '\n'.join([target[i:i + terminal_width] for i in range(0, len(target), terminal_width)])
print(wrapped_target)
