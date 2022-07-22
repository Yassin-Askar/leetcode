class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        i = 0
        for i in range(1, len(arr)+k+1):
            if i not in arr:
                k -= 1
                if k == 0:
                    return i
        return i


arr = [2, 3, 4, 7, 11]
k = 2

print(Solution().findKthPositive(arr, k))
