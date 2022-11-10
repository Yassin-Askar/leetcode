class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        w1 = ""
        w2 = ""
        for s in word1:
            w1 += s
        for s in word2:
            w2 += s

        return w1 == w2


print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
