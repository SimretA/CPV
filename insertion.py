if __name__ == '__main__':
    list1 = [3, 2, 1, 4]
    for i in range(1, len(list1)):
        for j in range(0, i):
            if list1[i] < list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    print(list1)
