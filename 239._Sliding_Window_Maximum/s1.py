import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = collections.deque()
        right = left = 0
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            if left > q[0]:
                q.popleft()
            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution(). maxSlidingWindow(nums=nums, k=k, ))
