import random


def roll():
    """サイコロを1回振って出目を返す"""
    return random.randint(1, 6)


def is_lucky(value):
    """1ならTrue、2〜6ならFalse"""
    return value == 1