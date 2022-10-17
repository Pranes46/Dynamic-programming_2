def knapsack (val,wt,m,n):
    
    dp= [[ 0 for _ in range (m+1)] for s in range  (n+1)]
    
    
    
    for i in range(n+1):
        for j in range(m+1):
           
            if j<wt[i-1]:
                
                dp[i][j]=dp[i-1][j]
            else:
                
                dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
             
    return dp[-1][-1]
    
val=[1,4,5,7]
wt=[1,3,4,5]
m=7
n=len(val)
print(knapsack(val,wt,m,n))