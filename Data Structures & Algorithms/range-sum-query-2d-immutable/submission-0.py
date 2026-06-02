class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rowNum, colNum = len(matrix), len(matrix[0])
        matSum = [[0] * (colNum+1) for _ in range(rowNum+1)]
        for i in range(rowNum):
            for j in range(colNum):
                matSum[i+1][j+1] = matSum[i][j+1] + matSum[i+1][j] + matrix[i][j] - matSum[i][j]
        self.matrix = matrix
        self.matSum = matSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.matSum[row2+1][col2+1] - self.matSum[row1][col2+1] - self.matSum[row2+1][col1] + self.matSum[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)