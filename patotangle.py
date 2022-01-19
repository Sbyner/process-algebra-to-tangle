#!/usr/bin/env python3
import maude
import sys
import re


def _init_arg(sasso):
    return f"{sasso} =|= e # 0"

def _convert(sasso):
    pa = maude.getModule("RULES")
    toMaude = pa.parseTerm(sasso)
    toMaude.rewrite()
    toMaude = pa.parseTerm(f"getTangle({str(toMaude)})")
    toMaude.reduce()
    return str(toMaude)

def to_tangle(input):
    maude.init()
    maude.load('patt.maude')
    
    out: str = _convert(_init_arg(input))
    arr = [s.strip() for s in out.split('~')]
    # arr = [(i,i2) for i, v in enumerate(arr)]
    outlist = []
    for i,v in enumerate(arr):
        for k,z in enumerate(arr):
            if v == z and i<k:
                outlist.append((i+1,k+1))
    res = ','.join([f"{i}:{k}" for i,k in outlist])
    return res

def _main():
    if len(sys.argv) <= 1:
        print("Not enough args")
        exit(1)
    print(to_tangle(sys.argv[1]))

if __name__ == '__main__':
    _main()
