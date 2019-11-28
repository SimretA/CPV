from sub import sub


def div(num1, num2):
    counter = 0
    mix = ""
    while len(num1) > len(num2):
        counter += 1
        num1 = sub(num1, num2)
    if int(num1) > 0:
        mix = num1 + "/" + num2

    return str(counter) + " and " + mix


if __name__ == '__main__':
    print(div("18", "8"))
