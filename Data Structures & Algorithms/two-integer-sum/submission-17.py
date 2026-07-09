class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]: 
                return [i, nums.index((target - nums[i]), i+1 , len(nums))]


        # d = {}
        
        # for num in nums:
        #     d[num] = target - num

        # for i in d:
        #     if (d[i]) in nums:
        #         return [nums.index(i), nums.index(d[i],nums.index(d[i]), len(nums))]



        # for i in range(len(nums)):
        #     for j in range(len(nums)): 
        #         if i != j and (nums[i] + nums[j] == target):
        #             return [i,j]




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
