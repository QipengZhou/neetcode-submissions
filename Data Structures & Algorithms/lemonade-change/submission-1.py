class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        remaind = {0: len(bills), 5: 0, 10: 0, 20: 0}
        for i, bill in enumerate(bills):
            r = bill - 5
            while r > 0:
                t = min(r // 10, remaind[10])
                if t == 0:
                    break
                r -= 10 * t
                remaind[10] -= t
            while r > 0:
                t = min(r // 5, remaind[5])
                if t == 0:
                    break
                r -= 5 * t
                remaind[5] -= t
            if r > 0:
                return False
            remaind[bill] += 1
        return True