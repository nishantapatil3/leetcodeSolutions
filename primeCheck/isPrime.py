"""
/* The limit is the square root since 
 * x*y == y*x The function only has to go 1 loop to find that given number is weather or not divisible 5 and 
 * therefore not prime.
 * Because of the first few tests, and the tests in the middle of loop, the loop only needs to be evaluated every 6th number.
 */
"""

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True