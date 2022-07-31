

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        res = []
        for d in range(2):
            i = -1
            low, height = 0, len(nums)-1

            while low <= height:
                mid = (low + height)//2
                guess = nums[mid]
                if guess < target:
                    low = mid + 1
                elif guess > target:
                    height = mid - 1
                else:
                    i = mid

                    if d:
                        low = mid + 1
                    else:
                        height = mid - 1
            res.append(i)
        return res


nums = [8, 8, 8, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))
