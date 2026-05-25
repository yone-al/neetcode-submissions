class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = defaultdict(int)
            for c in s:
                count[c] += 1
            key = tuple(sorted(count.items()))
            res[key].append(s)
        return list(res.values())