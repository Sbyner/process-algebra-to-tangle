#!/usr/bin/env python3
import maude

if __name__ == '__main__':
    maude.init()

    maude.load('patt.maude')

    pa = maude.getModule("RULES")
    first_to_parse = 'A 1 . ( A 3 || A 4 || A 5 ) . A 8 . nil =|= e # 0'
    anotherPa = pa.parseTerm(first_to_parse)
    length_to_parse = 'length(nil)'
    length = pa.parseTerm(length_to_parse)
    ln_to_parse = 'A 1 . A 2 . nil =|= e # 0'
    ln = pa.parseTerm(ln_to_parse)
    anotherPa.rewrite()
    length.reduce()
    ln.rewrite()
    print(length_to_parse, '\n', length, '\n')
    print(first_to_parse , '\n', anotherPa, '\n')
    print(ln_to_parse, '\n', ln, '\n')
