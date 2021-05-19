#!/usr/bin/env python
import argparse
import sys


def define_parser_with_arguments():
    my_parser = argparse.ArgumentParser(description="Open Application.")
    my_parser.add_argument("-a", "--app", help="Application Name.", type=str, metavar="")
    return my_parser

def check_for_invalid_flags():
    valid_falgs = ["a", "--app"]
    for flag in sys.argv[1:]:
        if flag not in valid_falgs:
            return 1

if __name__ == "__main__":
    invalid_flag_found = check_for_invalid_flags()
    if invalid_flag_found:
        sys.exit()
    my_parser = define_parser_with_arguments()
