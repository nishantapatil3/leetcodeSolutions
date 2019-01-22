class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Binary Search method
        ## Handle basic sqrt(0) and sqrt(1) (save some time)
        if x == 0 or x == 1:
            return x

        ## Since we already processed 0 and 1 start with 1
        start = 1
        end = x
        while (start <= end):
            mid = (start+end)//2
            
            n = mid*mid
            if n == x:
                return mid
            elif n < x:
                start = mid+1
            else:
                end = mid-1
        return end
