# https://leetcode.com/problems/triangle/

class Solution:
    def f(self, i,j, triangle, dp):
        if i == (len(triangle) - 1):
            return triangle[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        sumDown = triangle[i][j] + self.f(i+1, j, triangle, dp)
        sumDiagonal = triangle[i][j] + self.f(i+1, j+1, triangle, dp)
        
        dp[i][j] = min(sumDown, sumDiagonal)
        return dp[i][j]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = [[-1 for j in range(i)] for i in range(1, row+1)]
        return self.f(0, 0, triangle, dp)