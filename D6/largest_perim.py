class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        perim = 0
        for i in range(len(A)-2):
            tri_confirm = A[i] + A[i+1]
            if tri_confirm > A[i + 2]:
                temp = tri_confirm + A[i+2]
                if temp > perim:
                    perim = temp
        return perim


if __name__ == '__main__':
    s = Solution()
    print(s.largestPerimeter([1,2,1]))

