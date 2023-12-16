# -*- coding: utf-8 -*-

import logging

import days

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('tests')


def test_day01():
    log.info("Test Day1")
    d = days.day01
    with open('input/day01.test1') as f:
        assert d.solve(f)[0] == 142
    with open('input/day01.test2') as f:
        assert d.solve(f)[1] == 281
    with open('input/day01.test3') as f:
        # The right calibration values for string
        # "eighthree" is 83 and for "sevenine" is 79.
        assert d.solve(f)[1] == 162
    with open('input/day01') as f:
        assert d.solve(f) == (54953, 53868)


def test_day02():
    log.info("Test Day2")
    d = days.day02
    with open('input/day02.test') as f:
        assert d.solve(f) == (8, 2286)
    with open('input/day02') as f:
        assert d.solve(f) == (2207, 62241)


def test_day03():
    log.info("Test Day3")
    d = days.day03
    with open('input/day03.test') as f:
        assert d.solve(f) == (4361, 467835)
    with open('input/day03') as f:
        assert d.solve(f) == (520019, 75519888)


def test_day04():
    log.info("Test Day4")
    d = days.day04
    with open('input/day04.test') as f:
        assert d.solve(f) == (13, 30)
    with open('input/day04') as f:
        assert d.solve(f) == (26346, 8467762)


def test_day05():
    log.info("Test Day5")
    d = days.day05
    with open('input/day05.test') as f:
        assert d.solve(f) == (35, 46)
    with open('input/day05') as f:
        assert d.solve(f) == (322500873, 108956227)


def test_day06():
    log.info("Test Day6")
    d = days.day06
    with open('input/day06.test') as f:
        assert d.solve(f) == (288, 71503)
    with open('input/day06') as f:
        assert d.solve(f) == (219849, 29432455)


def test_day07():
    log.info("Test Day7")
    d = days.day07
    with open('input/day07.test') as f:
        assert d.solve(f) == (6440, 5905)
    with open('input/day07') as f:
        assert d.solve(f) == (248217452, 245576185)


def test_day08():
    log.info("Test Day8")
    d = days.day08
    with open('input/day08.test1') as f:
        assert d.solve(f)[0] == 2
    with open('input/day08.test2') as f:
        assert d.solve(f)[0] == 6
    with open('input/day08.test3') as f:
        assert d.solve(f)[1] == 6
    with open('input/day08') as f:
        assert d.solve(f) == (20513, 15995167053923)


def test_day09():
    log.info("Test Day9")
    d = days.day09
    with open('input/day09.test') as f:
        assert d.solve(f) == (114, 2)
    with open('input/day09') as f:
        assert d.solve(f) == (1647269739, 864)


def test_day10():
    log.info("Test Day10")
    d = days.day10
    with open('input/day10.test1') as f:
        assert d.solve(f)[0] == 4
    with open('input/day10.test2') as f:
        assert d.solve(f)[0] == 4
    with open('input/day10.test3') as f:
        assert d.solve(f)[1] == 4
    with open('input/day10.test4') as f:
        assert d.solve(f)[1] == 8
    with open('input/day10.test5') as f:
        assert d.solve(f)[1] == 10
    with open('input/day10') as f:
        assert d.solve(f) == (6754, 567)


def test_day11():
    log.info("Test Day11")
    d = days.day11
    with open('input/day11.test') as f:
        assert d.solve(f, 10) == (374, 1030)
        f.seek(0)
        assert d.solve(f, 100) == (374, 8410)
    with open('input/day11') as f:
        assert d.solve(f) == (10228230, 447073334102)


def test_day12():
    log.info("Test Day12")
    d = days.day12
    with open('input/day12.test') as f:
        assert d.solve(f) == (21, 525152)
    with open('input/day12') as f:
        assert d.solve(f) == (8419, 160500973317706)


def test_day13():
    log.info("Test Day13")
    d = days.day13
    with open('input/day13.test') as f:
        assert d.solve(f) == (405, 400)
    with open('input/day13') as f:
        assert d.solve(f) == (31739, 31539)


def test_day14():
    log.info("Test Day14")
    d = days.day14
    with open('input/day14.test') as f:
        assert d.solve(f) == (136, 64)
    with open('input/day14') as f:
        assert d.solve(f) == (107951, 95736)


def test_day15():
    log.info("Test Day15")
    d = days.day15
    assert d.h('HASH') == 52
    with open('input/day15.test') as f:
        assert d.solve(f)[1] == 145
    with open('input/day15') as f:
        assert d.solve(f) == (511257, 239484)


def test_day16():
    log.info("Test Day16")
    d = days.day16
    with open('input/day16.test') as f:
        assert d.solve(f) == (46, 51)
    with open('input/day16') as f:
        assert d.solve(f) == (8323, 8491)
