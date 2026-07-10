class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        seen = set()  # Using a set for faster lookups
        
        # Loop by index instead of value
        for i in range(len(strs)): 
            # Optimization: if we already grouped this word, skip it entirely
            if i in seen:
                continue
                
            group = []
            for j in range(len(strs)):
                # Only check j if we haven't used its exact index yet
                if j not in seen:
                    if sorted(strs[i]) == sorted(strs[j]): 
                        seen.add(j)       # Add the index to seen
                        group.append(strs[j]) # Append the actual string to group

            if len(group) != 0: 
                answer.append(group)

        return answer