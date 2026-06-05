#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header
for row in reader:
    try:
        education = row[3]    # education column
        housing = row[6]      # housing loan column (yes/no)
        print(f"{education}\t{housing}")
    except:
        continue