#!/usr/bin/env python

check = 1

def checkdiv(num):
    for i in range(1, 20):
        if num%i!=0:
            return False
    return num

while (True):
    if checkdiv(check):
        print check
        break
    check = check + 1
