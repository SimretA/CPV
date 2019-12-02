class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        distancep = [0]
        matr = [[r0, c0]]
        for i in range(R):
            for j in range(C):
                print(distancep)
                print(matr)
                if i == r0 and j == c0:
                    continue

                dis = abs(i - r0) + abs(j - c0)
                for k in range(len(distancep)-1, -1, -1):
                    if dis > distancep[k]:
                        distancep.insert(k+1, dis)
                        matr.insert(k+1, [i, j])
                        break
        return matr


if __name__ == '__main__':
    s = Solution()
    print(s.allCellsDistOrder(2, 2, 0, 1))
