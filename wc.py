#!/usr/bin/env python3

# start
# Objectives: ++++ path
# 1. wc - word count | -l lines -w words -c bytes

# Additional:
# 1. grep "pattern" file_to_look_in_for.txt | -

#
# import os
# import sys
# import argparse
#
#
# def run(args):
#     def count_lines():
#         if line_s:
#             lines = 0
#             for line in args.filename:
#                 lines += 1
#             sys.stdout.write(str(lines))
#
#     def count_words():
#         if word_s:
#             word = 0
#             for line in args.filename:
#                 word += len(line.split(" "))
#             sys.stdout.write(str(word))
#
#     def count_bytes():
#         if byte_s:
#             sys.stdout.write(str(sys.getsizeof(args.filename)))
#     count_lines()
#     count_words()
#     count_bytes()
#
#
# def main():
#     parser = argparse.ArgumentParser(description="Counting words lines and bytes of file")
#     parser.add_argument('filename', help="input text file", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
#     parser.add_argument('-l', help="Showing lines", dest="line_s", action='store_true')
#     parser.add_argument('-w', help="Showing words", dest="word_s", action='store_true')
#     parser.add_argument('-c', help="Showing bytes", dest="byte_s", action='store_true')
#     parser.set_defaults(func=run)
#     args = parser.parse_args()
#     args.func(args)
#
#
# if __name__ == "__main__":
#     main()
