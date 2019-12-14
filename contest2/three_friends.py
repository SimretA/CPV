if __name__ == '__main__':
    t = eval(input())
    inputs = list()
    ac, ab, bc = 0, 0, 0
    for _ in range(t):
        temp = input()
        inputs.append(temp.split(" "))
    for val in inputs:
        val = sorted(val)
        for i in range(3):
            val[i] = eval(val[i])
        ac = abs(val[0] - val[2])
        ab = abs(val[0] - val[1])
        bc = abs(val[1] - val[2])
        if ac == 0 or ac == 1:
            print(0)
        elif ac == ab or ac == bc:
            print(ac + ab + bc - 4)
        elif ac > 1:
            ac -= 2
            if ab >= 1:
                ab -= 1
            if bc >= 1:
                bc -= 1
            print(ac + ab + bc)


