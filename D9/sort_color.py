class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        result = []
        for i in nums:
            counter[i] += 1
        print(counter)
        index = 0
        for i in range(3):
            for j in range(counter[i]):
                nums[index] = i
                index += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2, 0, 2, 1, 1, 0]))
