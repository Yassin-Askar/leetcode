class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        if len(nums1) >= len(nums2):
            max_list = set(nums1)
            min_list = set(nums2)
        else:
            max_list = set(nums2)
            min_list = set(nums1)
        max_list = sorted(list(max_list))
        for n in min_list:
            h = len(max_list)-1
            l = 0
            while h >= l:
                mid = (h+l)//2

                if max_list[mid] == n:
                    res.append(n)
                    break
                elif max_list[mid] > n:
                    h -= 1
                elif max_list[mid] < n:
                    l += 1
        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution(). intersection(nums1=nums1, nums2=nums2, ))
