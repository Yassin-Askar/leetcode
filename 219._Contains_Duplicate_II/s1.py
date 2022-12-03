class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        my_dict = {}
        for i, v in enumerate(nums):
            if v in my_dict and i - my_dict[v] <= k:
                return True
            my_dict[v] = i
        return False


nums = [1, 2, 3, 1]
k = 3
print(Solution(). containsNearbyDuplicate(nums=nums, k=k, ))
