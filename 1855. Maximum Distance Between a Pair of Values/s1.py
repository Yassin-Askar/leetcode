class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res, j-i)
                j += 1
            else:
                i += 1
                j += 1
        return res


nums1 = [55, 30, 5, 4, 2]
nums2 = [100, 20, 10, 10, 5]

print(Solution().maxDistance(nums1=nums1, nums2=nums2))
