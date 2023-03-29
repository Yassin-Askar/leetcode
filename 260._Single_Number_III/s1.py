class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
            bitwise_sum = 0
            for i in nums:
                bitwise_sum ^= i
            bitwise_mask = bitwise_sum & (-bitwise_sum)
            results = 0
            for i in nums:
                if bitwise_mask & i:
                    results = results ^ i

            return [results, bitwise_sum ^ results]




nums =[1,2,1,3,2,5]
print(Solution(). singleNumber(nums = nums , ))