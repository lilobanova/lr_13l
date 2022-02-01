#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def positive_sum(*args):
    if args:
        i_max = 0
        el_max = 0
        for index, arg in enumerate(args):
            if arg >= el_max:
                i_max = index
                el_max = arg
        pos_s = sum(arg for index, arg in enumerate(args) if index > i_max)
        return pos_s
    else:
        return None

if __name__ == "__main__":
    arguments = [int(i) for i in input("Введите аргументы: ").split()]
    print("Сумма аргументв, расположенных после максимального = "
          f"{positive_sum(*arguments)}"
          )
