def getEditDistance(a, b):
    aLen = len(a)
    bLen = len(b)

    if aLen == 0 or bLen == 0:
        return aLen + bLen
    dp = [[0] * (bLen + 1) for i in range(aLen + 1)]

    for i in range(aLen + 1):
        dp[i][0] = i
    for i in range(bLen + 1):
        dp[0][i] = i

    for i in range(1, aLen + 1):
        for j in range(1, bLen + 1):
            if a[i - 1] != b[j - 1]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
    return dp[aLen][bLen]
