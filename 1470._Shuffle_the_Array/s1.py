class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        arr1 = []
        arr2 = []
        res = []
        for i in range(len(nums)):
            if i < n:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)):
            res.append(arr1[i])
            res.append(arr2[i])
        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
print(Solution(). shuffle(nums=nums, n=n, ))
