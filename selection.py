if __name__ == '__main__':
    list1 = [2, 5, 11, 7]
    for i in range(0, len(list1)):
        min_index = i
        for j in range(i, len(list1)):
            if list1[min_index] > list1[j]:
                min_index = j
        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp
    print(list1)