def isMatch(s, p):
    # If pattern is empty, string must also be empty
    if not p:
        return not s  # return True if s is empty too

    # Check if first character matches (if s is not empty and (first char same or p[0] is '.'))
    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

    # If pattern length >= 2 and p[1] is '*'
    if len(p) >= 2 and p[1] == '*':
        # Try skipping 'X*' in pattern, or consume one character if match
        return (isMatch(s, p[2:]) or  # Skip X*
                (first_match and isMatch(s[1:], p)))  # Use one instance of X (if match)
    else:
        # Otherwise, must match first char and move both pointers forward
        return first_match and isMatch(s[1:], p[1:])