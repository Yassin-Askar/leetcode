class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        minimum = nums[0]
        while low <= high:
            mid = (high + low)//2

            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid-1

            minimum = min(minimum, nums[mid])

        return minimum


nums = [3, 4, 5, 0, 1, 2]

print(Solution().findMin(nums))
