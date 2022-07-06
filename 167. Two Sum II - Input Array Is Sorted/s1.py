class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            index1, index2 = i + 1, len(nums) - 1
            while index1 < index2:

                sums = a + nums[index1] + nums[index2]
                if sums < 0:
                    index1 += 1
                elif sums > 0:
                    index2 -= 1
                else:
                    ans.append([a, nums[index1], nums[index2]])
                    index1 += 1
                    while nums[index1] == nums[index1 - 1] and index1 < index2:
                        index1 += 1
        return ans
