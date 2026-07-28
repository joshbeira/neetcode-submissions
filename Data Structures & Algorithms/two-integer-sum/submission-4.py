class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = target - num

        for i in d:
            if (d[i]) in nums:
                return [nums.index(i), nums.index(d[i])]



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
