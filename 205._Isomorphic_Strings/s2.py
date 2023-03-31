

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        str1_map = {}
        str2_map = {}
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in str1_map and str1_map[ch1] !=ch2:
                return False
            if ch2 in str2_map and str2_map[ch2] !=ch1:
                return False
            str1_map[ch1] = ch2
            str2_map[ch2] = ch1
        return True


s = "aba"
t = "ete"
print(Solution(). isIsomorphic(s=s, t=t, ))
