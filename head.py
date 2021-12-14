#!/usr/bin/env python3

# start
# 3.1 head - display first 10 lines of the file | -n x / -x to specify number of lines

#
import sys
import argparse


def run(args):
    lines = args.filename.readlines()
    n = int(args.number_lines)
    first_lines = lines[:n]
    for i in first_lines:
        sys.stdout.write(''.join(i))


def main():
    parser = argparse.ArgumentParser(description="Displays first 10 lines in files if not specified")
    parser.add_argument('filename', help="input text file", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-n', help="entered number of lines like this -n=1", dest="number_lines", default=10)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
