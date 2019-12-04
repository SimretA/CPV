class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c_temp = sorted(citations, reverse=True)

        length = len(citations)
        print(c_temp)
        for i in range(length):
            if c_temp[i] <= i:
                return i

        return length


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
