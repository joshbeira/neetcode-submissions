class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in nums: 
                if i != j and (i + j == target):
                    return [i,j]



        # for num in nums:
        #     remain = target - num
        #     try:
        #         j = nums.index(remain)
        #         i = nums.index(num)
        #         if i != j: 
        #             return [i, j]
        #         else: 
        #             continue 
        #     except: 
        #         continue
        # return [0,0]
