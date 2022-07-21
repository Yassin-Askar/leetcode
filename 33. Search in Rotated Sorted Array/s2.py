from turtle import right


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, hight = 0, len(nums) - 1

        while low <= hight:
            mid = (low + hight) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    hight = mid - 1

            else:
                if target < nums[mid] or target > nums[hight]:
                    hight = mid - 1
                else:
                    low = mid + 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

print(Solution().search(nums, target))
