from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            if count[c]:
                count[c] += 1
            else:
                count[c] = 1
        for c in s:
            if count[c] == 1:
                return s.index(c)

        return -1


s = "leetcode"
print(Solution(). firstUniqChar(s=s, ))
