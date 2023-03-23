class Solution:
    def sortColors(self, nums: list[int]) -> None:
        number_map = {0: 0, 1: 0, 2: 0}
        for i in range(len(nums)):
            if nums[i] not in number_map:
                number_map[nums[i]] = 1
            else:
                number_map[nums[i]] += 1

        i = 0

        for k, v in number_map.items():
            val = v
            while val > 0:
                nums[i] = k
                val -= 1
                i += 1


nums = [2, 0, 2, 1, 1, 0]
print(Solution(). sortColors(nums=nums, ))
