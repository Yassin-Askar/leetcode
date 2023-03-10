class Solution:
    def jump(self, nums: list[int]) -> int:
        goal = 0
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            goal = 0
            for i in range(l, r+1):
                goal = max(goal, i+nums[i])
            l = r+1
            r = goal
            jumps += 1
        return jumps


nums = [2, 3, 1, 1, 4]
print(Solution(). jump(nums=nums, ))
