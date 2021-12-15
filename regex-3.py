# start

import re

matches = []

with open("tale.txt") as input_file:
    for line in input_file:
        match = re.findall('[a-zA-z]*[Aa][a-zA-z]*[^, -?!]', line)
        matches.append(match)

with open("tale_a_letter.txt", "w") as output_file:
    for lines in matches:
        for match in lines:
            output_file.write(match + "\n")
