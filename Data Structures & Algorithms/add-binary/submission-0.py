class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []  # 用列表收集字符，最后一次性 join，效率比字符串相加更高
        cap = 0   # 进位 (carry)
        ia, ib = len(a) - 1, len(b) - 1
        
        # 只要 a 没加完，或者 b 没加完，或者最后还剩下一个孤零零的进位，循环就要继续
        while ia >= 0 or ib >= 0 or cap > 0:
            total = cap  # 先把上一轮的进位加上
            
            if ia >= 0:
                total += int(a[ia]) # 如果 a 还有剩，加上 a 的当前位值
                ia -= 1
                
            if ib >= 0:
                total += int(b[ib]) # 如果 b 还有剩，加上 b 的当前位值
                ib -= 1
            
            # 二进制的核心计算
            ans.append(str(total % 2))  # 当前位的结果
            cap = total // 2            # 计算新的进位
            
        # 因为我们是从后往前加的，收集到的结果是反的，最后需要逆序并拼接
        return "".join(ans[::-1])