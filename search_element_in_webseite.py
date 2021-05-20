#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import argparse
import sys
from urllib.request import urlopen

def define_new_parser():
    my_parser = argparse.ArgumentParser(description="Which webseite to look for something.", usage="&(prog)s [url]\
                                                                                                    [\"key-word\"]")

    my_parser.add_argument("[url]", help="The url you want to open.", metavar="")

    my_parser.add_argument(("[key-word]"), help="The element you want to search in the website.")
    return my_parser




def get_html_content(website):
    my = urlopen(website)
    print(my)
    mbytes = my.read()
    with open("source_code.txt", 'wb') as f:
        f.write(mbytes)

# def search_code_for_inforamtion(search_key):
#     with open("source_code.txt") as f:
#         lines = f.read()
#     cmp = []
#     one_char = ""
#     idx = 0
#     max_idx = len(search_key) - 1
#     for char in lines:
#         try:
#             one_char = char.encode("utf-8")
#         except UnicodeError:
#             print(char, "Geht nicht")
#         if one_char == search_key[idx]:
#             cmp.append(one_char)
#             idx += 1
#         else:
#             cmp = []
#             idx = 0
#             if idx == max_idx:
#                 return cmp
#     return 1




if __name__ == "__main__":
    sys.argv.append("https://www.otto.de/technik/heimkino/")
    sys.argv.append(["LG DSN4 2.1 2.1 Soundsystem (Bluetooth, 300 W)",
                     "Panasonic SC-HTB510 2.1 Soundbar (Bluetooth, WLAN (WiFi), 240 W, mit kabellosem Subwoofer)"])
    if len(sys.argv) == 3:
        my_parser = define_new_parser()
        my_parser.parse_args()
        get_html_content(sys.argv[1])

    elif len(sys.argv) < 3:
        sys.stdout.write("Too few Arguments.")
    else:
        sys.stdout.write("Too many Arguments.")