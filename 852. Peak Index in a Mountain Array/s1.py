import math


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low, high = 0, len(arr)-1
        peak = 0
        while low <= high:
            mid = math.ceil((low + high) / 2)

            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1
            if arr[mid] > arr[peak]:
                peak = mid
        return peak
