#https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:                
        prev = [-1] * n
        for i in range(m):
            cur = [-1] * n
            for j in range(n):
                if i == 0 or j == 0:
                    cur[j] = 1
                    continue
                
                up = 0
                if i > 0:
                    up = prev[j]
                
                left = 0
                if j > 0:
                    left = cur[j-1]
                
                cur[j] = up + left
            
            prev = cur
        
        
        return prev[n-1]