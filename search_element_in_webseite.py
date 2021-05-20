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



if __name__ == "__main__":
    sys.argv.append("http://www.google.de")
    sys.argv.append("hello world")
    if len(sys.argv) == 3:
        my_parser = define_new_parser()
        my_parser.parse_args()
        #open_safari()
        get_html_content(sys.argv[1])
        #open_website(sys.argv[1])

    elif len(sys.argv) < 3:
        sys.stdout.write("Too few Arguments.")
    else:
        sys.stdout.write("Too many Arguments.")