import os
import re

start_dir = r'target'
sample = r'\d+'

for fldr in os.listdir(start_dir):
    match = re.findall(sample, fldr)
    if int(match[0]) % 2 == 0:
        os.rename(start_dir + '/' + match[0], start_dir + '/lol' + str(int(match[0])*11))