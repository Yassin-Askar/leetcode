

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        sub = 0
        for c in s:
            right = len(t)-1
            while left <= right:
                if t[left] == c:
                    sub += 1
                    left += 1
                    break
                if t[right] == c:
                    left += 1
                else:
                    left += 1
                    right -= 1
        
        return sub == len(s)


s = "aaaaaa"
t = "bbaaaa"
print(Solution(). isSubsequence(s=s, t=t, ))
