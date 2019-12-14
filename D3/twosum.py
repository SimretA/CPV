def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if (i == j):
                continue
            if target == nums[i] + nums[j]:
                return [i, j]


if __name__ == '__main__':
    print(twoSum([1, 2, 5, 6], 11))