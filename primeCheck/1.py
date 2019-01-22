def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, n):
            if primes[i] == True:
                for j in range(2, (n-1)//i+1):
                    primes[i*j] = False
        return sum(primes)
