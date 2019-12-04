class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        wait = list()
        for i in range(len(T)):
            count = 0
            wait.append(count)
            for j in range(i + 1, len(T)):
                count += 1
                if T[i] < T[j]:
                    wait[-1] = count
                    break

        return wait