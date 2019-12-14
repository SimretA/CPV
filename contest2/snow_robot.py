if __name__ == '__main__':
    # print("saddess".replace("s", "", 1))
    t = eval(input())
    inputs = list()
    for _ in range(t):
        temp = input()
        inputs.append(temp)
    for walks in inputs:
        length = len(walks)
        walked = [0] * 4  # left, right, up, down
        prev = ""
        for x in range(len(walks)):
            drxn = walks[x]
            if drxn == "L":
                walked[0] += 1
            elif drxn == "R":
                walked[1] += 1
            elif drxn == "U":
                walked[2] += 1
            elif drxn == "D":
                walked[3] += 1
        if walked[0] != walked[1]:
            diff = abs(walked[0] - walked[1])

            if walked[0] > walked[1]:
                walked[0] -= diff
            else:
                walked[1] -= diff
        if walked[2] != walked[3]:
            diff = abs(walked[2] - walked[3])
            if walked[2] > walked[3]:
                walked[2] -= diff
            else:
                walked[3] -= diff
        if walked[0] == walked[1] == 0 and walked[2] != 0 and walked[3] != 0:
            walked[2] = 1
            walked[3] = 1
            length = 2
        elif walked[2] == walked[3] == 0 and walked[0] != 0 and walked[1] != 0:
            walked[0] = 1
            walked[1] = 1
            length = 2

        res = "L" * walked[0] + "U" * walked[2] + "R" * walked[1] + "D" * walked[3]
        print(sum(walked))
        print(res)

