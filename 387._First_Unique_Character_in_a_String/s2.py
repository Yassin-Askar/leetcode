from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for k,v in count.items():
            if v ==1:
                return s.index(k)
        return -1
s = "leetcode"
print(Solution(). firstUniqChar(s=s, ))
