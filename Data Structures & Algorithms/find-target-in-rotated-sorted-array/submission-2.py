class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Keep searching as long as the search space is valid
        while l <= r:
            mid = (l + r) // 2 
            
            # Check the actual value in the array, not the index
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                l = mid + 1 
            else:
                r = mid - 1
                
        # Return -1 if the target is not found
        return -1