import argparse
import webbrowser
import subprocess
import sys
import os

def define_new_parser():
    my_parser = argparse.ArgumentParser(description="Which webseite to look for something.", usage="&(prog)s [url]\
                                                                                                    [\"key-word\"]")

    my_parser.add_argument("[url]", help="The url you want to open.", metavar="")

    my_parser.add_argument(("[key-word]"), help="The element you want to search in the website.")
    return my_parser



def open_safari():
    subprocess.run(["python3", "./start_programms.py", "TextEdit"])

def open_website(website):
    webbrowser.open_new(website)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        my_parser = define_new_parser()
        my_parser.parse_args()
        open_safari()
        open_website(sys.argv[1])
    elif len(sys.argv) < 3:
        sys.stdout.write("Too few Arguments.")
    else:
        sys.stdout.write("Too many Arguments.")