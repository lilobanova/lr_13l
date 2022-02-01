#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        result = 1
        for value in values:
            result *= value
        return result ** (1 / n)
    else:
        return None


if __name__ == "__main__":
    print(geometric_mean())
    print(geometric_mean(3, 7, 1, 6, 9))
    print(geometric_mean(1, 5, 8, 4, 3, 9))
