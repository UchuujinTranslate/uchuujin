#!/usr/bin/env python3

# Reads alphanum.tbl and returns it as a dict
def alphanumTable():
    table = {}
    lines = open("alphanum.tbl", 'r', encoding="shift-jis").readlines()

    # Numbers
    numcounter = 0x0092  # 146
    for x in range(0, 10):
        line = lines[x]
        num = int(line[0:4], 16)
        table[numcounter] = num
        numcounter += 1

    # Capital letters
    capcounter = 0x009c  # 156
    for x in range(9, 35):
        line = lines[x]
        cap = int(line[0:4], 16)
        table[capcounter] = cap
        capcounter += 1

    # Lowercase letters
    lowcounter = 0x00b6  # 182
    for x in range(35, 61):
        line = lines[x]
        low = int(line[0:4], 16)
        table[lowcounter] = low
        lowcounter += 1

    return table
