#!/usr/bin/env python3

# start
# 3. sort - sort lines in file | -

#
import sys
import argparse


def run(args):
    lists = args.filename.readlines()
    pre_sort_ed = []
    for line in lists:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        pre_sort_ed.append(line_list)
    sort_ed = sorted(pre_sort_ed)
    for i in sort_ed:
        sys.stdout.write('  '.join(i))
        sys.stdout.write('\n')


def main():
    parser = argparse.ArgumentParser(description="Displays sorted lines in file")
    parser.add_argument('filename', nargs='*', type=argparse.FileType('r'), default=sys.stdin)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
