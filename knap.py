def MaxProf(W, n, val, wt):

    # dp[i] is going to store maximum 
    # value with knapsack capacity i.
    dp = [0 for i in range(W + 1)] # 0 0 0 0 0 0

    

    # Fill dp[] using above recursive formula
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])

    print( "Maximum profit ", dp[W])


W = 5
val = [4,5,3,7]
wt = [2,3,1,4]
n = len(val)

MaxProf(W, n, val, wt)