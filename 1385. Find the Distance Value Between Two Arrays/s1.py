

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2 = sorted(arr2)
        d_value = 0
        for num in arr1:
            low = 0
            valid = True
            hight = len(arr2)
            while low < hight:
                mid = (hight + low)//2
                if abs(arr2[mid]-num) <= d:
                    valid = False
                    break
                elif arr2[mid] > num:
                    hight = mid
                else:
                    low = mid + 1

            if valid:
                d_value += 1
        return d_value
