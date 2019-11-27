def add(a, b):
    neg = ""
    if a[0] == "-" and b[0] != "-":
        return sub(b, a[1:])
    if b[0] == "-" and a[0] != "-":
        return sub(a, b[1:])
    if a[0] == "-" and b[0] == "-":
        a = a[1:]
        b = b[1:]
        neg = "-"
    carry = 0
    result = ""
    maximum = len(a) if len(a) > len(b) else len(b)
    a = (maximum - len(a)) * "0" + a
    b = (maximum - len(b)) * "0" + b
    print("Adding ", a, " ", b)

    for i in range(maximum - 1, -1, -1):
        temp = int(a[i]) + int(b[i]) + carry
        carry = temp // 10
        temp = temp % 10
        result = str(temp) + result
    print("added ", result)
    return neg + result


def sub(param, param1):
    result = add(param, compliment(param1))
    res_len = max(len(param), len(param1))
    if len(result) > res_len:
        return result[1:]
    return result


def compliment(param):
    result = ""
    for i in range(len(param)):
        result += str(9 - int(param[i]))

    return add(result, "1")


if __name__ == '__main__':
    print("sub result", sub("118", "6"))
