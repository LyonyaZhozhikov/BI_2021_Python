# start

import re

matches = []

with open("references.txt") as input_file:
    for line in input_file:
        match = re.findall('(ftp(\.[a-zA-Z]{2,3}){4}(\/[a-zA-Z0-9_#]+)+(\.[a-z0-9]+)+)', line)
        matches.append(match)

with open("ftps.txt", "w") as output_file:
    for lines in matches:
        for match in lines:
            output_file.write(match[0] + "\n")
            # output_file.write("\n")
