class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m=len(matrix)
        n=len(matrix[0])
        self.dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.dp[i+1][j+1]=self.dp[i+1][j]+self.dp[i][j+1]-self.dp[i][j]+matrix[i][j]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
