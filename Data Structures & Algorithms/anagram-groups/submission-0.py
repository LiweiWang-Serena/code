class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {} #initialise dict
        for string in strs:
            count = "".join(sorted(string))
            if count in group:
                group[count].append(string)
            else:
                group[count] = [string]
        return list(group.values())
