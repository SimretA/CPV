class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n == 3:
            return 2
        return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)