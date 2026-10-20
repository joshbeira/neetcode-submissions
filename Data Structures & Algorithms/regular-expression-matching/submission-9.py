class Solution:
    def isMatch(self, s, p):
        # Helper function that tries to match s[i:] with p[j:]
        def match(i, j):
            # If we've reached the end of the pattern
            if j == len(p):
                # Return True only if we've also reached the end of the string
                return i == len(s)
            # Check if the first character matches (make sure we're in bounds)
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            # If the next character in the pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Try two options:
                # 1. Skip '*' and its preceding char
                # 2. If first characters match, move to next char in string but keep pattern pointer
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                # Otherwise, move both pointers forward if first char matches
                return first_match and match(i + 1, j + 1)
        # Start matching from the beginning of both strings
        return match(0, 0)