class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        for i in strs: 
            group = []
            seen = []
            for j in strs:
                if sorted(i) == sorted(j): 
                    if j not in seen:
                        seen.append(j)
                        group.append(j)

            answer.append(group)

        return answer 
