class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t1, t2, t3 = 0, 1, 1
        if n == 0:
            return 0
        for i in range(3, n+1):
                t1, t2, t3 = t2, t3, t1+ t2 + t3
        return t3