
import heapq as hq


class MedianFinder:
    first_part: list
    second_part: list

    def __init__(self):
        self.first_part = []
        self.second_part = []

    def addNum(self, num: int) -> None:
        hq.heappush(self.first_part, -num)
        hq.heappush(self.second_part, -hq.heappop(self.first_part))
        if len(self.first_part) < len(self.second_part):
            hq.heappush(self.first_part, -hq.heappop(self.second_part))

    def findMedian(self) -> float:
        if len(self.first_part) == len(self.second_part):
            return (-self.first_part[0] + (self.second_part[0])) / 2
        return -self.first_part[0]
