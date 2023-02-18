class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        seen = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            seen.add(s[i:i+10])
        return list(res)


s = "AAAAAAAAAAAAA"
print(Solution(). findRepeatedDnaSequences(s=s, ))
