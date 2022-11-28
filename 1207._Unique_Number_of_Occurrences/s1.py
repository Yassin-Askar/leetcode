class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        numbers_count = {}
        set_number = set()
        for num in arr:
            if num in numbers_count:
                numbers_count[num] += 1
            else:
                numbers_count[num] = 1
        for v in numbers_count.items():
            set_number.add(v[1])

        return len(numbers_count) == len(set_number)


arr = [1, 2]
print(Solution(). uniqueOccurrences(arr=arr, ))
