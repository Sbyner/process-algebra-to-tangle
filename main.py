#!/usr/bin/env python3
import maude

maude.init()

maude.load('patt.maude')


pa = maude.getModule("RULES")

boh = pa.parseTerm('A 1 . A 2 . nil')

ln = pa.parseTerm('length(A 1 . A 2 . nil)')
ln.reduce()
print(boh, ln)
