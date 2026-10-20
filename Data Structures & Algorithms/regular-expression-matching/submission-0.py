class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if (j + 1) < len(p) and p[j+1] == '*':
                # Two choices: skip "x*" or use one match (and try to use again)
                return dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                return first_match and dp(i+1, j+1)
        return dp(0, 0)