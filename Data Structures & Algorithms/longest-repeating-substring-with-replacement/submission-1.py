class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            # update the character at R in the map by incrementing by 1. If the character doesn't exist, set a default value of 0
            count[s[r]] = 1 + count.get(s[r], 0)
            # maxf is an optimisation introduced to save the number of loops below. It represents the highest frequency encountered by any character. 
            # this works because we have already established that a substring of the same length exists.
            # also, maxf will only increment when the current window contains that many occurences of a character. so it will differ from the occurences in the current window
            maxf = max(maxf, count[s[r]])

            # this is the key condition. taking the window length - maxf tells you the number of characters to replace. if it's greater than k, it will NOT form a consecutive substring, so we increment the left pointer. 
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 
                l += 1

            res = max(res, r - l + 1)
        return res
