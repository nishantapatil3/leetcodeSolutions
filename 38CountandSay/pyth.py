class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        
        for i in range(0,n-1):
            ans = self.countString(ans)
        return ans
    
    def countString(self, n):
        count, i , res = 1, 0, ""
        while i < len(n)-1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]
        return res
