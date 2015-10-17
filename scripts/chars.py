#!/usr/bin/python3
from sys import argv,stdin
from collections import Counter
from unicodedata import name as uname 
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-w', '--width', type=int, default=1)
parser.add_argument('files', nargs='*')
args = parser.parse_args()
files = args.files
if not files:
    files.append('-')
w=args.width
CC = Counter() 
for fn in files:
    if fn=='-':
        f = stdin
    else:
        f = open(fn)
    for line in f:
        if w==1:
             CC.update(line)
        else:
             for i in range(len(line)-w):
                 CC[line[i:i+w]] += 1

for (char, count) in CC.most_common():
    if w==1:
        print("<%c>: %s[%d]: %d" % (char, uname(char,"***UNKNOWN***"), ord(char), count))
    else:
        print("<%s>: %d" % (char, count))


