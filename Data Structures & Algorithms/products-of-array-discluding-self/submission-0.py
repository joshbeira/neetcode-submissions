class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZero = 0
        product = 1
        for i in nums:
            if i == 0: 
                numZero += 1 
            else: 
                product *= i

        res = []
        for num in nums:
            if numZero > 1: 
                res.append(0) 
                
            elif numZero == 1:
                if num == 0:
                    res.append(product) 
                else:
                    res.append(0)                    
            else:
                res.append(product // num)

        return res

        