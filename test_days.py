# -*- coding: utf-8 -*-

import logging

from . import days

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


def test_day02():
    log.info("Test Day2")
    d = days.day02
    with open('input/day02.test') as f:
        assert d.solve(f) == (8, 2286)


def test_day03():
    log.info("Test Day3")
    d = days.day03
    with open('input/day03.test') as f:
        assert d.solve(f) == (4361, 467835)


def test_day04():
    log.info("Test Day4")
    d = days.day04
    with open('input/day04.test') as f:
        assert d.solve(f) == (13, 30)


def test_day05():
    log.info("Test Day5")
    d = days.day05
    with open('input/day05.test') as f:
        assert d.solve(f) == (35, 46)


def test_day06():
    log.info("Test Day6")
    d = days.day06
    with open('input/day06.test') as f:
        assert d.solve(f) == (288, 71503)


def test_day07():
    log.info("Test Day7")
    d = days.day07
    with open('input/day07.test') as f:
        assert d.solve(f) == (6440, 5905)


def test_day08():
    log.info("Test Day8")
    d = days.day08
    with open('input/day08.test1') as f:
        assert d.solve(f)[0] == 2
    with open('input/day08.test2') as f:
        assert d.solve(f)[0] == 6
    with open('input/day08.test3') as f:
        assert d.solve(f)[1] == 6
