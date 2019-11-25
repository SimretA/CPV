from adder import add


def sub(param, param1):
    result = add(param, compliment(param1))
    if len(result) > 1:
        return result[1:]
    return result


def compliment(param):
    result = ""
    for i in range(len(param)):
        result += str(9 - int(param[i]) + 1)

    return result


if __name__ == '__main__':
    sub("18", "6")
