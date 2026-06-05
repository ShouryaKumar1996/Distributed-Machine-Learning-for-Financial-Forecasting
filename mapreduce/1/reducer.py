#!/usr/bin/env python

import sys

current_job = None
total_balance = 0
count = 0

for line in sys.stdin:
    job, balance, cnt = line.strip().split("\t")

    balance = float(balance)
    cnt = int(cnt)

    if current_job == job:
        total_balance += balance
        count += cnt

    else:
        if current_job:
            print(f"{current_job}\t{total_balance/count:.2f}")

        current_job = job
        total_balance = balance
        count = cnt

if current_job:
    print(f"{current_job}\t{total_balance/count:.2f}")