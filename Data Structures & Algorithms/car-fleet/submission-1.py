class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        descSortedIndex = sorted(range(len(position)), key=lambda i: -position[i])
        stack = []
        for i in descSortedIndex:
            remaindSeconds = (target - position[i]) / speed[i]
            if len(stack) > 0 and remaindSeconds <= (target - position[stack[-1]])/speed[stack[-1]]:
                continue
            stack.append(i)
        return len(stack)