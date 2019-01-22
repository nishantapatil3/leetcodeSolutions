import collections

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # print self.successors("0000")
        marked, depth = 'x', 0
        visited, q, deadends = set(), collections.deque(['0000', marked]), set(deadends)
        
        while q:
            node = q.popleft()
            # print node, "this"
            if node == target:    #target found return depth to acieve this
                return depth
            if node in visited or node in deadends:    #avoid visited and deadends
                continue
            if node == marked and not q:    #if none exists in q exits saying not possible to reach target
                return -1
            if node == marked:  #add in visited
                q.append(marked)
                depth += 1    #increase depth by one
            else:    #get surrounding values of current node and add to q
                visited.add(node)    #mark visited
                q.extend(self.successors(node))
        return -1
        
    def successors(self, src):
        res = []
        for i, ch in enumerate(src):
            num = int(ch)
            res.append(src[:i] + str((num-1)%10) + src[i+1:])
            res.append(src[:i] + str((num+1)%10) + src[i+1:])
        return res
