class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list(S)
        res = s[0]
        i = 1
        while len(s) > 0:
            print("len", len(s))
            if s[i] != res[-1]:
                res += s[i]
                s.pop(i)
                i = 0
            else:
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("aab"))