class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        print(f"s :{s} : {s[::-1]}")
        return s == s[::-1]
