class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            n1, n2 = n2, n1
        if num2 == '0':
            return '0'
        num = [0] * (n1 + n2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(n1):
            for j in range(n2):
                num[i+j] += int(num1[i]) * int(num2[j])
                num[i+j+1] += num[i+j] // 10
                num[i+j] %= 10

        while len(num) > 1 and num[-1] == 0:
            num.pop()
        return "".join(map(str, num[::-1]))