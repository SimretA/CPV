def add():
    num1 = input("enter first num>> ")
    num2 = input("enter second num>> ")
    result = ""

    maximum = len(num1) if len(num1) > len(num2) else len(num2)
    for i in range(0, maximum):
        temp = int(num1[i]) + int(num2[i])
        result += str(temp)
    print(result)


def add(a, b):
    carry = 0
    result = ""
    maximum = len(a) if len(a) > len(b) else len(b)
    a = (maximum-len(a))*"0" + a
    b = (maximum-len(b))*"0" + b
    print("Adding ", a, " ", b)

    for i in range(maximum-1, -1, -1):
        temp = int(a[i]) + int(b[i]) + carry
        carry = temp//10
        temp = temp % 10
        result = str(temp) + result
    print("added ", result)
    return result


if __name__ == '__main__':
    add("013", "123")
