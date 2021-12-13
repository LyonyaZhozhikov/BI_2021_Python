#!/usr/bin/env python3

# start
# Objectives: ++++ path
# 1. wc - word count | -l lines -w words -c bytes

# Additional:
# 1. grep "pattern" file_to_look_in_for.txt | -

#
import os
import sys
import argparse


def run(args):
    def count_lines(args):
        lines = 0
        for line in args.filename:
            lines += 1
        sys.stdout.write(str(lines))

    def count_words(args):
        words = 0
        for line in args.filename:
            words += len(line.split(" "))
        sys.stdout.write(str(words))

    def count_bytes(args):
        sys.stdout.write(sys.getsizeof(args.filename))
    whole = str(count_lines(args.filename), count_words(args.filename), count_bytes(args.filename))
    sys.stdout.write(whole)

def main():
    parser = argparse.ArgumentParser(description="Displays list of files in directory")
    parser.add_argument('filename', help="input text file", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-l', help="Showing lines", dest="lines", action='store_false')
    parser.add_argument('-w', help="Showing words", dest="words", action='store_false')
    parser.add_argument('-c', help="Showing bytes", dest="bytes", action='store_false')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
