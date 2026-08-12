class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        for i in range(3, n+1):
            tri[i%3] = sum(tri)
        return tri[n%3]
        