class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = {}
        for char in s1:
            char_dict[char] = char_dict.get(char, 0) + 1
        l = 0
        s1_length = len(s1)
        s2_length = len(s2)
        while l < (s2_length - s1_length) + 1:
            # print(l)
            if s2[l] in s1:
                r = l
                loop_end = l + s1_length
                window_dict = {}
                while r < loop_end:
                    r_char = s2[r]
                    window_dict[r_char] = window_dict.get(r_char, 0) + 1
                    r += 1   
                if char_dict == window_dict:
                    return True
            l += 1
        return False