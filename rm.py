#!/usr/bin/env python3

# start
# 4. rm - remove files | -r removes directories

#
import os
import shutil
import sys
import argparse


def run(args):
    if args.directory_specified:
        shutil.rmtree(args.filename)
    elif not args.directory_specified:
        os.remove(args.filename)



def main():
    parser = argparse.ArgumentParser(description="Deletes files or directories if specified")
    parser.add_argument('filename', help="command to delete tagged file",
                        type=str, default=sys.stdin)
    parser.add_argument('-r', help="command to delete tagged directory", dest="directory_specified",
                        action='store_true')
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
