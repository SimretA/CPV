class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        for i in nums1:
            if i in dictionary:
                continue
            for j in nums2:
                if i == j:
                    dictionary[i] = 1
        return list(dictionary.keys())


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersection([1, 2, 2, 7, 1], [2, 2, 7]))