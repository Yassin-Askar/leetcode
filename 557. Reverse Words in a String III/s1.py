class Solution:
    def reverseWords(s: str) -> str:  # type: ignore
        s = s.split(" ")  # type: ignore

        for i in range(len(s)):
            s[i] = s[i][::-1]  # type: ignore

        s = " ".join(s)
        return s


s = "Let's take LeetCode contest"

print((Solution.reverseWords(s)))  # type: ignore
