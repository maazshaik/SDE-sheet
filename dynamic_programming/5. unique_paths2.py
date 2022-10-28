#https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        prev = [0] * n
        for i in range(m):
            cur = [0] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                    continue
                
                if i==0 and j==0:
                    cur[j] = 1
                    continue
                
                up = 0
                if i > 0: up = prev[j] 
                
                left = 0
                if j > 0: left = cur[j-1]
                
                cur[j] = up + left
                
            prev = cur
        
        return prev[n-1]