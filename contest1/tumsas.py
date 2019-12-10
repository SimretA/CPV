if __name__ == '__main__':
    times = int(input())
    for _ in range(times):
        n = int(input())
        p = input().split()

        q = [0] * n
        for i, number in enumerate(p):
            q[int(number) - 1] = i

        left = right = q[0]
        res = []
        for k, i in enumerate(q):
            if i < left:
                left = i
            elif i > right:
                right = i
            res.append('1' if right - left == k else '0')
        print(''.join(res))