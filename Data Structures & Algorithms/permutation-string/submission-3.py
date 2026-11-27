class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        char_dict = {}
        window_dict = {}

        # Initialize frequency dictionaries
        for char in s1:
            char_dict[char] = char_dict.get(char, 0) + 1

        for char in s2[:s1_length]:
            window_dict[char] = window_dict.get(char, 0) + 1

        # Check the first window
        if char_dict == window_dict:
            return True

        # Slide the window
        for r in range(s1_length, s2_length):
            l = r - s1_length

            # Remove character leaving the window
            l_char = s2[l]
            window_dict[l_char] -= 1

            if window_dict[l_char] == 0:
                del window_dict[l_char]

            # Add character entering the window
            r_char = s2[r]
            window_dict[r_char] = window_dict.get(r_char, 0) + 1

            if char_dict == window_dict:
                return True

        return False