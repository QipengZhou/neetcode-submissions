class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for v in asteroids:
            alive = True
            while alive and v < 0 and stack and stack[-1] > 0:
                if stack[-1] < -v:
                    stack.pop()
                elif stack[-1] == -v:
                    alive = False
                    stack.pop()
                else:
                    alive = False
            if alive:
                stack.append(v)
        return stack