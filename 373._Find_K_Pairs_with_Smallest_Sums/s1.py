import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 and nums2:
            return []
        first_arr_len = len(nums1)
        second_arr_len = len(nums2)
        res = []
        min_heap = [(nums1[0]+nums2[0], 0, 0)]
        visited = set()
        while min_heap and len(res) < k:
            _, i, j = heapq.heappop(min_heap)
            if (i, j) not in visited:
                res.append([nums1[i], nums2[j]])
                visited.add((i, j))
            else:
                continue
            if i+1 < first_arr_len:
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], i+1, j))
            if j+1 < second_arr_len:
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))

        return res


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
print(Solution().kSmallestPairs(nums1=nums1, nums2=nums2, k=k, ))
