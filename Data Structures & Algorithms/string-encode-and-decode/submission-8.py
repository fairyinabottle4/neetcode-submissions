class Solution:

    def encode(self, strs: List[str]) -> str:
        to_send = ""
        delimiter = "#"
        for s in strs:
            str_len = str(len(s))
            to_send += str_len
            to_send += delimiter
            to_send += s
        return to_send

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # i is at the number, j looks for the #
        while i != len(s):
            j = i
            while s[j] != '#':
                j += 1
            # when j finds the #, we know the number, convert to int
            length = int(s[i:j])
            #now we move to the actual string
            i = j+1
            j = i + length
            res.append(s[i:j])
            # 'catch up' i to j
            i = j
        return res
