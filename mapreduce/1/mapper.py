#!/usr/bin/env python

import sys
import csv

reader = csv.reader(sys.stdin)

next(reader)  # Skip header

for row in reader:
    try:
        job = row[1]
        balance = float(row[5])

        print(f"{job}\t{balance}\t1")

    except:
        continue