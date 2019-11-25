def quick_sort(list1):
    if len(list1) > 1:
        left = list()
        right = list()
        pivot = list1[-1]
        for i in range(0, len(list1)-1):
            if list1[i] > pivot:
                right.append(list1[i])
            else:
                left.append(list1[i])
        print("left pivot right", left, pivot, right)
        if len(left) > 0:
            left = quick_sort(left)
        if len(right) > 0:
            right = quick_sort(right)
        return left + [pivot] + right
    else:
        return list1



if __name__ == '__main__':
    list1 = [3, 10, 22, 9, 11]
    print(quick_sort(list1))