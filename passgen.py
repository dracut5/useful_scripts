#!/usr/bin/env python3


from sys import argv
import random
import string

passLength = int(argv[1])
L1 = [s for s in string.ascii_lowercase]
L2 = [s for s in string.ascii_uppercase]
L3 = [str(i) for i in range(10)]
randomList = L1 + L2 + L3 * 4
random.shuffle(randomList)

resultList = []
for i in range(passLength):
    k = random.choice(randomList)
    resultList.append(k)

print("".join(resultList))
