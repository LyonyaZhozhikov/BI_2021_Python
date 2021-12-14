#!/usr/bin/env python3

# start
# 0.2 mkdir - creates a directory | -p creates a directory structure with the missing parent ones

#
import os
import sys
import argparse


def run(args):
    if args.path_specified:
        os.makedirs(args.filename)
    elif not args.path_specified:
        os.mkdir(args.filename)


def main():
    parser = argparse.ArgumentParser(description="Creates directories and paths if specified")
    parser.add_argument('filename', help="command to create tagged dir",
                        type=str, default=sys.stdin)
    parser.add_argument('-p', help="command to create tagged path of dirs", dest="path_specified",
                        action='store_true')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
