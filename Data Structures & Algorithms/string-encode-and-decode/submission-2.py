class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_strs = []
        for i in strs:
            le = len(i)
            encode_strs.append(f"{le}#{i}")
        return "".join(encode_strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        N = len(s)
        while i < N:
            hi = s.find('#', i)
            num = int(s[i:hi])
            si = hi+1
            ei = si + num
            strs.append(s[si:ei])
            i = ei
        return strs
