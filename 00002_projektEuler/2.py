#!/usr/bin/env python
# coding: utf-8

def fibb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)


if __name__ == "__main__":
    total = 0
    for i in range(40):
        current = fibb(i)
        if (current%2 == 0) and (current < 4000000):
            total = total + current
    print total
