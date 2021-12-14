#!/usr/bin/env python3

# start
# 2. cat - reading/viewing files | -

#
import sys
import argparse


def run(args):
    text = args.filename
    reading_cat = text.read()
    sys.stdout.write(reading_cat)


def main():
    parser = argparse.ArgumentParser(description="Reading cat")
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
