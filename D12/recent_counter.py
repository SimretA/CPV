class RecentCounter(object):

    def __init__(self):
        self.recents = list()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        if len(self.recents) == 0:
            self.recents.append(t)
            return 1
        else:
            while len(self.recents) > 0 and t - self.recents[0] > 3000:
                self.recents.pop(0)
            self.recents.append(t)
            return len(self.recents)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)