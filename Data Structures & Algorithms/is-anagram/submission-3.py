class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = []
        if len(s) == len(t):
            for i in s:
                chars.append(i)
            for i in t:
                if i in chars:
                    try: 
                        chars.remove(i)
                    except: 
                        return False 
                else: 
                    return False 
        else:
            return False 

        return True
    