def merge_sort(list1):
    if len(list1) > 1:
        results = list()
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)

        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1
        while i < len(left):
            results.append(left[i])
            i += 1
        while j < len(right):
            results.append(right[j])
            j += 1
        return results





if __name__ == '__main__':
    list1 = [3, 22, 9, 11]
    print(merge_sort(list1))