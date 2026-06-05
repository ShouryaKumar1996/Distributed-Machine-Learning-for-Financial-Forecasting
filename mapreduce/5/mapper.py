#!/usr/bin/env python
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header
for row in reader:
    try:
        age = int(row[0])
        balance = float(row[5])
        # Group age into brackets
        if age < 30:
            age_group = "18-29"
        elif age < 40:
            age_group = "30-39"
        elif age < 50:
            age_group = "40-49"
        elif age < 60:
            age_group = "50-59"
        else:
            age_group = "60+"
        print(f"{age_group}\t{balance}\t1")
    except:
        continue