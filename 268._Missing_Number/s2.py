def swap(a, b):
    """Swap the values of two variables."""
    temp = a
    a = b
    b = temp
    return a, b
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        i = 0

        arr_len=len(nums)
        while i < arr_len:
            value = nums[i]
            if nums[i] != i and nums[i] < arr_len-1:
                nums[i], nums[value] = nums[value], nums[i]

            elif value >= arr_len:
                i+=1

            else:
                i += 1

        for x in range(arr_len):
            if x != nums[x]:
                return x
        return i


nums = [3, 0, 1]
print(Solution(). missingNumber(nums=nums, ))
