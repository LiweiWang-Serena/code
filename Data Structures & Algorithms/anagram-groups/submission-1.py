class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} #initialise dict for group
        for i in strs:
            s = "".join(sorted(i))
            if s not in group:
                group[s] = [i]
            else:
                group[s].append(i)
        return list(group.values())