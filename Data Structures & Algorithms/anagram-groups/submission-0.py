from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        res = []
        strMaps = []
        for s in strs:
            mp = defaultdict(int)
            for c in s:
                mp[c] += 1
            found = False
            for i, v in enumerate(res):
                if len(v[0]) == len(s):
                    found = True
                    for kk, vv in strMaps[i].items():
                        if mp[kk] != vv:
                            found = False
                            break
                    if found:
                        res[i].append(s)
                        break
            if not found:
                res.append([s])
                strMaps.append(mp)
        return res
        