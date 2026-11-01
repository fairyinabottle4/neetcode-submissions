class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        pattern = r'\w'
        is_invalid = re.search(r'\w', s) is None
        print(s)
        print(is_invalid)
        if is_invalid:
            return True
        else:
            s_lower = s.lower()
            s_filtered = re.findall(pattern, s_lower)
            s_combined = "".join(s_filtered)
            head = s_combined[0]
            tail = s_combined[-1]
            middle = s_combined[1:-1]
            ends_match = head == tail
            return ends_match and self.isPalindrome(middle)
        