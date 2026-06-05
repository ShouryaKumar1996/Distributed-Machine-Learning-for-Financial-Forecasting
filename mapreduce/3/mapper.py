#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header
for row in reader:
    try:
        month = row[10]    # month column
        subscribed = row[16]  # y column (yes/no)
        print(f"{month}\t{subscribed}")
    except:
        continue