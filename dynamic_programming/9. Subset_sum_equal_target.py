# https://www.codingninjas.com/codestudio/problems/subset-sum-equal-to-k_1550954

def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[False for j in range(k+1)] for i in range(n+1)]
    target = k
    for i in range(n):
        dp[i][0] = True
            
    if arr[0] <= k: dp[0][arr[0]] = True
    
    for i in range(1, n):
        for target in range(1, k+1):
            not_pick = dp[i-1][target]

            pick = False
            if target-arr[i] >= 0:
                pick = dp[i-1][target-arr[i]]

            dp[i][target] = pick or not_pick
    
    
    return dp[n-1][k]
    
    
    

