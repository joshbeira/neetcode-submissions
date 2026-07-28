class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        seen = []
        for i in strs: 
            group = []
            for j in strs:
                if sorted(i) == sorted(j): 
                    if j == "":
                        group.append(j)
                    elif j not in seen:
                        seen.append(j)
                        group.append(j)

            if len(group) != 0: 
                answer.append(group)

        return answer 
