

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:

        def transformString(s: str) -> str:
            index_mapping = {}
            new_str = []

            for i, c in enumerate(s):
                if c not in index_mapping:
                    index_mapping[c] = i
                new_str.append(str(index_mapping[c]))

            return " ".join(new_str)
        
        return transformString(s) == transformString(t)


s = "aba"
t = "ete"
print(Solution(). isIsomorphic(s=s, t=t, ))
