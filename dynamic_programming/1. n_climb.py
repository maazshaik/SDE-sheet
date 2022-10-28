# https://leetcode.com/problems/climbing-stairs/

class Solution:
#     def climbStairs(self, n: int) -> int:
#         prev2 = 0
#         prev = 0
        
#         for idx in range(n+1):
#             if idx == 0:
#                 prev = 1
#                 continue
            
            
#             step1 = prev
            
#             step2 = 0
#             if idx >  1: step2 = prev2
        
#             prev2 = prev
#             prev = step1 + step2

#         return prev
    
#     def f(self, n, dp):
#         if n == 0:
#             return 1
        
#         if dp[n] != -1:
#             return dp[n]
        
#         step_1 = self.f(n-1, dp)
        
#         step_2 = 0
#         if n > 1: step_2 = self.f(n-2, dp)
         
#         dp[n] = step_1 + step_2
#         return dp[n]
    
    
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        
        dp[0] = 1
        
        for i in range(1, n+1):
            step_1 = dp[i-1]
        
            step_2 = 0
            if i > 1: step_2 = dp[i-2]
            
            
            dp[i] = step_1 + step_2
        
        
        return dp[n]