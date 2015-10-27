#!/usr/bin/python3
from sys import argv
from regex import compile
text = [open(fn).read()for fn in argv[2:]]
rr = compile(argv[1])
for t in text:
    for m in rr.findall(t):
        print(m)


