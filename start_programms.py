#!/usr/bin/env python
import argparse
import sys
import subprocess

def define_parser_with_arguments():
    my_parser = argparse.ArgumentParser(description="Open Application.", usage="%(prog)s [-h|--help] [App-Name]")
    my_parser.add_argument("[App-Name]", help="The Name of the Programm you want to start.")
    return my_parser

def open_programm():
    output = subprocess.run(["open", "-a", sys.argv[-1]], stdout=subprocess.PIPE)
    if output.returncode != 1:
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.stdout.write("Too many Arguments")
        exit()
    my_parser = define_parser_with_arguments()
    args = my_parser.parse_args()
    fail_to_open = open_programm()
    if fail_to_open:
        sys.stdout.write("Unable to open Programm.")
        exit()
