class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            remain = target - num
            try:
                j = nums.index(remain)
                i = nums.index(num)
                return [i, j]
            except: 
                continue
                
        