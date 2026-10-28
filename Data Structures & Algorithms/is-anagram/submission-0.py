class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        set1 = {}
        set2 = {}

        for char in s:
            if char in set1:
                set1[char] += 1
            else:
                set1[char] = 0
        for char in t:
            if char in set2:
                set2[char] += 1
            else:
                set2[char] = 0
        
        if len(set1) != len(set2): return False

        for entry in set1:
            if entry not in set2: return False
            if set1[entry] != set2[entry]:
                return False
        return True

        
