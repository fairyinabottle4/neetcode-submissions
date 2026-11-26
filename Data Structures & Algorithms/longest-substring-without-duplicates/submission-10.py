class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        chars = set()
        while r < len(s):
            l_char = s[l]
            r_char = s[r]
            while r_char in chars:
                chars.remove(l_char)
                l += 1
                l_char = s[l]
            chars.add(r_char)
            curr_len = r - l + 1
            if curr_len > res:
                res = curr_len
            r += 1
        return res