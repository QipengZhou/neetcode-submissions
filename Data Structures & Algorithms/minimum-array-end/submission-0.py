class Solution:
    def minEnd(self, n: int, x: int) -> int:
        num = n - 1
        res = x
        ix = 0
        inum = 0
        while (1 << inum) <= num:
            if (res & (1 << ix)) == 0:
                if (num & (1 << inum)) != 0:
                    res |= (1 << ix)
                inum += 1
            ix += 1
        return res