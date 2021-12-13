#!/usr/bin/env python3

# start
# 2. ls - files list | -a all files

#
import os
import sys
import argparse


def run(args):
    if args.all_files:
        ls_comm = next(os.walk(f'{args.path}'))[1] + next(os.walk(f'{args.path}'))[2]
        for i in ls_comm:
            sys.stdout.write(i)
            sys.stdout.write('\n')
    elif not args.all_files:
        ls_comm = next(os.walk(f'{args.path}'))[2]
        for i in ls_comm:
            sys.stdout.write(i)
            sys.stdout.write('\n')


def main():
    parser = argparse.ArgumentParser(description="Displays list of files in directory")
    parser.add_argument('-path', help="Please use brackets if your path contains spaces", type=str, dest="path",
                        default=".")
    parser.add_argument('-a', help="Showing hidden files as well. Default = off", dest="all_files",
                        action='store_true')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
