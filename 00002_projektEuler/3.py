#!/usr/bin/env python
# coding: utf-8

import sys

def get_largest_factor(num):
    i = 2
    while i*i < num:
        while (num%i == 0):
            num = num/i
        i = i + 1
    print num

def get_factors(num):
    i = 2
    while i*i < num:
        if num%i == 0:
            if isprime(i):
                print i
        i = i + 1

def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

if __name__ == "__main__":
    num = int(sys.argv[1])
    print "largest factor = ", get_largest_factor(num)
    print "prime factors => ", get_factors(num)
