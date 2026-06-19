class Solution:
    def calPoints(self, operations: List[str]) -> int:
        container = []
        for op in operations:
            if op == "+":
                container.append(container[-2] + container[-1])
            elif op == "D":
                container.append(2 * container[-1])
            elif op == "C":
                container.pop()
            else:
                container.append(int(op))
        return sum(container)