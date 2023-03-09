class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = 0
        i = 0
        while i < len(nums) and i <= goal:
            goal = max(goal,i+nums[i])
            i +=1
        return goal >= len(nums)-1


nums = []
print(Solution(). canJump(nums=nums, ))
