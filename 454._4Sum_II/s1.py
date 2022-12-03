from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:

        length = len(nums1)
        my_dict = defaultdict(int)
        res = 0

        for i in range(length):
            for j in range(length):
                my_dict[nums1[i] + nums2[j]] += 1

        for i in range(length):
            for j in range(length):
                res += my_dict[0 - (nums3[i] + nums4[j])]

        return res


nums1 = [1, 2],
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
print(Solution(). fourSumCount(nums1=nums1,  # type: ignore
      nums2=nums2, nums3=nums3, nums4=nums4, ))
