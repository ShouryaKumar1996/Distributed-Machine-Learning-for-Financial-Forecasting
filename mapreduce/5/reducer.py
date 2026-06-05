#!/usr/bin/env python
import sys

current_key = None
total_balance = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    age_group, balance, cnt = line.split("\t")
    balance = float(balance)
    cnt = int(cnt)
    if current_key == age_group:
        total_balance += balance
        count += cnt
    else:
        if current_key:
            print(f"{current_key}\tavg_balance:{total_balance/count:.2f}\tclient_count:{count}")
        current_key = age_group
        total_balance = balance
        count = cnt

if current_key:
    print(f"{current_key}\tavg_balance:{total_balance/count:.2f}\tclient_count:{count}")