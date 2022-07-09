class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.split()

        return len(s[-1])


print(Solution.lengthOfLastWord(s))
