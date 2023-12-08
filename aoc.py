#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import days

day = sys.argv[1]
print("### Run Advent Of Code - Day {} ###\n".format(day))

day = getattr(days, "day{}".format(day))
res = day.solve(sys.stdin)
print("Solutions: [{}] [{}]".format(*res))
