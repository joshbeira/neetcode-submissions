class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            remain = target - num
            try:
                j = nums.index(remain)
                i = nums.index(num)
                if i != j: 
                    return [i, j]
                else: 
                    continue 
            except: 
                continue
                
