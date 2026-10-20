class Solution:
    def isMatch(self, s, p):
        @lru_cache(maxsize=None)
        def dp(i, j):
            # If we've reached the end of the pattern
            if j == len(p):
                return i == len(s)
            # Does the current character match?
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            # Handle '*' (zero or more of the preceding element)
            if j + 1 < len(p) and p[j + 1] == '*':
                return dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                return first_match and dp(i + 1, j + 1)
        return dp(0, 0)