if __name__ == '__main__':
    inputs = list()
    stack = list()
    results = list()
    depth = list()
    for _ in range(1):
        temp = input()
        inputs.append(temp)
    for brackets in inputs:
        temp = ""
        _depth = 0
        previous_depth = 0
        for i in range(len(brackets)):

            if brackets[i] == "(":

                if _depth != 0:
                    print("Check 1")
                    depth.append(_depth)
                    _depth = 0
                    results.append(temp)
                    temp = ""
                stack.append("(")
                temp += "("
                print("temp is ", temp)
            else:
                if len(stack) > 0:
                    print("Check 2")
                    temp += ")"
                    print("temp is ", temp)
                    _depth += 1
                    stack.pop(-1)
                if i == len(brackets) - 1:
                    depth.append(_depth)
                    results.append(temp)

        # results.append(temp)
        # depth.append(_depth)

        print(depth, results)