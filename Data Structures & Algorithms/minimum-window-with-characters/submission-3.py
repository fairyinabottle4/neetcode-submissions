class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        res = ""
        if t_len > s_len:
            return ""
        # create dictionaries
        t_dict = {}
        window_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        l = 0
        tracker = 0
        required = len(t_dict)

        for r in range(s_len):
            # Expand window
            r_char = s[r]
            window_dict[r_char] = window_dict.get(r_char, 0) + 1

            # the below requirement tracks a moment a required character is satisfied. 
            if r_char in t_dict and window_dict[r_char] == t_dict[r_char]:
                tracker += 1

            # Shrink window while valid
            while tracker == required:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]

                l_char = s[l]
                window_dict[l_char] -= 1

                if l_char in t_dict and window_dict[l_char] < t_dict[l_char]:
                    tracker -= 1

                if window_dict[l_char] == 0:
                    del window_dict[l_char]

                l += 1

        return res        