

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        left = 0
        right = 1
        while (len(arr)) > right:
            if diff != (arr[left] - arr[right]):
                return False
            left += 1
            right += 1
        return True


arr = [0, 0]
print(Solution(). canMakeArithmeticProgression(arr=arr, ))
