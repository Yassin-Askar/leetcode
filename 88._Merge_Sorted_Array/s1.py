class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        nums1 += nums2
        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(Solution(). merge(nums1=nums1, m=m, nums2=nums2, n=n, ))
