from adder import add


def multiply():
    carry = 0
    num1 = input("enter first num>> ")
    num2 = input("enter second num>> ")
    num1len = len(num1)
    num2len = len(num2)
    to_add = []

    for i in range(num1len - 1, -1, -1):
        temp = ""
        for j in range(num2len - 1, -1, -1):

            multiplied = int(num1[i]) * int(num2[j]) + carry
            carry = multiplied // 10
            multiplied = multiplied % 10
            temp = str(multiplied) + temp

        temp += (num1len - 1 - i) * "0"
        to_add.append(temp)

    print(to_add)
    result = to_add[0]
    for result_i in range(1, len(to_add)):
        result = add(to_add[result_i], result)
    print("Result ", result)


if __name__ == '__main__':
    multiply()
