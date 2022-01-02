#!/usr/bin/env python3
import sys, time


print("printowanie bledow", file=sys.stderr)

longstring = []
for x in range(17):
    print(len(longstring))	
    time.sleep(1)
    longstring.append('1' * 10**6)
