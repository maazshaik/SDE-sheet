# https://leetcode.com/problems/house-robber/
class Solution:
    
    def f(self, idx, nums, dp):
        if idx == 0:
            return nums[idx]
        if idx < 0:
            return 0
        
        if dp[idx] != -1:
            return dp[idx]
        
        pick = nums[idx] + self.f(idx -2, nums, dp)
        not_pick = self.f(idx -1, nums, dp)
        
        dp[idx] = max(pick, not_pick)
        return dp[idx]
        
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.f(n-1, nums, dp)