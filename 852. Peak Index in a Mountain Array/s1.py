import math


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low, hight = 0, len(arr)-1
        peak = 0
        while low <= hight:
            mid = math.ceil((low + hight) / 2)

            if arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                hight = mid - 1
            if arr[mid] > arr[peak]:
                peak = mid
        return peak
