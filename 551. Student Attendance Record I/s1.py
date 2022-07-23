class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0
        for char in s:
            if char == 'L':
                l_count += 1
            else:
                l_count = 0
            if char == 'A':
                a_count += 1
            if l_count >= 3 or a_count >= 2:
                return False
        return True
