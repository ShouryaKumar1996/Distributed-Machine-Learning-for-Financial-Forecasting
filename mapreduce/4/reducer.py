#!/usr/bin/env python
import sys

current_key = None
total_duration = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    poutcome, duration, cnt = line.split("\t")
    duration = float(duration)
    cnt = int(cnt)
    if current_key == poutcome:
        total_duration += duration
        count += cnt
    else:
        if current_key:
            print(f"{current_key}\tavg_duration:{total_duration/count:.2f} seconds\tcount:{count}")
        current_key = poutcome
        total_duration = duration
        count = cnt

if current_key:
    print(f"{current_key}\tavg_duration:{total_duration/count:.2f} seconds\tcount:{count}")