class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "‽"

        return res  


    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for c in s:
            while c != "‽": 
                word += c 
            res.append(word)
            word = ""
        return res
        

