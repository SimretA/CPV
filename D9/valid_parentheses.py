class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = list()
        for i in s:
            if i == ")":
                if len(par) == 0:
                    return False
                elif par[-1] == "(":
                    par.pop(len(par) - 1)
                else:
                    return False
            elif i == "]":
                if len(par) == 0:
                    return False
                elif par[-1] == "[":
                    par.pop(len(par) - 1)
                else:
                    return False
            elif i == "}":
                if len(par) == 0:
                    return False
                elif par[-1] == "{":
                    par.pop(len(par) - 1)
                else:
                    return False
            else:
                par.append(i)
        if len(par) == 0:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("]"))
