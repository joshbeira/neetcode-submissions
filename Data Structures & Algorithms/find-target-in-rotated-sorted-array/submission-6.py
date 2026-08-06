class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0 
        while i < len(nums):
            if i == target: 
                return i 
            i = i + 1 