class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for i in tokens:
            if i == "+":
                res = stack.pop(-2) + stack.pop(-1)
                stack.append(res)
            elif i == "-":
                res = stack.pop(-2) - stack.pop(-1)
                stack.append(res)
            elif i == "*":
                res = stack.pop(-2) * stack.pop(-1)
                stack.append(res)
            elif i == "/":
                res = stack.pop(-2) / stack.pop(-1)
                stack.append(int(res))
            else:
                stack.append(int(i))
            print(stack)
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN())
    #print(int(6 / -132))