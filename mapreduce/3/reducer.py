#!/usr/bin/env python
import sys
from collections import defaultdict

counts = defaultdict(lambda: {"yes": 0, "no": 0})

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    month, subscribed = line.split("\t")
    counts[month][subscribed] += 1

for month, data in sorted(counts.items()):
    total = data["yes"] + data["no"]
    print(f"{month}\ttotal:{total}\tsubscribed_yes:{data['yes']}\tsubscribed_no:{data['no']}")