class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        a, b = a & MASK, b & MASK
        res = 0
        carry = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            current_sum = bit_a ^ bit_b ^ carry
            res |= (current_sum << i)
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)
        return res if res <= 0x7FFFFFFF else ~(res ^ MASK)