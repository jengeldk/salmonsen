#!/usr/bin/python3
# encoding utf-8 
from sys import argv, stderr, stdin
from zipfile import ZipFile
import re
from collections import Counter
from unicodedata import name as uname 
from argparse import ArgumentParser

class kmers:
    def __init__(self, w=1, s=None):
        self.kmers = Counter()
        self.w = w
        if s:
            self.update(s)

    def update(self, s):
        if self.w == 1:
            self.kmers(s)
        else:
            for i in range(len(s)-self.w):
                 self.kmers[s[i:i+self.w]] += 1
    def most_common(self, n):
        return self.kmers.most_common(n)

    def 

"""
for (char, count) in CC.most_common():
    if w==1:
        print("<%c>: %s[%d]: %d" % (char, uname(char,"***UNKNOWN***"), ord(char), count))
    else:
        print("<%s>: %d" % (char, count))

"""
_forf = re.compile(r'([^<]+)?<i>([^<]+)</i>([^<]*)(<i>([^<]+)</i>)?([^<]+)?')

class Forfatter:
    def __init__(self, forf, typ, bind, side, linie, line=None):
        self.forf = forf
        if line:
            self.line = line
        else:
            self.line = forf
        self.typ = typ
        self.bind = bind
        self.side = side
        self.linie = linie
        
    def parse(self):
        if re.match('^†',self.forf):
            self.doed = 1
            self.forf = re.sub('^† *','', self.forf)
        elif re.search('\(†\)', self.forf):
            self.doed = 2
            self.forf = re.sub(' *\(†\) *', '', self.forf)
        elif '†' in self.forf:
            self.doed = 3
        else:
            self.doed = 0

def get_zip(bind, side, typ='txt', path="zip_files/", zip="salmonsen-{udgave}-{bind}-{typ}.zip", udgave=2):
    if typ == 'txt':
        fn = 'Pages/{side:04}.txt'
    if typ == 'tif':
        fn = 'salmonsen/{udgave}/{bind}/{side:04}.tif'
    zf = ZipFile(path+zip.format(bind=bind, udgave=udgave, typ=typ))
    return zf.open(fn.format(udgave=udgave, bind=bind, side=side), 'rU')

def get_file(bind, side, path, typ="txt", udgave=2):
    pre = path + 'salmonsen/{udgave}/{bind}/'
    if typ == 'txt':
        post = 'Pages/{side:04}.txt'
    if typ == 'tif':
        post = '{side:04}.tif'
    return open((pre+post).format(udgave=udgave, bind=bind, side=side))

class article:
    def __init__(self, s):
        pass


def readforf(filliste):
    """Læser forfatternavne fra sider i filliste"""
    typ=''
    gl_bind = 0 
    gl_side = 0
    ret = []
    for fn in filliste:
        m = re.search('/2/([1-9][0-9]?)/Pages/([0-9]{4})\.txt', fn)
        if not m:
            raise Exception("Filpath %s indeholder ikke bind og sidetal" % fn)
        bind, side = [int(e) for e in m.groups()]
        if (bind, side) <= (gl_bind, gl_side):
            raise Exception("Sider skal læses i orden: %d:%d kommer ikke efter %d:%d"
                    % (bind, side, gl_bind, gl_side))
        gl_side = side
        if bind != gl_bind:
            typ = ""
            gl_bind = bind
        line_no = 0
        for line in open(fn):
            line_no += 1
            if not '<i>' in line:
                print(line.strip())
                if 'signerede' in line.lower():
                    typ = 'SIGN'
                elif 'bidrag' in line.lower():
                    typ = 'BIDR'
                elif 'tidligere' in line.lower():
                    typ = 'TIDL'
                continue

            line = line.rstrip()
            orig = line
            if ' — ' in line:
                line = line.strip(' —')
                ff = line.split(' — ')
                for f in ff:
                    ret.append(Forfatter(f, typ, bind, side, line_no))
            else:
                ret.append(Forfatter(line, typ, bind, side, line_no))
    return ret

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-w', '--width', type=int, default=1)
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()
    files = args.files
    if not files:
        files.append('-')
    
    
