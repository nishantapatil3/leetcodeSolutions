class Solution(object):
    def tonum(self, ip):
        numbers = list(map(int, ip.split(".")))
        n = (numbers[0]<<24) + (numbers[1]<<16) + (numbers[2]<<8) + numbers[3]
        return n

    def toip(self, num):
        return ".".join([str(num>>24&255), str(num>>16&255), str(num>>8&255), str(num&255)])
    
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        startnum = tonum(ip)
        endnum = startnum + n - 1
        currentnum = startnum
        ans = []
        while currentnum <= endnum:
            MaxFreePositions = 0
            while currentnum % (1 << (MaxFreePositions+1)) == 0:
                MaxFreePositions += 1
            FreePositions = MaxFreePositions

            while (currentnum | ((1 << FreePositions) - 1)) > endnum:
                FreePositions -=1

            ans.append(self.toip(currentnum) + "/" + str(32-FreePositions))
            currentnum = (currentnum | ((1 << FreePositions) - 1)) + 1
        return ans

test = Solution()
print test.iptoCIDR("255.0.0.7", 10)
