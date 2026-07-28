class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = True 
        chars = []
        for i in s:
            chars.append(i)
        for i in t:
            if i not in chars:
                anagram = False 
        return anagram  

        