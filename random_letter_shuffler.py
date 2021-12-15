# start

from random import shuffle
import string
import sys
import argparse


def run(args):
    punctuation = tuple(string.punctuation)
    file = args.filename
    for line in file.readlines():
        res = []
        for i in line.split():
            punch = False
            if len(i) >= 4:
                if i.endswith(punctuation):
                    val = list(i[1:-2])
                    punch = True
                else:
                    val = list(i[1:-1])
                shuffle(val)
                if punch:
                    res.append("{0}{1}{2}".format(i[0], "".join(val), i[-2:]))
                else:
                    res.append("{0}{1}{2}".format(i[0], "".join(val), i[-1]))
            else:
                res.append(i)
        sys.stdout.write(' '.join(res))


def main():
    parser = argparse.ArgumentParser(description="this script shuffles all letters in your text, except first and last")
    parser.add_argument('filename', help="input text file.txt", nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
