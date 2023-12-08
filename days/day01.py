#!/usr/bin/env python3

import re


def solve(din):
    lines = din.readlines()
    numbers = [
        'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine']

    def parse_n(v):
        return v in numbers and str(numbers.index(v) + 1) or v

    def to_int(ds):
        return ds and int(f'{parse_n(ds[0])}{parse_n(ds[-1])}') or 0

    def calibration(r):
        yield from [to_int(r.findall(l)) for l in lines]

    return (
        sum(calibration(re.compile(r'\d'))),
        sum(calibration(re.compile(rf'(?=(\d|{r"|".join(numbers)}))'))))
