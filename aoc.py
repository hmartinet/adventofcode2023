#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

import days

if len(sys.argv) > 1:
    d = sys.argv[1]
    print(f"### Run Advent Of Code 2023 - Day {d} ###\n")

    res = getattr(days, f"day{d}").solve(sys.stdin)
    print("Solutions: [{}] [{}]".format(*res))
else:
    print("### Run Advent Of Code 2023 ###\n")
    tt = 0
    for d in days.__all__:
        with open(f'input/{d}') as f:
            st = time.process_time()
            r = getattr(days, d).solve(f)
            dt = time.process_time() - st
            res = "Day {}: [{}] [{}]".format(d[-2:], *r)
            tt += dt
        print(f"{res: <40} {dt:.3f}s")
    print(f"{'Total execution time': <40} {tt:.3f}s")
