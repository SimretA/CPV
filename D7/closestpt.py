import math


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance = []
        res = []
        for point in points:
            dis = math.sqrt((point[0]**2) + (point[1]**2))
            distance[str(dis)] = point
        for i in sorted(distance.keys()):
            res.append(distance[i])
        print(res)


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[0,1],[1,0]], 2))