def isMatch(s, p):
    # Helper function that tries to match s[i:] with p[j:]
    def match(i, j):
        # If we've reached the end of both s and p, it's a match
        if i == len(s) and j == len(p):
            return True  # both are fully matched

        # If we've reached the end of the pattern but not the string, no match
        if j == len(p):
            return False  # pattern finished but string not

        # Check if current characters match
        current_match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')

        # Handle '*' wildcard in pattern
        if (j + 1) < len(p) and p[j + 1] == '*':
            # Two options:
            # 1. Skip the 'char*' part in pattern (treat as zero occurrences)
            # 2. If current char matches, move to next char in s, but stay on this pattern part
            return (
                match(i, j + 2) or
                (current_match and match(i + 1, j))
            )

        # If current char matches, move ahead in both s and p
        if current_match:
            return match(i + 1, j + 1)

        # If not matched, return False
        return False

    # Start recursion from the beginning of s and p
    return match(0, 0)