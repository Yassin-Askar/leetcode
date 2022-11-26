class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        numbers = {}
        res = [-1] * (len(nums1))
        for i, num in enumerate(nums1):
            numbers[num] = i
        stack = []
        for i, _ in enumerate(nums2):
            num = nums2[i]
            while stack and num > stack[-1]:
                pop_val = stack.pop()
                index = numbers[pop_val]
                res[index] = num
            if num in numbers:
                stack.append(num)
        return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution(). nextGreaterElement(nums1=nums1, nums2=nums2))
