# start

import re

matches = []

with open("tale.txt") as input_file:
    for line in input_file:
        match = re.findall('[0-9]+[0-9]', line)
        matches.append(match)

with open("tale_only_digits.txt", "w") as output_file:
    for lines in matches:
        for match in lines:
            output_file.write(match + "\n")
