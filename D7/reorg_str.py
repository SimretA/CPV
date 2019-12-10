class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dictionary ={}
        for i in S:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        print(dictionary)


if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("aab"))