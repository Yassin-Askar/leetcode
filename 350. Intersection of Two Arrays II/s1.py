import re


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        nums2 = sorted(nums2)
        for num in nums1:
            height = len(nums2)-1
            low = 0
            while low <= height:
                mid = (low + height) // 2

                if nums2[mid] == num:
                    res.append(num)
                    nums2.remove(num)
                    break

                if nums2[mid] >= num:
                    height = mid - 1
                else:
                    low = mid + 1
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(Solution().intersect(nums1=nums1, nums2=nums2))
