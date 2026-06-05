#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header
for row in reader:
    try:
        poutcome = row[15]   # poutcome column
        duration = float(row[11])  # duration column
        print(f"{poutcome}\t{duration}\t1")
    except:
        continue