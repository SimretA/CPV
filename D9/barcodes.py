class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        length = len(barcodes)
        
        for i in range(length//2):
            if i % 2 == 0:
                temp = barcodes[i]
                barcodes[i] = barcodes[length - i - 1]
                barcodes[length - i - 1] = temp
                print("swaping ", barcodes)
        return barcodes


if __name__ == '__main__':
    s = Solution()
    print(s.rearrangeBarcodes([1, 1, 2, 2, 2, 3]))
