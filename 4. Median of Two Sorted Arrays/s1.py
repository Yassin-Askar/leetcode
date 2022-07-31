import math
from pickle import HIGHEST_PROTOCOL


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        med = 0.0
        if len(nums1) % 2 == 0:
            med = (nums1[(len(nums1)+1)//2] + nums1[((len(nums1))//2)-1])/2
        else:
            med = nums1[(len(nums1)-1)//2]

        return med


nums1 = [1, 3]
nums2 = [2, 4]


print(Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2))
