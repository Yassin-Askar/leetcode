class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.split()

        return len(s[-1])


s = "   fly me   to   the moon  "
print(Solution.lengthOfLastWord(s))
