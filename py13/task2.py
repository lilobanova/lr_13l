#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        result = 0
        for value in values:
            result += (1 / value)
        return n / result
    else:
        return None


if __name__ == "__main__":
    print(harmonic_mean())
    print(harmonic_mean(3, 7, 1, 6, 9))
    print(harmonic_mean(1, 5, 8, 4, 3, 9))
