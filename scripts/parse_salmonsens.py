from sys import argv
from collections import Counter
from unicodedata import name as uname 
from zipfile import ZipFile

def nl(s, nls=('\n', '\r', '\r\n')):
    NL = '\n'
    for cc in nls:
        if cc in s:
            NL = cc
    return NL

numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = i // integer
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result

def readziplines(zipfile, fn, encoding=None):
    if encoding:
         s = str(zipfile.read(fn), encoding)
    else:
         s = str(zipfile.read(fn))
    NL = nl(s)
    if s.endswith(NL):
        return s.split(NL)[:-1]
    else:
        return s.split(NL)

fn = argv[1]
zf = ZipFile(fn)

ml = readziplines(zf, 'Metadata', 'latin-1')

metadict = dict(e.split(': ',1) for e in ml if ': ' in e)
encoding = metadict['CHARSET']
volume, title = metadict['TITLE'].split(':', 1)
title = title.strip()
year = metadict['PUBLISHING_YEAR']
volume = volume.split(None, 1)[-1] 
volume = volume.strip()

print("file: %s, title: %s, volume: %s[%d], year: %s, encoding: %s" % (fn, title, volume, roman_to_int(volume), year, encoding))
pl = readziplines(zf, 'Pages.lst', encoding)
pldict = dict(l.split('|') for l in pl if '|' in l)
okl = readziplines(zf, 'Pages.lst', encoding)
okcount = Counter(okl)
