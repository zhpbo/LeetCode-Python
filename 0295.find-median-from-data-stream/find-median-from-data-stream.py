from heapq import *
class MedianFinder(object):
# 维护两个堆，一个大顶堆，一个小顶堆，小顶堆里的数比大顶堆里的数都要大， 
# 如果有两个潜在的中位数（两个堆size相同），数据流的中位数就是两个堆顶之和除以2
# 如果只有一个中位数，就看size更小的那个堆的堆顶
# 新进来的数都丢进小顶堆，然后把小顶堆的堆顶丢到大顶堆，
# 调整两个堆，使得size 差最大为1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = list()
        self.min_h = list()
        heapify(self.max_h)
        heapify(self.min_h)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.min_h, num)
        heappush(self.max_h, -heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h, -heappop(self.max_h))

    def findMedian(self):
        """
        :rtype: float
        """
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        if max_len == min_len: #有两个候选中位数
            return (self.min_h[0] + -self.max_h[0]) / 2.
        else:#小顶堆的size 一定 >= 大顶堆的size，所以答案就是小顶堆的堆顶
            return self.min_h[0] / 1.
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()