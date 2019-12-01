from D9.Stack import Stack


def calc(param):
    temp = param.split(" ")
    stack = Stack()
    for i in range(len(temp) - 1, -1, -1):
        ii = temp[i]
        if ii == "+":
            res = stack.pop() + stack.pop()
            stack.push(res)
        elif ii == "-":
            res = stack.pop() - stack.pop()
            stack.push(res)
        elif ii == "*":
            res = stack.pop() * stack.pop()
            stack.push(res)
        elif ii == "/":
            res = stack.pop() / stack.pop()
            stack.push(res)
        else:
            stack.push(int(ii))
    return stack.pop()


if __name__ == '__main__':
    print(calc("+ 4 * 3 12"))
