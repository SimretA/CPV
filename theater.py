if __name__ == '__main__':
    inputs = input()
    m, n, a = inputs.split(" ")
    rows, cols = 0, 0

    m = int(m)
    n = int(n)
    a = int(a)

    diff = abs(m - n)

    maximum = max(m, n)

    aa = (maximum - diff)
    while aa > 0:
        rows += 1
        aa -= a

    while diff > 0:
        cols += 1
        diff -= a
    print(rows * rows + cols * rows)
