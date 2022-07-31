import math


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low, height = 0, len(arr)-1
        peak = 0
        while low <= height:
            mid = math.ceil((low + height) / 2)

            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                height = mid - 1
            if arr[mid] > arr[peak]:
                peak = mid
        return peak
