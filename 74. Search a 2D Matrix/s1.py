class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        for li in matrix:
            h = len(li)-1
            l = 0
            mid = 1
            if target > li[h]:
                continue

            while h >= l:
                mid = (h+l)//2
                if li[mid] == target:
                    return True
                if li[mid] > target:
                    h -= 1
                if li[mid] < target:
                    l += 1

        return False
