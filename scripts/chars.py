from sys import argv
from collections import Counter
from unicodedata import name as uname 
w=1
CC = Counter() 
for fn in argv[1:]:
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


