class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = list()
        for i in arr2:
            count = 0
            while len(arr1) > count:
                if i == arr1[count]:
                    result.append(arr1.pop(count))
                    continue
                count += 1
        if len(arr1) > 0:
            result += sorted(arr1)
        return result


if __name__ == '__main__':
    c = Solution()
    print(c.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
