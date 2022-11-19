class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        res = float("inf")
        for pointer_2 in range(len(nums)):
            total += nums[pointer_2]
            while total >= target:
                res = min(pointer_2 - left +1,res)
                total -= nums[left]
                left += 1
        return res if res != float("inf") else 0


target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(Solution(). minSubArrayLen(target=target, nums=nums, ))
