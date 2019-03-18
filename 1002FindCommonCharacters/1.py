class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        answer = None
        
        for word in A:
            work = {}
            for lett in word:
                if lett in work:
                    work[lett] += 1
                else:
                    work[lett] = 1
            
            if answer != None:
                keys = list(answer.keys())
                for k in keys:
                    if k in work:
                        answer[k] = min(answer[k], work[k])
                    else:
                        del answer[k]
            else:
                answer = work
        
        answerArr = []
        for key in answer:
            count = answer[key]
            for _ in xrange(count):
                answerArr.append(key)
        
        return answerArr
