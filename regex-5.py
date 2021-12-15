# start

import re
# import matplotlib.pyplot as plt

data = {}

with open("tale.txt") as input_file:
    for line in input_file:
        matches = re.findall('[a-zA-z\']+', line)
        