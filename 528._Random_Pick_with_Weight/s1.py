import random


class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sum = []
        self.total_sum = 0
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        x = random.randint(1, self.total_sum)
        left, right = 0, len(self.prefix_sum) - 1
        while left <= right:
            mid = (left+right) // 2
            if self.prefix_sum[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

w = [1]
print(Solution(w=w))
