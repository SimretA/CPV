def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """

    result = [0] * len(A)
    next_odd = 1
    next_even = 0
    for i in range(len(A)):
        if is_even(A[i]):
            result[next_even] = A[i]
            next_even += 2
        else:
            result[next_odd] = A[i]
            next_odd += 2
    return result


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    print(sortArrayByParityII([5, 2, 10, 0, 8, 1, 3, 7, 6, 9, 4]))
    #print([0]*12)