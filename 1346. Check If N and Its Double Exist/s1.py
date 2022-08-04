

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        count = 0

        for n in range(len(arr)):

            low = 0
            high = len(arr)-1
            if arr[n] == 0:
                count += 1
                if count == 2:
                    return True
                continue
            while low <= high:

                mid = (low + high)//2

                if arr[mid] == (2*arr[n]):

                    return True
                elif arr[mid] > (2*arr[n]):
                    high = mid - 1
                else:
                    low = mid + 1
        return False


arr = [-2, 0, 10, -19, 4, 6, -8]
print(Solution().checkIfExist(arr))
