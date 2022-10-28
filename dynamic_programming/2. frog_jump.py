#https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

from typing import *
import sys

def f(idx, heights, dp):
    if idx == 0:
        return 0
    if idx < 0:
        return sys.maxsize
    
    if dp[idx] != -1:
        return dp[idx]
    step1 = f(idx-1, heights, dp) + abs(heights[idx-1] - heights[idx])
    step2 = sys.maxsize
    if idx > 1: step2 = f(idx-2, heights, dp) + abs(heights[idx-2] - heights[idx])
    
    dp[idx] = min(step1, step2)
    return dp[idx]
    
    
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [-1] * n
    
    for idx in range(n):
        if idx == 0:
            dp[idx] = 0
            continue
            
        step1 = dp[idx-1] + abs(heights[idx-1] - heights[idx])
        step2 = sys.maxsize
        if idx > 1: step2 = dp[idx-2] + abs(heights[idx-2] - heights[idx])
        
        dp[idx] = min(step1, step2)
    
    return dp[n-1]
