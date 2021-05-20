# -*- coding: UTF-8 -*-
import argparse
import webbrowser
import subprocess
import sys
import urllib.request
import os

def define_new_parser():
    my_parser = argparse.ArgumentParser(description="Which webseite to look for something.", usage="&(prog)s [url]\
                                                                                                    [\"key-word\"]")

    my_parser.add_argument("[url]", help="The url you want to open.", metavar="")

    my_parser.add_argument(("[key-word]"), help="The element you want to search in the website.")
    return my_parser



def open_safari():
    subprocess.run(["python3", "./start_programms.py", "Safari"])

def open_website(website):
    safari = webbrowser.get("Safari")
    response = safari.open(website, new=1, autoraise=0)
    safari.open_new_tab("www.google.de")
    if not response:
        sys.stdout.write("Could not open Browser.")

def get_html_content(website):
    my = urllib.request.urlopen(website)
    mbytes = my.read()
    with open("source_code.txt", 'wb') as f:
        f.write(mbytes)

def search_code_for_inforamtion(search_key):
    with open("source_code.txt") as f:
        lines = f.read()
    cmp = []
    one_char = ""
    idx = 0
    max_idx = len(search_key) - 1
    for line in lines:
        for ch in line:
            try:
                one_char = ch.encode("utf-8")
            except UnicodeError:
                print(ch, "Geht nicht")

            if one_char == search_key[idx]:
                cmp.append(one_char)
                idx += 1
            else:
                cmp = []
                idx = 0
                if idx == max_idx:
                    return cmp
    return 1




if __name__ == "__main__":
    sys.argv.append("https://www.loremipsum.de")
    sys.argv.append("At vero")
    if len(sys.argv) == 3:
        my_parser = define_new_parser()
        my_parser.parse_args()
        #open_safari()
        get_html_content(sys.argv[1])
        #open_website(sys.argv[1])
        print(search_code_for_inforamtion(sys.argv[-1]))

    elif len(sys.argv) < 3:
        sys.stdout.write("Too few Arguments.")
    else:
        sys.stdout.write("Too many Arguments.")