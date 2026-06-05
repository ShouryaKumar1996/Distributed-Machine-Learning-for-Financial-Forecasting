#!/usr/bin/env python
import sys
from collections import defaultdict

counts = defaultdict(lambda: {"yes": 0, "no": 0})

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    education, housing = line.split("\t")
    counts[education][housing] += 1

for education, data in sorted(counts.items()):
    print(f"{education}\thousing_yes:{data['yes']}\thousing_no:{data['no']}")