class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for char in s:
            s_map[char] = 0
        for char in t:
            t_map[char] = 0
        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1

        if s_map == t_map:
            return True
        else: 
            return False