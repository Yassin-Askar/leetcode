from ctypes import pointer
from re import sub


class Solution:
    def lengthOfLongestSubstring(s: str) -> int:  # type: ignore
        # type: ignore
        # alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
        # type: ignore
        sSet = set()
        length = 0
        max_length = 0
        for i in range(len(s)):
            print(length)
            while s[i] in sSet:
                sSet.remove(s[length])
                length += 1
            sSet.add(s[i])
            max_length = max(max_length, i-length+1)
        return max_length


word = "pwwkew"
print(Solution.lengthOfLongestSubstring(word))  # type: ignore
