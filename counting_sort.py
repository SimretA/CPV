def counting_sort(list1):
    maxi = mini = list1[0]
    counter = list()
    sorted = list()
    for i in list1:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    for i in range(mini, maxi+1):
        counter.append(0)
    for i in list1:
        counter[maxi-i] += 1
    for i in range(len(counter)):
        for j in range(counter[i]):
            sorted.append(mini+i)
    return sorted

if __name__ == '__main__':
    print(counting_sort([6, 3, 2, 5, 0, 7, 10, 8, 4, 1, 9]))