class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = defaultdict(int)
        for num in nums:
            if num not in lst: 
                lst[num] = 1
            else: 
                lst[num] += 1 

        answer = []


        for _ in range(k):
            maxValue = -1
            maxKey = -1 
            
            for key, val in lst.items():
                if val > maxValue:
                    maxValue = val
                    maxKey = key
            
            answer.append(maxKey)
                        
            del lst[maxKey]

        return answer