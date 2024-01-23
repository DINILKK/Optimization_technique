def knapsack(values, weights, capacity):
    n = len(values)

    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
               
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
           
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][capacity]


values = [6, 10, 12,10]
weights = [1, 2, 3,5]
capacity = 10

max_value = knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
