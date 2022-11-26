class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        res = [-1] * (len(nums))

        stack = []

        for i in list(range(len(nums))) * 2:

            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res


print(Solution(). nextGreaterElements(nums=[1, 2, 3, 4, 3], ))
