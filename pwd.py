#!/usr/bin/env python3

# start
# 0.1 pwd - shows current directory

#
import os
import argparse
import sys


def run(args):
    sys.stdout.write(os.getcwd())


def main():
    parser = argparse.ArgumentParser(description="Displays current working directory")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
