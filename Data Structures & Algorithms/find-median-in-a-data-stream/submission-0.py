import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for lower half (invert sign)
        self.low = []
        # Min-heap for upper half
        self.high = []

    def addNum(self, num: int) -> None:
        # Add to max-heap (as negative for max-heap)
        heapq.heappush(self.low, -num)
        # Make sure every num in low <= every num in high
        if self.low and self.high and (-self.low[0] > self.high[0]):
            moved = -heapq.heappop(self.low)
            heapq.heappush(self.high, moved)
        # Balance sizes (low can have 1 more than high)
        if len(self.low) > len(self.high) + 1:
            moved = -heapq.heappop(self.low)
            heapq.heappush(self.high, moved)
        if len(self.high) > len(self.low):
            moved = heapq.heappop(self.high)
            heapq.heappush(self.low, -moved)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        else:
            return (-self.low[0] + self.high[0]) / 2.0
