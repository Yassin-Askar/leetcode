

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        res = []
        for d in range(2):
            i = -1
            low, hight = 0, len(nums)-1

            while low <= hight:
                mid = (low + hight)//2
                guess = nums[mid]
                if guess < target:
                    low = mid + 1
                elif guess > target:
                    hight = mid - 1
                else:
                    i = mid

                    if d:
                        low = mid + 1
                    else:
                        hight = mid - 1
            res.append(i)
        return res


nums = [8, 8, 8, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))
