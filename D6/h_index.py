class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        print(reversed(citations))

if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
