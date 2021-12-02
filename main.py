#!/usr/bin/env python3
import maude

if __name__ == '__main__':
    maude.init()

    maude.load('patt.maude')

    pa = maude.getModule("RULES")
    first_to_parse = 'A 1 . A 2 . A 3 . ( A 5 . A 6 || A 4 ) . A 8 . nil =|= e'
    anotherPa = pa.parseTerm(first_to_parse)
    length_to_parse = 'length(A 1 . A 2 . A 5 || A 4 . nil)'
    length = pa.parseTerm(length_to_parse)
    ln_to_parse = 'A 1 . A 2 . nil =|= e'
    ln = pa.parseTerm(ln_to_parse)
    anotherPa.rewrite()
    length.reduce()
    ln.rewrite()
    print(length_to_parse, '\n', length)
    print(first_to_parse , '\n', anotherPa)
    print(ln_to_parse, '\n', ln)
