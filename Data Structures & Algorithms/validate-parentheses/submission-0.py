class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s: 
            if char in closeToOpen: # check if it's a close bracket  
                if stack and stack[-1] == closeToOpen[char]: 
                    stack.pop()
                else: 
                    return False 

            else: 
                stack.append(char)

        return True if not stack else False 
        

"""
print(hello[s])
(,[,],)
"""

"""
print(hello[s]
(,[,]
"""

"""
print(hello[s](
(,[,],(
"""



