def watermelon(num):

    if num == 2:
        return "NO"
    if num % 2 == 0:
        return "YES"
    return "NO"


if __name__ == '__main__':
    weight = eval(input())
    print(watermelon(weight))