#!/usr/bin/env python3
import maude
import sys

def init_arg(sasso):
    return f"{sasso} =|= e # 0"

def test_conversion(sasso):
    pa = maude.getModule("RULES")
    width = 17
    print(f"\n{'To convert:':<{width}} {sasso}")
    toMaude = pa.parseTerm(sasso)
    toMaude.reduce()
    print(f"{'Reduce:':<{width}} {toMaude}")
    toMaude = pa.parseTerm(sasso)
    toMaude.rewrite()
    print(f"{'Rewrite:':<{width}} {toMaude}")
    toMaude = pa.parseTerm(f"getTangle({str(toMaude)})")
    toMaude.reduce()
    print(f"{'Rewrite - reduce:':<{width}} {toMaude}")

def convert(sasso):
    pa = maude.getModule("RULES")
    toMaude = pa.parseTerm(sasso)
    toMaude.rewrite()
    toMaude = pa.parseTerm(f"getTangle({str(toMaude)})")
    toMaude.reduce()
    return str(toMaude)

if __name__ == '__main__':
    maude.init()
    maude.load('patt.maude')


    if len(sys.argv) <= 1:
        print("Not enough args")
        exit(1)
    
    out: str = convert(init_arg(sys.argv[1]))
    arr = [s.strip() for s in out.split('~')]
    # arr = [(i,i2) for i, v in enumerate(arr)]
    outlist = []
    for i,v in enumerate(arr):
        for k,z in enumerate(arr):
            if v == z and i<k:
                outlist.append((i,k))
                
    print(','.join([f"{i}:{k}" for i,k in outlist]))