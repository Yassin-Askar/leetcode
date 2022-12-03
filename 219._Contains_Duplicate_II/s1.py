class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


nums = [1, 2, 3, 1]
k = 3
print(Solution(). containsNearbyDuplicate(nums=nums, k=k, ))
