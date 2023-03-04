class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # check if left half is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # check if right half is sorted
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # if nums[left] == nums[mid], skip the duplicates
                left += 1
        return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(Solution().search(nums, target=target))
